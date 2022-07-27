from telebot import TeleBot
from replit import db
# from PIL import Image
# import request

app = TeleBot(__name__)


@app.route('/command ?(.*)')
def example_command(message, cmd):
    chat_dest = message['chat']['id']
    msg = "Command Recieved: {}".format(cmd)

    app.send_message(chat_dest, msg)


@app.route('(?!/).+')
def parrot(message):
    chat_dest = message['chat']['id']
    user_msg = message['text']
    msg = "Parrot Says: {}".format(user_msg)
    app.send_message(chat_dest, msg)


@app.route('/dudos')
def dudos_example(message):
    chat_dest = message['chat']['id']

    for i in range(5):
        if (i < 100):
            msg = "Загрузка: 0," + str(i)
        else:
            msg = "Загрузка: 1," + str(i)
        app.send_message(chat_dest, msg)


@app.route('/helpreg')
def reges(message):
    chat_dest = message['chat']['id']
    msg = "Чтобы зарегестрировать себя в системе нужно ввести пароль, логин присваивается автоматически"
    app.send_message(chat_dest, msg)


@app.route('/reg')
def reges_full(message):
    chat_dest = message['chat']['id']
    db[int(chat_dest)] = message
    msg = "Вы зарегестрированы"
    app.send_message(chat_dest, msg)


@app.route('/sdfsdfadasf')
def check_reg(message):
    chat_dest = message['chat']['id']
    app.send_message()
    app.send_sticker()


# @app.route('/sticker')
# def check_stiker(message):
#         chat_dest = message['chat']['id']
# @app.route(content_types = ["photo"])
# def photo(message):
#         idphoto = message.photo[0].file_id
#         app.send_photo(message.chat.id, idphoto)

if __name__ == '__main__':
    app.config['api_key'] = '5518757007:AAEDj6_9mezeOalMO-aAbcQxL0mmO4VZJ2o'
    app.poll(debug=True)
