import telebot
import config
import random
import csv
from array import *
from telebot import types



# import question


"""
# BOT
bot = telebot.TeleBot(config.TOKEN)

# KEYBOARD MAIN
#markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
items = []
with open("q.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:
        items.append(types.KeyboardButton(row["question"]))
markup.add(*items)
csvfile.close()



def welcome(message):
    sti = open('static/cat1.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)


    bot.send_message(message.chat.id, "Бобро пожаловать, {0.first_name}!\nЯ -  <b>{1.first_name}</b>, бот созданный ... ".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):

    with open("q.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            if message.chat.type == 'private':
                if message.text == 'Рандомное число':
                    bot.send_message(message.chat.id, str(random.randint(0,100)))
                elif message.text == row["question"]:
                    bot.send_message(message.chat.id, row["answer"])
                    print(message.chat.first_name,'->',message.text, '->', row["question"], '|', row["answer"])
                else:
                    bot.send_message(message.chat.id, 'ХЗ чо ответить (не сцы)',
                                     parse_mode='html', reply_markup=markup)

def lalala2(message):
    if message.text == "q":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        items = []
        items.append(types.KeyboardButton("question"))
        markup.add(*items)

csvfile.close()
"""


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])

def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
    elif (message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "У меня нет имени..")

    elif message.text == "Что я могу?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться2 в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Поздороваться с читателями", reply_markup=markup)

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


# RUN
bot.polling(none_stop=True)


















