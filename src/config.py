import uuid
import warnings

from enum import StrEnum
from pathlib import Path
from environs import Env
from dataclasses import dataclass

class GigaModels(StrEnum):
    GIGACHAT_LITE = 'Gigachat'
    GIGACHAT_PRO = 'GigaChat-Pro'
    GIGACHAT_MAX = 'GigaChat-Max'

class GigaScopes(StrEnum):
    PERS = 'GIGACHAT_API_PERS'
    B2B = "GIGACHAT_API_B2B"
    CORP = "GIGACHAT_API_CORP"

class GigaAPI(StrEnum):
    base_url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    chat_url = "https://gigachat.devices.sberbank.ru/api/v1/"
    embeddings_url = "https://gigachat.devices.sberbank.ru/api/v1/embeddings"

env = Env()

project_dir = Path(__file__).parent.parent
env_path = project_dir.joinpath('deployment', '.env')

if env_path.exists():
    env.read_env(path=env_path)
else:
    warnings.warn(f"Environment file not found at {env_path}. Using system Environment.")


@dataclass(frozen=True)
class GigaConfig:
    """
    Dataclass for GigaChat configuration
    """
    GIGACHAT_TOKEN: str = env.str("GIGACHAT_TOKEN")
    GIGACHAT_MODEL: GigaModels = env.str("GIGACHAT_MODEL")
    GIGACHAT_SCOPE: GigaScopes = GigaScopes.CORP

    @property
    def requests_headers(self):
        return {
            "Authorization": f"Bearer {self.GIGACHAT_TOKEN}",
            "RqUID": str(uuid.uuid4()),
            "Content-Type": "application/x-www-form-urlencoded",
        }


@dataclass(frozen=True)
class MarkdownAPIConfig:
    """
    Dataclass for MarkdownAPI.
    It isn't necessary to use this API, you can implement html_to_rst converter by yourself.
    """
    MARKDOWN_API_HOST: str | None = env.str("MARKDOWN_API_HOST", None)
    MARKDOWN_API_PORT: int | None = env.int("MARKDOWN_API_PORT", None)
    MARKDOWN_API_AUTH: str | None = env.str("MARKDOWN_API_AUTH", None)

    @property
    def auth_token(self) -> tuple:
        return "parsing", self.MARKDOWN_API_AUTH

    @property
    def convert_endpoint(self) -> str:
        return f'http://{self.MARKDOWN_API_HOST}:{self.MARKDOWN_API_PORT}/convert'


giga_config = GigaConfig()
md_api_conf = MarkdownAPIConfig()