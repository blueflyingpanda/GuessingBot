import pickle

import telebot
from PIL import Image, ImageDraw
import numpy as np
from ShapeClassifier import ShapeClassifier

token = '1855857929:AAH-r1NKWky7sM459iIdWrlI12EvUuOyHLM'
bot = telebot.TeleBot(token)
clf = ShapeClassifier()
with open('model.pkl', 'rb') as f:
    clf = pickle.load(f)

@bot.message_handler(content_types=['text', 'photo'])
def get_messages(message):
    if message.photo:
        file_id = message.photo[0].file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('tmp.jpg', 'wb') as new_file:
            new_file.write(downloaded_file)
        img = np.array(Image.open('tmp.jpg').resize((64, 64)).convert('L'))
        data = list(img.ravel().reshape(1, -1))
        Image.fromarray(img).save('temp.jpg')
        bot.send_message(message.from_user.id, "Жди...")
        answer = clf.predict(data)
        bot.send_photo(message.chat.id, "https://lh3.googleusercontent.com/proxy/rjfVkqo1LQDmWMAjcU_-UD3ev4zYRIZSce0xA48vNNLX9vkK1RJpY3wkCW6lYOrP3-tU5Qg9IR-2WY7ibNbt1We1uSPUSjxn1qxp_ZyLwpBlxnT9fCQIBze19jcI48M")
        if answer == 't':
            bot.send_message(message.from_user.id, "ТРЕУГОЛЬНИК!")
        elif answer == 'r':
            bot.send_message(message.from_user.id, "ЧЕТЫРЕХУГОЛЬНИК!")
        else:
            bot.send_message(message.from_user.id, "ЭЛЛИПС!")
    elif message.text == "/help" or message.text == "/start":
        bot.send_message(message.from_user.id, "Пришли картинку эллипса, треугольника или четырехугольника, "
                                               "а я скажу тебе что нарисовано на картинке:)")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
