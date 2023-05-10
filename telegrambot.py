import telebot
git add
git commit -m "Initial commit"
git push -u origin master
git remote add origin https://github.com/danil-lonely/danil-lonely.git
bot.set_webhook(url='https://github.com/Danil-Lonely/danil-lonely/tree/73a3391552ef524442a867070884d2227e41602f#hi-there-')
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
