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
        if self.username and self.password:
            return f"{self.username}:{self.password}@{self.host}:{self.port}"
        return f"{self.host}:{self.port}"
