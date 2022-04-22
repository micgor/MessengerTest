from flask import Flask, request, render_template
from datetime import datetime
import json

application = Flask(__name__)  # Создаем Flask-приложение
DB_FILE = "./data/db.json"


# Чтение сообщений из файла
def load_messages():
    json_file = open(DB_FILE, "r") # открываем для чтения
    data = json.load(json_file)
    return data["messages"]


all_messages = load_messages() # список всех сообщений


# Сохранение сообщений в файл
def save_messages():
    data = {
        "messages": all_messages
    }
    json_file = open(DB_FILE, "w") # открываем  для записи
    json.dump(data, json_file)


@application.route("/chat")
def display_chat():
    return render_template("form.html")  # Показываем файл из папки templates


@application.route("/")
def index_page():
    return "Hello, welcome to Skillbox Chat"


@application.route("/get_messages")
def get_messages():
    return {"messages": all_messages}


@application.route("/send_message")
def send_message():
    # Получаем информацию от пользователя
    sender = request.args["name"]
    text = request.args["text"]

    # Добавляем сообщение в список
    add_message(sender, text)

    save_messages()
    return "OK"


def add_message(sender, text):
    # Узнаем длину имени пользователя и сообщения
    # lsender = len(sender)
    # ltext = len(text)

    # Проверяем длину имени пользователя и сообщения
    # if lsender < 3 or lsender > 100:
    #    print('ERROR: Name must be in range [3...100]')
    #elif ltext < 1 or ltext > 3000:
        #print('ERROR: Text must be in range [1...3000]')
    #else:
    # 1. Подготовить словарь с данными сообщения
    new_message = {
        "sender": sender,
        "text": text,
        "time": datetime.now().strftime("%H:%M:%S"),
    }
    # 2. Добавить получившийся словарь в список всех сообщений
    all_messages.append(new_message)


def print_message(mess):
    print(f"[{mess['sender']}]: {mess['text']} / {mess['time']}")


application.run(host='0.0.0.0', port=80)  # Запускаем приложение

#  ДЗ:
#  Предусмотреть ограничения для имени и текста (валидация данных) в фунции add_message

#  День 3:
#  Подгтовить код к размещению на хостинге
#  Настроить хостинг и запустить там чат
#  Сохранение сообщений в файл
