import telebot
from telebot import types

bot = telebot.TeleBot('5970767489:AAEZiGknRy87MUYS7QmHUNAwV08aOloF0mY')

smartphones = ["Apple Iphone 10", "Samsung Galaxy S4", "Xiaomi Redmi Note 8", "Huawei P20 Pro", "Google Pixel 7"]
tvs = ["Samsung UE43N5510AU", "Philips 58PUS850", "Xiaomi Mi TV 4S 55 T2", "Samsung UE55TU7090U",
       "LG 32LH595", "LG OLED55B6V"]
laptops = ["Apple MacBook Air M1 2020", "Microsoft Surface Laptop 4", "HP Spectre x360", "DELL XPS 13",
           "Acer Swift 3", "Apple MacBook Pro 16", "ASUS ROG Zephyrus G14", "Lenovo ThinkPad X1 Carbon"]
headphones = ["Apple AirPods Pro 2", "Jabra Elite 85h", "Sony WF-1000XM3", "Apple AirPods 3",
              "Beats Fit Pro", "Sony WH-1000XM2"]
MP3_players = ["Cowon Plenue D2", "Sony NW-A45", "Apple iPod Touch", "FiiO M11 Pro", "Cowon Plenue D"]

smartphone_price = [79900, 13200, 56400, 32800, 45900, 28400]
tv_price = [25900, 36700, 82400, 54700, 32500, 71400]
laptop_price = [91500, 38900, 67400, 56200, 23300, 89900, 43500, 85600]
headphone_price = [23500, 13800, 8400, 10400, 15600, 11600]
mp3_player_price = [12500, 7400, 5900, 10600, 6200]


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    keyboard = types.InlineKeyboardMarkup()
    keySmartphone = types.InlineKeyboardButton(
        text='Смартфоны', callback_data='smartphones')
    keyboard.add(keySmartphone)
    keyTV = types.InlineKeyboardButton(
        text='Телевизоры', callback_data='tvs')
    keyboard.add(keyTV)
    keyLaptop = types.InlineKeyboardButton(
        text='Ноутбуки', callback_data='laptops')
    keyboard.add(keyLaptop)
    keyHeadphone = types.InlineKeyboardButton(
        text='Наушники', callback_data='headphones')
    keyboard.add(keyHeadphone)
    keyMP3player = types.InlineKeyboardButton(
        text='MP3-плееры', callback_data='MP3_players')
    keyboard.add(keyMP3player)
    bot.send_message(message.from_user.id,
                     text='Выбери вид техники', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "smartphones":
        keyboard = types.InlineKeyboardMarkup()

        for i in range(len(smartphones)):
            keySmartphoneModel = types.InlineKeyboardButton(
                text=smartphones[i], callback_data='smartphoneModel' + str(i))
            keyboard.add(keySmartphoneModel)
        bot.send_message(call.from_user.id,
                         text='Выбери модель смартфона', reply_markup=keyboard)

    if call.data == "tvs":
        keyboard = types.InlineKeyboardMarkup()

        for i in range(len(tvs)):
            keyTVModel = types.InlineKeyboardButton(
                text=tvs[i], callback_data='tvModel' + str(i))
            keyboard.add(keyTVModel)
        bot.send_message(call.from_user.id,
                         text='Выбери модель телевизора', reply_markup=keyboard)

    elif call.data == "laptops":
        keyboard = types.InlineKeyboardMarkup()

        for i in range(len(laptops)):
            keyLaptopModel = types.InlineKeyboardButton(
                text=laptops[i], callback_data='laptopModel' + str(i))
            keyboard.add(keyLaptopModel)
        bot.send_message(call.from_user.id,
                         text='Выбери модель ноутбука', reply_markup=keyboard)

    elif call.data == "headphones":
        keyboard = types.InlineKeyboardMarkup()

        for i in range(len(headphones)):
            keyHeadphoneModel = types.InlineKeyboardButton(
                text=headphones[i], callback_data='headphonesModel' + str(i))
            keyboard.add(keyHeadphoneModel)
        bot.send_message(call.from_user.id,
                         text='Выбери модель наушников', reply_markup=keyboard)

    elif call.data == "MP3_players":
        keyboard = types.InlineKeyboardMarkup()

        for i in range(len(MP3_players)):
            keyMP3playerModel = types.InlineKeyboardButton(
                text=MP3_players[i], callback_data='mp3Model' + str(i))
            keyboard.add(keyMP3playerModel)
        bot.send_message(call.from_user.id,
                         text='Выбери модель MP3-плеера', reply_markup=keyboard)
    else:
        msg = "Рыночная цена "
        if 'smartphoneModel' in call.data:
            for i in range(len(smartphones)):
                if call.data == 'smartphoneModel' + str(i):
                    msg += smartphones[i] + ": " + str(smartphone_price[i])
                    break
            bot.send_message(call.message.chat.id, msg)
        elif 'tvModel' in call.data:
            for i in range(len(tvs)):
                if call.data == 'tvModel' + str(i):
                    msg += tvs[i] + ": " + str(tv_price[i])
                    break
            bot.send_message(call.message.chat.id, msg)
        elif 'laptopModel' in call.data:
            for i in range(len(laptops)):
                if call.data == 'laptopModel' + str(i):
                    msg += laptops[i] + ": " + str(laptop_price[i])
                    break
            bot.send_message(call.message.chat.id, msg)
        elif 'headphonesModel' in call.data:
            for i in range(len(headphones)):
                if call.data == 'headphonesModel' + str(i):
                    msg += headphones[i] + ": " + str(headphone_price[i])
                    break
            bot.send_message(call.message.chat.id, msg)
        elif 'mp3Model' in call.data:
            for i in range(len(MP3_players)):
                if call.data == 'mp3Model' + str(i):
                    msg += MP3_players[i] + ": " + str(mp3_player_price[i])
                    break
            bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)
