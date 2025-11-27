from mcdreforged.api.all import *


class Config(Serializable):
    first_language: str = "zh_cn"
    secondary_language: str = "en_us"
    base_url: str = "https://api.deepseek.com"
    model: str = "deepseek-chat"
    api_key: str = "enter-your-api-key"
    is_proxy_to_other_servers: bool = False
    proxy_servers: list[dict] = [
        {"address": "127.0.0.1", "port": 25575, "password": ""},
        {"address": "127.0.0.1", "port": 25576, "password": ""},
    ]


config: Config = None
