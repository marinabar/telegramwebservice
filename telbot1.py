import telebot
from flask import Flask, render_template
from threading import Thread
app = Flask(__name__)
token = "664959010:AAFmQYtPrmhuq4bc7O0J_NuYmbgmK10M-S0"
telebot.apihelper.proxy = {'https': 'socks5://tvorogme@tvorog.me:6666'}
bot = telebot.TeleBot(token=token)

msg = []
messag=''
@bot.message_handler(content_types=['text'])
def echo(message):
    global messag
    text = message.text
    user = message.chat.id
    msg.append(text)
    bot.send_message(user, 'Ok')
    print(msg)
    messag = ', '.join(msg)
def redo():
    bot.polling(none_stop=True)




redo_thread = Thread(target=redo)

redo_thread.start()


@app.route('/')
def index():
    return '''<html><head></head>
        <body>
        <h1>
            All Telegram messages
        </h1>
        <p>{}</p>
        </html>
        '''.format(messag)


app.run(debug='True', port='8080')
