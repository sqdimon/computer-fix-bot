import telebot
import config
#import main
import read
from telebot import types

"""
# RUN
bot.polling(none_stop=True)

bot = telebot.TeleBot(config.TOKEN)

read_result_json = read.read_engene('diagram.docx')
result = []
last_request = ""

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я тестовый бот ".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    no_answer = True
    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)".format(message.from_user))
        no_answer = False
    if (message.text == "❓ Задать вопрос"):
        # прочитать нулевой элемент
        main.result = read.search_engene("id0",main.read_result_json)     # result = list with dic records
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for x in range(len(main.result)):
            btn = types.KeyboardButton(main.result[x]["Name"])
            markup.add(btn)
        back_main = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back_main)
        bot.send_message(message.chat.id, text="Какая у вас проблема?", reply_markup=markup)
        no_answer = False
    if (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        no_answer = False
    if (message.text == "Вернуться Назад"):
        main.result = read.search_engene(read.search_prev_element(main.last_request, read_result_json), main.read_result_json)  # result = list with dic records
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for x in range(len(main.result)):
            btn = types.KeyboardButton(main.result[x]["Name"])
            markup.add(btn)
        back = types.KeyboardButton("Вернуться Назад")
        markup.add(back)
        back_main = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back_main)
        bot.send_message(message.chat.id, text="Какая у вас проблема?", reply_markup=markup)
        main.result = read.search_engene(main.result[x]["id"], main.read_result_json)
        return
        no_answer = False
    if (main.result != []):
        for x in range(len(main.result)):
            if (main.result[x]["Name"] == message.text):
                main.last_request = main.result[x]["id"]             # saving id for step back
                main.result = read.search_engene(main.result[x]["id"], main.read_result_json)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                for x in range(len(main.result)):
                    btn = types.KeyboardButton(main.result[x]["Name"])
                    markup.add(btn)
                back = types.KeyboardButton("Вернуться Назад")
                markup.add(back)
                back_main = types.KeyboardButton("Вернуться в главное меню")
                markup.add(back_main)
                bot.send_message(message.chat.id, text="Какая у вас проблема?", reply_markup=markup)
                no_answer = False
                break           # stop cycle when find target element - bacause we change main.result
    if (no_answer == True):
        # nothing simular
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал.. /start")
"""

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

"""
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")
"""
"""
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")
"""
"""
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
"""

#*****************************
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('Привет! 👋')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=greet_kb)

greet_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True,one_time_keyboard=False).add(button_hi)

@dp.message_handler(commands=['hi1'])
async def process_hi1_command(message: types.Message):
    await message.reply("Первое - изменяем размер клавиатуры", reply_markup=greet_kb2)

greet_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_hi)

# bot.py
@dp.message_handler(commands=['hi2'])
async def process_hi2_command(message: types.Message):
    await message.reply("Второе - прячем клавиатуру после одного нажатия", reply_markup=greet_kb2)

button1 = KeyboardButton('1️⃣')
button2 = KeyboardButton('2️⃣')
button3 = KeyboardButton('3️⃣')

markup3 = ReplyKeyboardMarkup().add(
    button1).add(button2).add(button3)

markup4 = ReplyKeyboardMarkup().row(
    button1, button2, button3
)

markup5 = ReplyKeyboardMarkup().row(
    button1, button2, button3
).add(KeyboardButton('Средний ряд'))

button4 = KeyboardButton('4️⃣')
button5 = KeyboardButton('5️⃣')
button6 = KeyboardButton('6️⃣')
markup5.row(button4, button5)
markup5.insert(button6)

@dp.message_handler(commands=['hi3'])
async def process_hi3_command(message: types.Message):
    await message.reply("Третье - добавляем больше кнопок", reply_markup=markup3)

@dp.message_handler(commands=['hi4'])
async def process_hi4_command(message: types.Message):
    await message.reply("Четвертое - расставляем кнопки в ряд", reply_markup=markup4)

@dp.message_handler(commands=['hi5'])
async def process_hi5_command(message: types.Message):
    await message.reply("Пятое - добавляем ряды кнопок", reply_markup=markup5)

markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
).add(
    KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
)

#bot.py
@dp.message_handler(commands=['hi6'])
async def process_hi6_command(message: types.Message):
    await message.reply("Шестое - запрашиваем контакт и геолокацию\nЭти две кнопки не зависят друг от друга", reply_markup=markup_request)

markup_big = ReplyKeyboardMarkup()

markup_big.add(
    button1, button2, button3, button4, button5, button6
)
markup_big.row(
    button1, button2, button3, button4, button5, button6
)

markup_big.row(button4, button2)
markup_big.add(button3, button2)
markup_big.insert(button1)
markup_big.insert(button6)
markup_big.insert(KeyboardButton('9️⃣'))

# bot.py
@dp.message_handler(commands=['hi7'])
async def process_hi7_command(message: types.Message):
    await message.reply("Седьмое - все методы вместе", reply_markup=markup_big)

@dp.message_handler(commands=['rm'])
async def process_rm_command(message: types.Message):
    await message.reply("Убираем шаблоны сообщений", reply_markup=ReplyKeyboardRemove())

inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')

@dp.message_handler(commands=['1'])
async def process_command_1(message: types.Message):
    await message.reply("Первая инлайн кнопка", reply_markup=inline_kb1)


inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)
inline_kb_full.add(InlineKeyboardButton('Вторая кнопка', callback_data='btn2'))
inline_btn_3 = InlineKeyboardButton('кнопка 3', callback_data='btn3')
inline_btn_4 = InlineKeyboardButton('кнопка 4', callback_data='btn4')
inline_btn_5 = InlineKeyboardButton('кнопка 5', callback_data='btn5')
inline_kb_full.add(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.row(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.insert(InlineKeyboardButton("query=''", switch_inline_query=''))
inline_kb_full.insert(InlineKeyboardButton("query='qwerty'", switch_inline_query='qwerty'))
inline_kb_full.insert(InlineKeyboardButton("Inline в этом же чате", switch_inline_query_current_chat='wasd'))
inline_kb_full.add(InlineKeyboardButton('Уроки aiogram', url='https://surik00.gitbooks.io/aiogram-lessons/content/'))

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 2:
        await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉', show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code}')

@dp.message_handler(commands=['2'])
async def process_command_2(message: types.Message):
    await message.reply("Отправляю все возможные кнопки", reply_markup=inline_kb_full)


help_message =  "Это урок по клавиатурам.\n"\
                "Доступные команды:\n"\
                "/start - приветствие,\n"\
                " Шаблоны клавиатур:,\n "\
                "/hi1 - авто размер,\n"\
                "/hi2 - скрыть после нажатия,\n"\
                "/hi3 - больше кнопок, \n"\
                "/hi4 - кнопки в ряд, \n"\
                "/hi5 - больше рядов, \n"\
                "/hi6 - запрос локации и номера телефона,\n"\
                "/hi7 - все методы\n"\
                "/rm - убрать шаблоны, \n"\
                "Инлайн клавиатуры:, \n"\
                "/1 - первая кнопка, \n"\
                "/2 - сразу много кнопок"



@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)



#******************************
if __name__ == '__main__':
    executor.start_polling(dp)
