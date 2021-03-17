import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
from random import randint

vk_sess = vk_api.VkApi(token="8a07dc2550ebf5edbf4446ee1d178c8f9cbf702e81bea8fa672826b957051fe91828bbd0a95deb9e51d62")
vk = vk_sess.get_api()
longpoll = VkLongPoll(vk_sess)


def sender(id, text):
    vk_sess.method('messages.send', {'user_id': id, 'message': text, 'random_id': randint(1, 1000000000)})


def edit(text, event):
    vk_sess.method('messages.edit', {'conversation_message_id': event.message_id, 'message': text, "peer_id": event.peer_id})


def top_likes(msg, event):
    slash = msg.rfind("/")
    msg = msg[slash + 1:]
    try:
        js = requests.get(
            f"""https://api.vk.com/method/wall.get?domain={msg}&access_token=a0375038a0375038a037503848a041ba19aa037a0375038c067ae78c738000389cf1a75&v=5.52""").json()
        count = js["response"]["count"]
        popyt = min(count // 100, 50)
        offset = 0
        count_z = 100
        if popyt == 0:
            count_z = count
            popyt = 1
        top = []
        mtop = 0
        procent = 100 // popyt
        procent_ = 0
        text = "Загрузка"
        sender(event.user_id, text)
        for i in range(popyt):

            params = {'domain': msg,
                      'offset': offset,
                      'count': count_z,
                      'access_token': 'a0375038a0375038a037503848a041ba19aa037a0375038c067ae78c738000389cf1a75',
                      'v': 5.52}
            offset += 100
            response = requests.get("https://api.vk.com/method/wall.get", params=params).json()
            for g in range(100):
                likes = response["response"]["items"][g]["likes"]["count"]
                if likes > mtop:
                    top.append([likes, response["response"]["items"][g]["text"]])
                    top.sort(reverse=True)
                    if len(top) <= 5:
                        mtop = 0
                    else:
                        mtop = top[4][0]
                        del top[5]
            if i % 3 == 0:
                procent_ += min(procent * 3, 100)
                text = "Загрузка " + str(procent_) + "%"
                edit(text, event)
        st = ""
        for i in range(len(top)):
            st += top[i][1] + "\n Лайков: " + str(top[i][0]) + "\n__________________________\n\n"
        edit("Загрузка 100%", event)
        return st
    except KeyError:
        return "Error"




for event in longpoll.listen():
    print(event.type)

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if "/" in event.text and event.text[:3].lower() == "топ":
                msg = event.text.lower()
                st = top_likes(msg, event)
                sender(event.user_id, st)





