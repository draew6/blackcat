from ..models import Proxy
import httpx


class WebShareProvider:
    def __init__(self, token: str):
        self.token = token
        self.proxies = self.get_proxies()

    def get_proxies(self) -> list[Proxy]:
        response = httpx.get(
            "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=1000",
            headers={"Authorization": f"Token {self.token}"},
        )
        data = response.json()
        return [
            Proxy(
                provider="webshare",
                username=proxy["username"],
                password=proxy["password"],
                host=proxy["proxy_address"],
                port=proxy["port"],
                provider_external_id=proxy["id"],
                country_code=proxy["country_code"],
                created_at=proxy["created_at"],
                asn_name=proxy["asn_name"],
                asn_number=proxy["asn_number"],
            )
            for proxy in data["results"]
        ]
