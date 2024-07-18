import threading
import telebot
import time
from parsernews_save_date_in_file import get_news

bot = telebot.TeleBot('7095456957:AAHekdlVpLG2wzgaqXvnRGQfy9o5z4QzffA')

site = "https://unn.ua/politics"


@bot.message_handler(commands=['status'])
def status(message):
    bot.send_message(message.chat.id, "Бот працює")


@bot.message_handler(commands=['start'])
def start(message):
    with open("userids.txt", "r", encoding="utf-8") as file:
        users = file.readlines()
    if str(message.chat.id)+'\n' not in users:
        users.append(str(message.chat.id)+'\n')
        with open("userids.txt", "w", encoding="utf-8") as file:
            file.writelines(users)
            bot.send_message(message.chat.id, 'Вас додано до користувачів боту')
    else:
         bot.send_message(message.chat.id, 'Ви вже є користувачем боту')


def background_task():
    last_news = ["o"]
    current_news = ["d"]
    while True:
        markup = telebot.types.InlineKeyboardMarkup()
        with open("datenews.txt", "r", encoding="utf-8") as file:
            current_news = file.readlines()
        if current_news[0] != last_news[0]:
            last_news = current_news
            with open("userids.txt", "r", encoding="utf-8") as file:
                for line in file:
                    markup.add(telebot.types.InlineKeyboardButton('Читати далі', last_news[1]))
                    bot.send_message(int(line), last_news[0], reply_markup=markup)
        time.sleep(5)


background_thread = threading.Thread(target=background_task)
background_thread.daemon = True
background_thread.start()

background_thread2 = threading.Thread(target=get_news)
background_thread2.daemon = True
background_thread2.start()

bot.infinity_polling()

