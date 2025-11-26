#импортирует библиотеки
import telebot
from telebot import types
import time
from telebot import apihelper
import os
import random
from datetime import datetime
import threading


#Инициализирует бота
bot = telebot.TeleBot ('8592594669:AAHybCJ4QxI2VB1r8dA32TwwXf-1L7hSXP4')
#Приветствие и регистрация
text = "Введите команду"


@bot.message_handler(commands=['start'])
def start (message) :
    global user_id
    user_id = str (message.from_user.id)
    msg = bot.send_message(message.from_user.id, """Привет! Я бот для заметок. Со мной вы можете:\n
Создать новую заметку ✴️\nУдалить существующую заметку ❌\nНайти заметку по ключевому слову ❇️\n(Команда вводится с кнопок)""")
    x1 (message)

def x1 (message) :
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Создать заметку ✴️")
    but2 = types.KeyboardButton("️Удалить заметку ❌")
    but3 = types.KeyboardButton("Найти заметку по ключевому слову ❇️")
    markup.add(but1, but2, but3, row_width=1)
    msg = bot.send_message(message.from_user.id, text, reply_markup=markup)
    bot.register_next_step_handler (message, x)


def x (message) :
    if message.text == "/start" :
        start (message)
        return
    elif message.text == "Создать заметку ✴️" :
        new (message)
    elif message.text == "️Удалить заметку ❌" :
        delete (message)
    elif message.text == "Найти заметку по ключевому слову ❇️" :
        show (message)
    else :
        msg = bot.send_message(message.from_user.id, "⚠️ Ошибка!⚠️")
        x1 (message)

def new (message) :
    if message.text == "/start" :
        return
    remove_markup = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.from_user.id, "Введите слово доступа к записи", reply_markup=remove_markup)
    bot.register_next_step_handler (message, new2)

def new2 (message) :
    if message.text == "/start" :
        return
    global user_key
    user_key = message.text
    msg = bot.send_message(message.from_user.id, "Введите текст")
    bot.register_next_step_handler (message, new3)

def new3 (message) :
    global user_id
    user_id = str (message.from_user.id)
    if message.text == "/start" :
        return
    user_text = message.text
    with open (user_id + " " + user_key + ".txt", "w") as f :
        f.write (user_text)
        msg = bot.send_message(message.from_user.id, "Сохранено! ✅")
        x1 (message)

def delete (message) :
    if message.text == "/start" :
        return
    remove_markup = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.from_user.id, "Введите кодовое слово для удаления", reply_markup=remove_markup)
    bot.register_next_step_handler (message, delete2)
def delete2 (message) :
    global user_id
    user_id = str (message.from_user.id)
    if message.text == "/start" :
        return
    global delete_word
    delete_word = message.text
    try :
        os.remove(user_id + " " + delete_word + ".txt")
        msg = bot.send_message(message.from_user.id, "Удалено! ✅")
        x1 (message)
    except :
        msg = bot.send_message(message.from_user.id, "⚠️ У вас нет такой заметки!⚠️")
        x1 (message)
def show (message) :
    if message.text == "/start" :
        return
    remove_markup = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.from_user.id, "Введите кодовое слово", reply_markup=remove_markup)
    bot.register_next_step_handler (message, show2)

def show2 (message) :
    global user_id
    user_id = str (message.from_user.id)
    if message.text == "/start" :
        return
    user_key = message.text
    try :
        with open (user_id + " " + user_key + ".txt", "r") as f :
            text_file = f.read ()
            msg = bot.send_message(message.from_user.id, 'Читаю : "{}"'.format (text_file))
            x1 (message)
    except :
        msg = bot.send_message(message.from_user.id, "⚠️ У вас нет такой заметки!⚠️")
        x1 (message)

def check_internet_connection():
    import socket
    try:
        socket.create_connection(("api.telegram.org", 443), timeout=5)
        print("Соединение с Telegram API установлено")
        return True
    except OSError:
        print("Нет соединения с интернетом или Telegram API")
        return False

if __name__ == "__main__":
    while True:
        if check_internet_connection():
            try:
                print("Бот запущен и работает...")
                bot.polling(none_stop=True, interval=2, timeout=60)
            except Exception as e:
                print(f"Ошибка: {e}, перезапуск через 3 секунды")
                time.sleep(3)
        else:
            print("Нет интернет-соединения, проверка через 3 секунды")
            time.sleep(3)


