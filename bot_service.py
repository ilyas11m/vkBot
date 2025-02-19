import vk_api

from config.config import Config
from vk_api.longpoll import VkLongPoll, VkEventType, VkMessageFlag

vk_session = vk_api.VkApi(token=Config.TOKEN)
vk = vk_session.get_api()
long_poll = VkLongPoll(vk_session)

def sender(user_id, text):
    vk.messages.send(user_id=user_id, message=text, random_id=0)
def send_photo(id, url):
    vk.messages.send(user_id=id, attachment=url, random_id=0)

for event in long_poll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            if msg == "photo":
                send_photo(id, "photo351786545_457262754%2Fmail351786545-291")

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            if msg == "start":
                sender(id, "Привет! Этот бот создан для публикации твоих фотографий в нашей группе :)")