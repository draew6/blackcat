import uuid
from datetime import datetime, timedelta

from .models import Proxy
import random
import string


class TestProxyProvider:
    def __init__(self, token: str, provider: str = "home"):
        self.token = token
        self.provider = provider
        self.proxies = self.get_proxies()

    def get_proxies(self) -> list[Proxy]:
        return [
            Proxy(
                provider=self.provider,
                username="".join(
                    random.choices(string.ascii_lowercase + string.digits, k=8)
                ),
                password="".join(
                    random.choices(
                        string.ascii_letters + string.digits + "!@#$%^&*", k=12
                    )
                ),
                host=".".join(str(random.randint(1, 254)) for _ in range(4)),
                port=random.randint(1024, 65535),
                provider_external_id=uuid.uuid4().hex,
                country_code=random.choice(
                    [
                        "US",
                        "GB",
                        "DE",
                        "FR",
                        "IT",
                        "ES",
                        "CN",
                        "JP",
                        "IN",
                        "BR",
                        "CA",
                        "AU",
                        "NL",
                        "SE",
                        "NO",
                        "FI",
                        "PL",
                        "RU",
                        "ZA",
                        "KR",
                    ]
                ),
                created_at=(datetime.now() - timedelta(days=random.randint(0, 365))),
                asn_number=(asn_number := random.randint(1000, 64511)),
                asn_name=f"AS{asn_number}_PROVIDER",
            )
            for _ in range(10)
        ]
