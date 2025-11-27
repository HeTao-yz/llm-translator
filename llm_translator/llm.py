from mcdreforged.api.all import *
from openai import OpenAI

config = None


class LLM:
    @staticmethod
    def get_client():
        client = OpenAI(api_key=config.api_key, base_url=config.base_url)
        return client

    @staticmethod
    def use(message):
        try:
            response = LLM.get_client().chat.completions.create(
                model=config.model,
                messages=[
                    {
                        "role": "system",
                        "content": f"将以下句子{config.first_language}和{config.secondary_language}互译，翻译准确达意。注意Minecraft这款游戏中特有名词翻译正确，只返回翻译结果，不需要任何解释",
                    },
                    {"role": "user", "content": message},
                ],
                stream=False,
            )
            return response.choices[0].message.content
        except Exception as e:
            return e
