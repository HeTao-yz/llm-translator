from mcdreforged.api.all import *
from .proxy_other_server import *
from .sign_and_book import *
from .config import Config
from .llm import *

config = None


def on_load(server: PluginServerInterface, prev_module):
    global config
    config = server.load_config_simple(target_class=Config)
    send_config()
    prefix = "t [translate-message] and !!tr <x> <y> <z> [xyz is sign or book location]"
    help_message = f"使用大模型进行{config.first_language}和{config.secondary_language}互译。玩家对话，游戏内木牌和放在讲台上的书均可翻译"
    server.register_help_message(prefix, help_message)

    builder = SimpleCommandBuilder()
    builder.command("!!tr <x> <y> <z>", send_nbt)

    builder.arg("x", Integer)
    builder.arg("y", Integer)
    builder.arg("z", Integer)

    builder.register(server)


def send_config():
    from . import llm

    llm.config = config
    from . import proxy_other_server

    proxy_other_server.config = config
    from . import sign_and_book

    sign_and_book.config = config


def send_nbt(source: InfoCommandSource, dic: dict):
    server = source.get_server()
    server.execute(f"data get block {dic['x']} {dic['y']} {dic['z']}")


def on_user_info(server: ServerInterface, info: Info):
    if info.content.startswith("t "):
        translator_messages = LLM.use(info.content[2:])
        server.say(f"§7[T]<{info.player}> " + f"§f{translator_messages}")
        if config.is_proxy_to_other_servers:
            proxy_message(info.player, translator_messages)


def on_info(server: PluginServerInterface, info: Info):
    if "has the following block data:" in info.content and len(info.content) > 80:
        if not info.is_player:
            nbt = info.content
            get_messages_and_translate(nbt)
    if (
        "The target block is not a block entity" in info.content
        and len(info.content) < 40
    ):
        if not info.is_player:
            server.say("§7Unsupported block. Please choose a sign or book.")
