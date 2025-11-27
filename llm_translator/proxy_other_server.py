from mcdreforged.api.all import *

config = None


def proxy_message(player, message):
    for proxy_server in config.proxy_servers:
        proxy(
            proxy_server["address"],
            proxy_server["port"],
            proxy_server["password"],
            player,
            message,
        )


def proxy(address, port, password, player, message):
    command = f'/tellraw @a [{{"text":"[T]<{player}> ","color":"gray"}},{{"text":"{message}","color":"white"}}]'
    rcon = RconConnection(address, port, password)
    try:
        if rcon.connect():
            rcon.send_command(command)
            rcon.disconnect()
    except:
        ServerInterface.get_instance().logger.error(
            f"[llm-translator] Failed to connect to the port: {port}"
        )
