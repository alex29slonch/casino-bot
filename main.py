import random
import time

import config
import texts

import telebot
import logging
from telebot import types

bot = telebot.TeleBot(config.token)
logging.basicConfig(level=logging.INFO, filename='mainlog.log', filemode='w', format='%(asctime)s %(levelname)s %(message)s')

def get_emoji_num(num):
    if num == 1:
        text = texts.num_text1

    elif num == 2:
        text = texts.num_text2

    elif num == 3:
        text = texts.num_text3

    elif num == 4:
        text = texts.num_text4

    elif num == 5:
        text = texts.num_text5

    elif num == 6:
        text = texts.num_text6

    return text

def check_nums(number, bot_number):
    if number > bot_number:
        pass
    elif number == bot_number:
        pass
    else:
        pass

def dice_buttons():

    markup = types.ReplyKeyboardMarkup()
    trow_button = types.KeyboardButton(text=texts.but_throw_text)
    rules_button = types.KeyboardButton(text=texts.but_rules_text)
    markup.add(trow_button, rules_button)
    return markup

@bot.message_handler(commands=['start'])
def send_start_message(message):
    bot.send_message(message.chat.id, texts.start_text)

@bot.message_handler(commands=['dice'])
def start_game(message):
    bot.send_message(message.chat.id, texts.dice_text, reply_markup=dice_buttons())

@bot.message_handler(content_types=['text'])
def check_text(message):
    if message.text == texts.but_throw_text:
        num = random.randint(1, 6)
        bot.send_message(message.chat.id, f'{texts.num_text} <b>{get_emoji_num(num)}</b>', parse_mode='html')

        time.sleep(1)
        bot.send_message(message.chat.id, f'<i>{texts.bot_num_text1}</i>', parse_mode='html')

        time.sleep(3)
        bot_num = random.randint(1, 6)
        bot.send_message(message.chat.id, f'<i>{texts.bot_num_text2} <b>{get_emoji_num(bot_num)}</b></i>', parse_mode='html')
        check_nums(num, bot_num)

if __name__ == '__main__':
    bot.polling(none_stop=True)
