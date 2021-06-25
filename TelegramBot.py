import telebot
from PIL import Image, ImageDraw
import numpy as np

bot = telebot.TeleBot('1855857929:AAH-r1NKWky7sM459iIdWrlI12EvUuOyHLM')


@bot.message_handler(content_types=['text', 'photo'])
def get_messages(message):
    if message.photo:
        print(message.photo)
        # file = message.photo.get_file()
        # file.download()
        bot.send_message(message.from_user.id, "Жди...")  # обработать фото
    elif message.text == "/help" or message.text == "/start":
        bot.send_message(message.from_user.id, "Пришли картинку элипса, треугольника или четырехугольника, "
                                               "а я скажу тебе что нарисовано на картинке:)")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)


def image_to_array():
    pass
