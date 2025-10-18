from pydantic_settings import BaseSettings, SettingsConfigDict


class TestSettings(BaseSettings):
    webshare_api_key: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
