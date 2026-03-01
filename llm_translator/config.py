from mcdreforged.api.all import *


class Config(Serializable):
    first_language: str = "zh_cn"
    secondary_language: str = "en_us"
    base_url: str = "https://api.deepseek.com"
    model: str = "deepseek-chat"
    api_key: str = "enter-your-api-key"
    enable_system_prompt: bool = True
    system_prompt: str = "将以下句子{first_language}和{secondary_language}互译，翻译准确达意。注意Minecraft这款游戏中特有名词翻译正确，只返回翻译结果，不需要任何解释"
    is_proxy_to_other_servers: bool = False
    proxy_servers: list[dict] = [
        {"address": "127.0.0.1", "port": 25575, "password": ""},
        {"address": "127.0.0.1", "port": 25576, "password": ""},
    ]



config: Config = None
