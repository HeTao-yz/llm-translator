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
            if config.enable_system_prompt:
                system_content = config.system_prompt.format(
                    first_language=config.first_language,
                    secondary_language=config.secondary_language
                )
                response = LLM.get_client().chat.completions.create(
                    model=config.model,
                    messages=[
                        {"role": "system","content": system_content},
                        {"role": "user", "content": message},
                    ],
                    stream=False,
                )
            else:
                response = LLM.get_client().chat.completions.create(
                    model=config.model,
                    messages=[
                        {"role": "user", "content": message}
                    ],
                    stream=False,
                )
            return response.choices[0].message.content
        except Exception as e:
            return e
