import telebot

bot = telebot.TeleBot("5339792476:AAH29caOBZ_imHgS3y1TtjnCjtMNcnmMdhA") #Чтобы получить токен, в телеграме нужно найти бота с ником @BotFather и написать команду /newbot

@bot.message_handler(content_types=['text']) #наша функция реагирует только на один аргумент - текстовое сообщение, на картинки, войсы, стикеры он не реагирует
def send_echo(message):  #наша функция принимает только один параметр, сообщенеи)
    #bot.reply_to(message,message.text) #функция ответа
    bot.send_message(message.chat.id, message.text)

bot.polling( none_stop = True )

