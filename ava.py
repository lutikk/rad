import time
import loguru
import os, random
from threading import Thread
import vk_api
import datetime
from vk_api.longpoll import VkLongPoll, VkEventType
from utils import read_config

def pfoto():
    lyl_2 = os.getcwd()
    lyl = f"{lyl_2}/ava"
    see = os.listdir(path=str(lyl))
    colvo = len(see)
    s = random.randint(1, colvo)
    print(f'{lyl}/{see[s - 1]}')
    return f'{lyl}/{see[s - 1]}'


def l(i):
    try:
        vk_session = vk_api.VkApi(token=i)
        longpoll = VkLongPoll(vk_session)
        vk = vk_session.get_api()
        upload = vk_api.VkUpload(vk_session)

        photo = upload.photo_profile(photo=pfoto())

    except Exception as err:
        loguru.logger.error(f"Ошибка {err}")


def delit():
    for i in read_config()["tokens"]:
        th = Thread(target=l, args=(i,))
        th.start()

delit()