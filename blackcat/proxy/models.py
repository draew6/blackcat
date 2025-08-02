from pydantic import BaseModel, Field
from datetime import datetime, UTC


class Proxy(BaseModel):
    provider: str
    username: str | None = None
    password: str | None = None
    host: str
    port: int
    provider_external_id: str | int
    country_code: str  #  ISO 3166‑1 alpha‑2
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    asn_name: str
    asn_number: int

    @property
    def ip(self):
        return self.get_ip(self.username, self.password, self.host, self.port)

    @staticmethod
    def get_ip(username: str | None, password: str | None, host: str, port: int) -> str:
        if username and password:
            return f"{username}:{password}@{host}:{port}"
        return f"{host}:{port}"

    @staticmethod
    def split_ip(ip: str) -> tuple[str | None, str | None, str, int]:
        if "@" in ip:
            user_pass, host_port = ip.split("@", 1)
            if ":" in user_pass:
                username, password = user_pass.split(":", 1)
            else:
                username, password = user_pass, None
        else:
            username, password = None, None
            host_port = ip

        host, port_str = host_port.rsplit(":", 1)
        port = int(port_str)
        return username, password, host, port

    @property
    def data(self):
        return (
            self.provider,
            self.username,
            self.password,
            self.host,
            self.port,
            self.provider_external_id,
            self.country_code,
            self.asn_name,
            self.asn_number,
        )
