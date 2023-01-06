from datetime import datetime
import random
from loguru import logger
import vk_api
import requests as req
import json, requests
from utils import read_config, write_config, check_access
from const import DEFAULT_CONFIG, APPS


def nev_pass():
    passw = ''
    ss = random.randint(8, 15)
    i = 0
    qq = ['d', 's', 'f', 'e', 'g', 'z', 'x', 'c', 'v', 'b', 'bn', 'df', 'qw', 'fg', 'hj']
    while i < ss:
        ll = random.randint(1, len(qq))
        passw += qq[ll-1]
        i += 1
    return passw


name = f"{datetime.now().strftime('%m-%d-%Y')}.{random.randint(1, 4096)}"
data = str()
tokens = str()



def _auth(login, password):
    try:
        vk_outh = "https://oauth.vk.com/token?"
        vk_outh += "grant_type=password"
        params = {
            "client_id" : "2274003",
            "client_secret" : "hHbZxrka2uZ6jB1inYsH",
            "username" : login,
            "password" : password,
            "scope": "notify,friends,photos,audio,video,stories,pages,status,notes,messages,wall,ads,offline,docs,groups,notifications,stats,email,market, stories, photos, app_widget, messages, docs, manage"
        }

        token = req.get(vk_outh, params=params).json()["access_token"]
        print(token)
        return token

    except:
        print("Нет")


with open('pass.txt', 'r', encoding='utf-8') as f:
    for line in f:
        try:

            login, password, tok = tuple(line.strip().split(":"))

            config = read_config()
            config['tokens'].append()
            write_config(config)

            logger.info("Установил токен")
        except Exception as err:
            logger.error(f"Ошибка {err}")



f = open(f'{name}.txt', 'wt', encoding='utf-8')
f.write(data)
f.close()

