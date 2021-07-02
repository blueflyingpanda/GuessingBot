import telebot
from telebot import types
from PIL import Image
import numpy as np
import os

from keras.models import load_model

global duplicates
global answer
global img

new_data_path = 'new_data/'
token = '1855857929:AAH-r1NKWky7sM459iIdWrlI12EvUuOyHLM'
bot = telebot.TeleBot(token)

model = load_model('drawing_classification.h5')


def ask_wrong_or_right(message):
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
    keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Я угадал? \U0001F605'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global duplicates
    if call.data == "yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
        if not duplicates:
            bot.send_message(call.message.chat.id, 'Ура \U0001F60E')
    elif call.data == "no":
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        global answer
        if not duplicates:
            if answer[0] == 'c':
                key_t = types.InlineKeyboardButton(text='Треугольник', callback_data='t')
                keyboard.add(key_t)  # добавляем кнопку в клавиатуру
                key_r = types.InlineKeyboardButton(text='Четырехугольник', callback_data='r')
                keyboard.add(key_r)
            elif answer[0] == 't':
                key_e = types.InlineKeyboardButton(text='Эллипс', callback_data='e')
                keyboard.add(key_e)
                key_r = types.InlineKeyboardButton(text='Четырехугольник', callback_data='r')
                keyboard.add(key_r)
            else:
                key_e = types.InlineKeyboardButton(text='Эллипс', callback_data='e')
                keyboard.add(key_e)
                key_t = types.InlineKeyboardButton(text='Треугольник', callback_data='t')
                keyboard.add(key_t)  # добавляем кнопку в клавиатуру
            bot.send_message(call.message.chat.id, 'Печалька \U0001F614\nА что было изображено на картинке?',
                             reply_markup=keyboard)
    elif call.data == 'e':
        if not duplicates:
            duplicates = True
            bot.send_message(call.message.chat.id,
                             'Эллипс значит \U0001F611\nНу ладно, пойду дальше учиться.\nСпасибо!')
            with open('e.txt', 'r+') as current:
                try:
                    new_data = int(current.read())
                except:
                    new_data = 0
                current.seek(0)
                current.write(str(new_data + 1))
                current.truncate()
            Image.fromarray(img).save(new_data_path + 'circles/e' + str(new_data) + '.png')
    elif call.data == 't':
        if not duplicates:
            duplicates = True
            bot.send_message(call.message.chat.id, 'Трехугольник значит \U0001F611\nНу ладно, пойду дальше '
                                                   'учиться.\nСпасибо!')
            with open('t.txt', 'r+') as current:
                try:
                    new_data = int(current.read())
                except:
                    new_data = 0
                current.seek(0)
                current.write(str(new_data + 1))
                current.truncate()
            Image.fromarray(img).save(new_data_path + 'triangles/t' + str(new_data) + '.png')
    elif call.data == 'r':
        if not duplicates:
            duplicates = True
            bot.send_message(call.message.chat.id, 'Четырехугольник значит \U0001F611\nНу ладно, пойду дальше '
                                                   'учиться.\nСпасибо!')
            with open('r.txt', 'r+') as current:
                try:
                    new_data = int(current.read())
                except:
                    new_data = 0
                current.seek(0)
                current.write(str(new_data + 1))
                current.truncate()
            Image.fromarray(img).save(new_data_path + 'rectangles/r' + str(new_data) + '.png')


label = {0: "circle", 1: "rectangle", 2: "triangle"}


def predict(file_name):
    image = Image.open(file_name).resize((28, 28))
    image = np.reshape(image, [1, 28, 28, 3])
    image = image / 255
    classes = np.argmax(model.predict(image)[0])
    category = label[classes]
    return category


def report_prediction(file_name):
    def to_percent(x):
        if x * 100 > 99:
            return '>99'
        elif x * 100 < 1:
            return '<1'
        else:
            return str(round(x * 100))
    image = Image.open(file_name).resize((28, 28))
    image = np.reshape(image, [1, 28, 28, 3])
    image = image / 255
    proba = model.predict(image)[0]
    report = ("Эллипс: " + to_percent(proba[0]) + '%' + '\n' +
              "Четырехугольник: " + to_percent(proba[1]) + '%' + '\n' +
              "Треугольник: " + to_percent(proba[2]) + '%')
    return report


@bot.message_handler(content_types=['text', 'photo'])
def get_messages(message):
    if message.photo:
        bot.send_message(message.from_user.id, "Жди...\U0001F9D0")
        global duplicates
        duplicates = False
        file_id = message.photo[0].file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('tmp.png', 'wb') as new_file:
            new_file.write(downloaded_file)
        global img
        img = np.array(Image.open('tmp.png').resize((28, 28)))
        global answer
        answer = predict('tmp.png')
        bot.send_photo(message.chat.id,
                       "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1TzH_qrobukWbEXQIht3j5OyM06yH9PHSSg&usqp=CAU")
        msg_answer = {"circle": "ЭЛЛИПС! \U0001F534",
                      "rectangle": "ЧЕТЫРЕХУГОЛЬНИК! \U0001F7E5",
                      "triangle": "ТРЕУГОЛЬНИК! \U0001F53A"}
        bot.send_message(message.from_user.id, msg_answer[answer])
        bot.send_message(message.from_user.id, report_prediction('tmp.png'))
        os.remove('tmp.png')
        # bot.register_next_step_handler(message, ask_wrong_or_right)
        ask_wrong_or_right(message)
    elif message.text == "/help" or message.text == "/start":
        bot.send_message(message.from_user.id,
                         "Привет " + str(message.from_user.username) + "! Пришли картинку эллипса,"
                                                                       " треугольника или четырехугольника, "
                                                                       "а я скажу тебе что нарисовано на картинке "
                                                                       "\U0001F609")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю \U0001F643\nНапиши /help.")


bot.polling(none_stop=True, interval=0)
