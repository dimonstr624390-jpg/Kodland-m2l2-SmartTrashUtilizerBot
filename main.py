import telebot
from logic import sortprob

bot = telebot.TeleBot('8489617318:AAEBJuPjFoUOiScu0odoG9bIQzGOJ3A9FUA')

@bot.message_handler(commands=['start', 'ok'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Используй команду /help для большей информации об этом бесполезном боте.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, """Я могу сам распределить ваш мусор по урнам, как только вы его покажите(эмодзи). Для этого напишите команду /sort
/ok - вернуться обратно
/list - эмодзи, которые я могу переработать.""")

@bot.message_handler(commands=['sort'])
def send_sorting(message):
    bot.reply_to(message, "Пожалуйста, отправьте любое эмодзи стекла, пластика, бумаги или метала для сортировки")

@bot.message_handler(commands=['list'])
def send_sorting(message):
    bot.reply_to(message, """Стекло - 🪞, 🔮, 🥃, 🍸, 🍷, 🍺, 🍶, 🧴, 🧪, 🔬, 🔭, 💉, 🏺
                 
Пластик - 💳, 🪪, 🧴, 🔫, 🪀, 🪁, 🧩, 🎮, 🕹️, 💾, 💿, 📀, 🖨️, 🛢️, 🗑️, 🪣, 🧺, 🛍️, 📏
                 
Бумага - 📄, 📃, 📜, 📑, 🧻, 📰, 📒, 📔, 📕, 📖, 📗, 📘, 📙, 📚, 📓, 🗞️, 🎫, 🧾, 📇, 📋, 📁, 📂, 🗂️, 💌, 📨, 📩, ✉️, 📦, 🏷️, 🪪
                 
Металл - 🔑, 🗝️, ⚙️, ⛓️, 🔗, 🛠️, 🔨, 🪚, 🪛, 🔧, 💣, 🪙, 💰, 💎, 🥇, 🥈, 🥉, 🏆, 🎖️, ✂️, 🔪, 🗡️, 🪓, 🪄, 🪝, 🪜, 🪠, 🛡️, 🪞, 🕰️, ⏰, 🚲, 🏍️, 🚗, ✈️, 🚀, 🚂, 🚇, 🛞, ⚔️, 🪺""")

@bot.message_handler(func=lambda message: True)
def handle_emoji(message):
    if message.text:
        result = sortprob(message.text) 
        bot.reply_to(message, result)

if __name__ == '__main__':
    print("Бот запущен")
    bot.infinity_polling()
