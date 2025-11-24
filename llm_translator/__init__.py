import os
from typing import Optional
from mcdreforged.api.all import *
from openai import OpenAI

class Config(Serializable):
    first_language: str = 'zh_cn'
    secondary_language: str = 'en_us'
    base_url: str = "https://api.deepseek.com"
    model: str = 'deepseek-chat'
    api_key: str = '请在此处填写API'

config: Optional[Config] = None

def on_load(server: PluginServerInterface,prev_module):
    global config
    config = server.load_config_simple(target_class=Config)
    prefix = 't [translate-message]'
    help_message = f'前缀t与空格,后接信息以使用大语言模型进行{config.first_language}和{config.secondary_language}互译。'
    server.register_help_message(prefix, help_message)

class LLM:
    @staticmethod
    def get_client():
        client = OpenAI(
            api_key=config.api_key,
            base_url=config.base_url
        )
        return client

    @staticmethod
    def use(message):
        response = LLM.get_client().chat.completions.create(
            model=config.model,
            messages=[
                {"role": "system", "content": f"请将以下句子进行{config.first_language}和{config.secondary_language}互译，翻译需要准确达意正确，不产生歧义。同时请注意在Minecraft这款游戏中的特有名词翻译正确，只返回翻译结果，不需要任何解释"},
                {"role": "user", "content": message},
            ],
            stream=False
        )
        return response.choices[0].message.content

def translator_message(message):
    try:
        return LLM.use(message)
    except Exception as e:
        return f'ERROR: {str(e)}'

def on_user_info(server: ServerInterface, info: Info):
    if info.content.startswith('t '):
        server.say(f'§7[T]<{info.player}> '+f'§f{translator_message(info.content[2:])}')




 