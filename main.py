import telebot
from config import *
import time
import threading
import scrapper
import bbdd

bot = telebot.TeleBot(BOT_TOKEN)
find = True

@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.reply_to(message, "Hola mundo")



@bot.message_handler(commands=["remove"])
def cmd_remove(message):
    print("remove message")
    mess = message.text.split(" ")
    print(len(mess))

    if len(mess) == 2:
        conn = bbdd.create_connection()
        link = mess[1]
        bbdd.delete_web_watching(conn[0],conn[1],link)
        bot.send_message(CHANNEL, link + " borrado")


@bot.message_handler(commands=["vigila"])
def cmd_vigila(message):
    while True:
        conn = bbdd.create_connection()
        result = bbdd.read_web_watching(conn[0], conn[1])
        listWebsAcademiaDelCine = dict((x, y) for x, y in result)

        for k, v in listWebsAcademiaDelCine.items():
            print("k= " + k + " V= " + v)
            if scrapper.checkTickedAcademiaDelCine(k) and v != "debugg":
                bot.send_message(CHANNEL_PUBLIC, "Entradas disponibles para " + k)
                bot.send_message(CHANNEL, "Entradas disponibles para " + k)
            elif scrapper.checkTickedAcademiaDelCine(k) and v == "debugg":
                bot.send_message(CHANNEL, "Entradas disponibles para " + k)
            else:
                bot.send_message(CHANNEL,"Entradas no disponibles para " + v)
        bot.send_message(CHANNEL, "_________________________________________")
        time.sleep(30)


@bot.message_handler(commands=["add_academy"])
def cmd_added_academy(message):
    if len(message.text) > 3:
        body_message = message.text.split(" ")
        print(message.text)
        for i in body_message:
            print("i= " + i)
        link = body_message[1]
        title = body_message[2]
        conn = bbdd.create_connection()

        bbdd.insert_web_watching(conn[0], conn[1], link, title, "academia", False)
        conn = bbdd.create_connection()
        bot.send_message(CHANNEL, "Añadido")
    else:
        bot.send_message(CHANNEL, "Datos mal introducidos")

@bot.message_handler(content_types=["text"])
def plain_text(message):
    print(message.chat.id)

def receiver_messages():
    bot.infinity_polling()


if __name__ == '__main__':
    conn = bbdd.create_connection()
    bbdd.create_table(conn[0], conn[1])
    print("iniciar bot")
    thread_bot = threading.Thread(name="threadBot", target=receiver_messages)
    thread_bot.start()
    print("fin del bot")
