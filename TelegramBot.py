import telebot
from PIL import Image, ImageDraw
import numpy as np

token = '1855857929:AAH-r1NKWky7sM459iIdWrlI12EvUuOyHLM'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text', 'photo'])
def get_messages(message):
    if message.photo:
        file_id = message.photo[2].file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('tmp.jpg', 'wb') as new_file:
            new_file.write(downloaded_file)
        img = np.array(Image.open('tmp.jpg').resize((64, 64)).convert('L'))
        Image.fromarray(img).save('temp.jpg')
        bot.send_message(message.from_user.id, "Жди...")  # обработать фото
    elif message.text == "/help" or message.text == "/start":
        bot.send_message(message.from_user.id, "Пришли картинку элипса, треугольника или четырехугольника, "
                                               "а я скажу тебе что нарисовано на картинке:)")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)


def image_to_array():
    pass
