import telebot

bot = telebot.TeleBot('6056497295:AAEojGoXBvz6nYHaJA5yCc1h9h3ZaVv1TIw')
bot.set_webhook(url='https://yourdomain.com/your-webhook-path')
@bot.message_handler(commands=['kick'])
def kick_user(message):
    user_id = message.reply_to_message.from_user.id
    bot.kick_chat_member(message.chat.id, user_id)
@bot.message_handler(commands=['mute'])
def mute_user(message):
    user_id = message.reply_to_message.from_user.id
    bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=False)

@bot.message_handler(commands=['ban'])
def ban_user(message):
    user_id = message.reply_to_message.from_user.id
    bot.kick_chat_member(message.chat.id, user_id)
    bot.unban_chat_member(message.chat.id, user_id)

@bot.message_handler(commands=['rob'])
def rob_user(message):
    bot.reply_to(message, "Вы были ограблены!")

@bot.message_handler(commands=['slap'])
def slap_user(message):
    bot.reply_to(message, "Вы получили шлепок!")


@bot.message_handler(commands=['kiss'])
def kiss_user(message):
    bot.reply_to(message, "Вы были поцелованы!")

def send_image(message):
    with open('image.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

bot.polling()