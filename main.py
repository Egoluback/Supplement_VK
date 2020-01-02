import requests, json, vk_api, random, pprint, io, math

from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from const import *
from StoryGenerator import StoryGenerator

vk_session = vk_api.VkApi(token=TOKEN)
vk_session._auth_token()

vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, PUBLIC_ID)

print("Bot has been launched.")

while True:
    try:
        for event in longpoll.listen():
            print("there is new event - " + str(event.type))
            if (event.type == VkBotEventType.MESSAGE_NEW):
                if (event.object.text):
                    print(str(event.object.from_id) + " - " + event.object.text)
                    if (event.from_chat):
                        print("new message")
                        isSend = random.randint(1, 10)
                        print(isSend)
                        if (isSend == 1):
                            toSend = event.object.text + get_sample(event.object.text)
                            print(toSend)
                            vk.messages.send(chat_id = event.chat_id, message = toSend, random_id = get_random_id())
                    else:
                        if ("@g_onyourown" in event.object.text):
                            countIter = 1

                            if (len(event.object.text.split(" ")) == 1):
                                countIter = random.randint(1, 3)
                            else:
                                countIter = int(event.object.text.split(" ")[1])

                            storyGenerator = StoryGenerator("", "g_onyourown", countIter)
                            story = storyGenerator.Generate()

                            vk.messages.send(user_id = event.object.from_id, message = story, random_id = get_random_id())
                        else:
                            textSplit_arr = event.object.text.split("@")
                            if (len(textSplit_arr) == 1):
                                countIter = 1
                                text = event.object.text
                            else:
                                countIter = int(textSplit_arr[0])
                                text = textSplit_arr[1]

                            storyGenerator = StoryGenerator(text, "default", countIter)
                            story = storyGenerator.Generate()
                            try:
                                vk.messages.send(user_id = event.object.from_id, message = story, random_id = get_random_id())
                            except vk_api.exceptions.ApiError:
                                border = 4096
                                for i in range(math.ceil(len(story) / border)):
                                    vk.messages.send(user_id = event.object.from_id, message = story[i * border : (i + 1) * border], random_id = get_random_id())
    except:
        print("I've got an exception... keep working.")