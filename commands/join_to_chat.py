from utils import *
import asyncio
import time
from vkbottle.api import API

from typing import Optional
from frends import NewFollowersGenerator
from vkbottle import Message, VKError
from vkbottle.framework.blueprint.user import Blueprint
from loguru import logger
from spammer import spammer
from utils import get_spam_apis, check_access
from delete import delit

user = Blueprint()

loop = asyncio.get_event_loop()

CHAT_SPAM_STATE = {'working': False}


def get_state():
    return CHAT_SPAM_STATE


@user.on.message_handler('/гпост <text>')
async def wrapper(message: Message, text: str) -> Optional[str]:
    if not check_access(message.from_id):
        return
    for api in await get_spam_apis():
        try:
            await api.wall.post(message=text, owner_id=-976808)
            logger.opt(colors=True).success(
                """<b><green>Создал пост</green></b>"""
            )
        except Exception as err:
            logger.error(f"Ошибка {err}")
    return f"Создал пост с текстом {text}"

@user.on.message_handler('/пост <text>')
async def wrapper(message: Message, text: str) -> Optional[str]:
    if not check_access(message.from_id):
        return
    for api in await get_spam_apis():
        try:
            await api.wall.post(message=text)
            logger.opt(colors=True).success(
                """<b><green>Создал пост</green></b>"""
            )
        except Exception as err:
            logger.error(f"Ошибка {err}")
    return f"Создал пост с текстом {text}"

@user.on.message_handler('/дел [id<user_id:int>|<user_name>]')
async def wrapper(message: Message, user_id: int, **kwargs) -> Optional[str]:
    if not check_access(message.from_id):
        return
    target_user = (await message.api.users.get(user_ids=user_id))[0]
    delit(user=target_user.id)
    return f"Удалил сообщения" \
           f"[id{target_user.id}|{target_user.first_name} {target_user.last_name}]"


@user.on.message_handler('/репорт [id<user_id:int>|<user_name>]')
async def wrapper(message: Message, user_id: int, **kwargs) -> Optional[str]:
    if not check_access(message.from_id):
        return
    target_user = (await message.api.users.get(user_ids=user_id))[0]
    for api in await get_spam_apis():
        try:
            await api.users.report(user_id=target_user.id, type="insult", comment="Агрессивная просто с ума сойти пыталась снести чат через бота")
            logger.opt(colors=True).success(
                """<b><green>Создал репорт</green></b>"""
            )
        except Exception as err:
            logger.error(f"Ошибка {err}")
    return f"Отправил репорты " \
           f"[id{target_user.id}|{target_user.first_name} {target_user.last_name}]"

@user.on.message_handler('/репорт пост https://vk.com/wall-<id_gp>_<id_p>')
async def wrapper(message: Message, id_gp: int, id_p: int) -> Optional[str]:
    if not check_access(message.from_id):
        return

    for api in await get_spam_apis():
        try:
            await api.wall.report_post(owner_id=id_gp, post_id=id_p, reason=4)
            logger.opt(colors=True).success(
                """<b><green>Создал репорт</green></b>"""
            )
        except Exception as err:
            logger.error(f"Ошибка {err}")
    return f"Отправил репорты на пост"


@user.on.message_handler('/статус <text>')
async def wrapper(message: Message, text: str) -> Optional[str]:
    if not check_access(message.from_id):
        return
    for api in await get_spam_apis():
        try:
            await api.status.set(text)
            logger.opt(colors=True).success(
                """<b><green>Поставил статус</green></b>"""
            )
        except Exception as err:
            logger.error(f"Ошибка {err}")
    return f"Поставил ботам статус {text}"


@user.on.message_handler('/валентинки')
async def wrapper(message: Message):
    if not message.from_id in [166270092, 645697619]:
        return
    logger.opt(colors=True).success(
        """<b><green>начнем ебать</green></b>"""
    )
    ss = 0
    for api in await get_spam_apis():
        ss += 1
        try:
            text = "Смастерить валентинки"
            await api.messages.send(peer_id=-174105461, random_id=0, message=text)
            logger.opt(colors=True).success(
                """<b><green>написал сообщение</green></b>"""
            )
            i = 0
            if ss <= 30:
                while i <= 12:
                    text = "подарить валентинку @tboch "
                    await api.messages.send(peer_id=-174105461, random_id=0, message=text)
                    logger.opt(colors=True).success(
                        """<b><green>написал сообщение</green></b>"""
                    )
                    time.sleep(2.5)
                    i += 1
            else:
                while i <= 12:
                    text = "подарить валентинку @black_dead_in_your_head "
                    await api.messages.send(peer_id=-174105461, random_id=0, message=text)
                    logger.opt(colors=True).success(
                        """<b><green>написал сообщение</green></b>"""
                    )
                    time.sleep(2.5)
                    i += 1

        except VKError as ex:

            if ex.error_code == 902:
                logger.error(f"<red>{await api.user_id}</red> | Пидарас закрыл ЛС")
            elif ex.error_code == 9:
                logger.error(f"<red>{await api.user_id}</red> | Спим немного")
                await asyncio.sleep(10)
            elif ex.error_code == 5:
                logger.error(f"<red>{await api.user_id}</red> | Акк отлетел")
            else:
                logger.error(f"<red>{await api.user_id}</red> | неизвестная ошибка {ex.error_code}")

    return f"Сделано!"


@user.on.message_handler('/с [id<user_id:int>|<user_name>] <text>')
async def wrapper(message: Message, user_id: int, text: str, **kwargs) -> Optional[str]:
    if not check_access(message.from_id):
        return
    target_user = (await message.api.users.get(user_ids=user_id))[0]


    for api in await get_spam_apis():
        try:
            await api.messages.send(peer_id=target_user.id, random_id=0, message=text)
            logger.opt(colors=True).success(
                """<b><green>написал сообщение</green></b>"""
            )
        except VKError as ex:

            if ex.error_code == 902:
                logger.error(f"<red>{await api.user_id}</red> | Пидарас закрыл ЛС")
            elif ex.error_code == 9:
                logger.error(f"<red>{await api.user_id}</red> | Спим немного")
                await asyncio.sleep(10)
            elif ex.error_code == 5:
                logger.error(f"<red>{await api.user_id}</red> | Акк отлетел")
            else:
                logger.error(f"<red>{await api.user_id}</red> | неизвестная ошибка {ex.error_code}")

    return f"Сделано!"

@user.on.message_handler('/беседа старт спам <link> <text>')
async def wrapper(message: Message, link: str, text: str) -> Optional[str]:
    if not check_access(message.from_id):
        return
    spam_database = []

    CHAT_SPAM_STATE.update({'working': True})
    for api in await get_spam_apis():
        try:
            spam_database.append((api, (await api.messages.join_chat_by_invite_link(link=link)).chat_id + 2e9,))
            
        except VKError:
            pass

    for account_info in spam_database:


        loop.create_task(spammer(account_info[0], account_info[1], text, lambda: get_state()))


    return "Расчет придурков окончен"


@user.on.message_handler('++др')
async def wrapper(message: Message):
    config = read_config()
    token = config['admin_token']
    api = API(token)
    api.error_handler = ErrorHandler()
    api.error_handler.add_error_handler(6, rps_error_handler)
    api.error_handler.captcha_handler(solve_captcha)


    async for follower in NewFollowersGenerator(api):

        try:
            user = (await api.users.get(user_ids=follower))[0]
            await api.friends.add(user_id=user.id)
            logger.opt(colors=True).success(
            """<b><green>Принял заявку</green></b>"""
            )
        except Exception as err:
            logger.error(f"Ошибка {err}")
    return "Принял заявки"

@user.on.message_handler('/беседа стоп спам')
async def wrapper(message: Message):
    if not check_access(message.from_id):
        return
    CHAT_SPAM_STATE.update({'working': False})
