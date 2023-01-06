"""from src.lazy_proxy import LazyProxy

proxy = LazyProxy("http")
proxy.get_proxies("proxies.txt")
"""
import vk_api
from loguru import logger
import time
vk_sesion = vk_api.VkApi(token='vk1.a.coIOwv7FajmNWvw4TuSUgsTrH5gaLwPXXcnYwPD_pLUIY37KB7Rlk92dyjuInk0Z1X0SXzfeeJPj1OzbOudZz2mEhiHJb9mSy_jb3pM8nCZcA9F1vpFIkVAZoNH3bASSvThmFheQgusSpDw0Plsbu3UxhX5autgsGFcgA7F0aVp3gXXzwBb-PZe3h3k0bbX2g1-wso0VBtAv5X22-7FZzg')

vk = vk_sesion.get_api()

sq = vk.wall.get(owner_id=-89063613, count=1, filter='all', offset=2)

col = sq['count']
i = 0

while col >= i:

    lol = vk.wall.get(owner_id=-89063613, count=100, filter='all', offset=i)
    for sqs in lol['items']:
        i += 1
        try:
            logger.debug(sqs['id'])
            us = sqs['signer_id']

            if int(us) == 249022997:
                logger.success('НАЙДЕННО')
                print(sqs)
                time.sleep(120)
            else:
                logger.debug('Не она')
        except Exception as ex:
            logger.error(ex)
