import util, os, telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))

STATE_DEFAULT = "default"
STATE_ASK_LOCATION = "ask_location"
LOCATION_LIMIT = 10

user_states = {}
user_location = {}

@bot.message_handler(commands=['update'])
def start_location_sharing(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item = types.KeyboardButton("Share Location", request_location=True)
    markup.add(item)

    bot.send_message(message.chat.id, "Click 'Share Location' to share your live location:", reply_markup=markup)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello there, I can help you find the nearest location to your destination. Provide me your current location.")
    start_location_sharing(message)

@bot.message_handler(commands=['exit'])
def send_exit(message):
    bot.reply_to(message, "Bye. Thank you for chosing locator. If you require assistance again, press /start to begin a new conversation.")

@bot.message_handler(content_types=['location', 'venue'])
def handle_shared_location(message):
    user_location['latitude'] = message.location.latitude
    user_location['longitude'] = message.location.longitude

    bot.reply_to(message, "Please type in the category of your destination.")
    user_states[message.chat.id] = STATE_ASK_LOCATION

def handle_error(message):
    bot.reply_to(message, "Please type in an appropriate category of your destination.")

def ask_help(message):
    bot.reply_to(message, "You can ask for nearest locations of another category by entering the chat again.")

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == STATE_ASK_LOCATION, content_types=['text'])
def handle_shared_destination(message):
    try:
        parsed_input = util.parse_category_input(message.text)
    except ValueError as e:
        handle_error(message)
    else:
        reply = util.get_nearby_places(user_location, parsed_input, LOCATION_LIMIT)
        bot.reply_to(message, str(reply))
        ask_help(message)

bot.infinity_polling()
