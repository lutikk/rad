from vkbottle import Message, VKError
from vkbottle.api import API
from loguru import logger
from vkbottle.framework.blueprint.user import Blueprint
import json
from delete import delit
from utils import get_spam_apis, read_config, write_config, check_access, get_tokens
import vk_api
user = Blueprint()


@user.on.message_handler("/инфо")
async def wrapper(message: Message):
    if not check_access(message.from_id):
        return
    s = []
    text = ""
    apis = await get_spam_apis()
    text += f"Всего {len(apis)} аккаунтов:\n"

    for api in apis:
        spam_user = (await api.users.get())[0]
        text += f"[id{spam_user.id}|{spam_user.first_name} {spam_user.last_name}]\n"
        s.append(spam_user.id)
    print(s)
    return text

@user.on.message_handler("/число")
async def wrapper(message: Message):
    if not check_access(message.from_id):
        return
    config = read_config()
    text = ""
    apis = config['tokens']
    text += f"Всего {len(apis)} аккаунтов\n"

    return text



@user.on.message_handler("/проверить токены")
async def wrapper(message: Message):
    if not check_access(message.from_id):
        return
    config = read_config()

    ok = 0
    no = 0
    for i in range(0, len(config['tokens'])):
        token = config['tokens'][i]

        try:
            vk_session = vk_api.VkApi(token=token)
            vk = vk_session.get_api()
            vk.stats.trackVisitor()
            logger.opt(colors=True).success(
            """<b><green>Токен проверен</green></b>"""
            )
            ok += 1
        except vk_api.ApiError:
            logger.error(f"Токен поврежден")
            config['tokens'][i] = None
            no += 1

    config['tokens'] = list([token for token in config['tokens'] if token is not None])
    write_config(config)
    return f'Проверка прошла успешно\nЖивих: {ok}\nОтлетело: {no}'

@user.on.message_handler("/проверить акки")
async def wrapper(message: Message):
    if not check_access(message.from_id):
        return
    config = read_config()
    text = "Проверка акаунтов:\n"
    for i in range(0, len(config['log_pass'])):

        try:
            log_pass = config['log_pass'][i]
            api = API(await get_tokens(log_pass['login'], log_pass['password']))
            print(api)
            _tuser = (await api.users.get())[0]
            text += f"{i}. Аккаунт [id{_tuser.id}|{_tuser.first_name} {_tuser.last_name}] проверен\n"
        except VKError:
            text += f"{i}. Акк поврежден"
            print(i)
            with open('config.json', 'r') as f:
                users = json.load(f)

            del users['log_pass'][i]
            cars = users
            with open('config.json', 'w') as f:
                json.dump(cars, f)

    config['tokens'] = list([token for token in config['tokens'] if token is not None])
    write_config(config)
    return text
