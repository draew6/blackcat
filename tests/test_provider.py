from blackcat.proxy.providers.webshare import WebShareProvider
from tests.settings import TestSettings


def test_webshare_provider():
    settings = TestSettings()
    provider = WebShareProvider(settings.webshare_api_key)
    assert len(provider.proxies) > 0
    print(f"Fetched {len(provider.proxies)} proxies from WebShare")