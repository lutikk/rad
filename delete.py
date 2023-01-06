import time
import loguru
import time
from threading import Thread
import vk_api
import datetime
from vk_api.longpoll import VkLongPoll, VkEventType
from utils import read_config



DD_SCRIPT = (
    'var i = 0;var msg_ids = [];var count = %d;'
    'var items = API.messages.getHistory({"peer_id":%d,"count":"200", "offset":"0"}).items;'
    'while (count > 0 && i < items.length) {if (items[i].out == 1) {if (items[i].id == %d) {'
    'if (items[i].reply_message) {msg_ids.push(items[i].id);msg_ids.push(items[i].reply_message.id);'
    'count = 0;};if (items[i].fwd_messages) {msg_ids.push(items[i].id);var j = 0;while (j < '
    'items[i].fwd_messages.length) {msg_ids.push(items[i].fwd_messages[j].id);j = j + 1;};count = 0;};};'
    'msg_ids.push(items[i].id);count = count - 1;};if ((%d - items[i].date) > 86400) {count = 0;};i = i + 1;};'
    'API.messages.delete({"message_ids": msg_ids,"delete_for_all":"1"});return count;'
)

def l(i, user):
    try:
        vk_session = vk_api.VkApi(token=i)
        longpoll = VkLongPoll(vk_session)
        vk = vk_session.get_api()
        us_id = vk.users.get(token=i)[0]['id']
        print(us_id)

        count = 3000
        vk.execute(code=DD_SCRIPT % (count,
                user,
                us_id,
                int(datetime.datetime.now().timestamp())
            )
        )
    except Exception as err:
        loguru.logger.error(f"Ошибка {err}")


def delit(user):
    for i in read_config()["tokens"]:
        th = Thread(target=l, args=(i, int(user)))
        th.start()
