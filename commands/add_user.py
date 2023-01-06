from typing import Optional

from vkbottle import Message
from vkbottle.framework.blueprint.user import Blueprint
from vkbottle.framework.framework.rule import FromMe
import requests
from utils import read_config, write_config, check_access

user = Blueprint()


@user.on.message_handler("/добавить акк <login>:<password>")
async def add_account(message: Message, login: str, password: str) -> Optional[str]:
    if not check_access(message.from_id):
        return
    try:
        vk_outh = "https://oauth.vk.com/token?grant_type=password&"
        cliend_and_secret = "client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH"
        get_token = requests.get(f"{vk_outh}{cliend_and_secret}&username={login}&password={password}")
        token = str(get_token.json()["access_token"])
        config = read_config()
        config['tokens'].append(token)
        write_config(config)
        return "Логин и пароль добавлен"
    except:
        return "Неверный логин или пароль"


@user.on.message_handler("/добавить токен <token>")
async def add_token(message: Message, token: str) -> Optional[str]:
    if not check_access(message.from_id):
        return
    config = read_config()
    config['tokens'].append(token)
    write_config(config)
    return "Токен добавлен"
