import telebot
from telebot import types

bot = telebot.TeleBot("6543839952:AAFKL_2eFAcj7EfLwRwxptJ7vP0c6lHg-8Q")

STATE_DEFAULT = "default"
STATE_ASK_LOCATION = "ask_location"

user_states = {}
user_location = {}

def start_location_sharing(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item = types.KeyboardButton("Share Location", request_location=True)
    markup.add(item)

    bot.send_message(message.chat.id, "Click 'Share Location' to share your live location:", reply_markup=markup)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello there, I can help you find the nearest location to your destination. Provide me your current location.")
    start_location_sharing(message)

@bot.message_handler(content_types=['location', 'venue'])
def handle_shared_location(message):
    user_location[latitude] = message.location.latitude
    user_location[longitude] = message.location.longitude

    bot.reply_to(message, "Please type in the category of your destination.")
    user_states[message.chat.id] = STATE_ASK_LOCATION

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == STATE_ASK_LOCATION, content_types=['text'])
def handle_shared_destination(message):

def handle_error(message):
    bot.reply_to(message, "Please type in the category of your destination.")

bot.infinity_polling()