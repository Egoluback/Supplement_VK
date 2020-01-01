import requests, json, vk_api, random, pprint, io, math

from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from StoryGenerator import StoryGenerator

# url = 'https://models.dobro.ai/gpt2_poetry/'
url = 'https://models.dobro.ai/gpt2/medium/'
TOKEN = '47bbb34e7a81b4d1ce62dd3a4e6fbfdc9e29c6c7d6dac8a0a09b61bb3a70a4c68ae3afd50d98446f7d6ae'
PUBLIC_ID = 190299951

def get_sample(text):
    response = requests.post(url, json={"prompt": text, "length": 50})
    return json.loads(response.text)["replies"][0]

vk_session = vk_api.VkApi(token=TOKEN)
vk_session._auth_token()

vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, PUBLIC_ID)

print("Bot has been launched.")

while True:
    # try:
    
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
                    if (event.object.text == "@g_onyourown"):
                        storyGenerator = StoryGenerator("", "g_onyourown", 1)
                        story = storyGenerator.Generate()

                        vk.messages.send(user_id = event.object.from_id, message = story, random_id = get_random_id())
                    else:
                        countIter = int(event.object.text.split("@")[0])
                        text = event.object.text.split("@")[1]
                        storyGenerator = StoryGenerator(text, "default", countIter)
                        story = storyGenerator.Generate()
                        try:
                            vk.messages.send(user_id = event.object.from_id, message = story, random_id = get_random_id())
                        except vk_api.exceptions.ApiError:
                            border = 4096
                            for i in range(math.ceil(len(story) / border)):
                                vk.messages.send(user_id = event.object.from_id, message = story[i * border : (i + 1) * border], random_id = get_random_id())
    # except:
    #     print("I've got an exception... keep working.")