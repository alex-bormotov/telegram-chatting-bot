import json

import telebot
from telebot import types


def get_config():
    with open("config.json", "r") as read_file:
        config = json.load(read_file)
        return config

# https://github.com/python-telegram-bot/python-telegram-bot
bot = telebot.TeleBot(get_config()["telegram_bot_token"])


def send_typing(message):
    bot.send_chat_action(message.from_user.id, 'typing')
    # sendChatAction
    # action_string can be one of the following strings: 'typing', 'upload_photo', 'record_video', 'upload_video',
    # 'record_audio', 'upload_audio', 'upload_document' or 'find_location'.
    # bot.send_chat_action(chat_id, action_string)
def send_typing_image(message):
    bot.send_chat_action(message.from_user.id, 'upload_photo')

def send_typing_audio(message):
    bot.send_chat_action(message.from_user.id, 'record_audio')

def send_typing_video(message):
    bot.send_chat_action(message.from_user.id, 'upload_video')
############### Keyboards #####################################################

def keyboard(keyboard_number):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button_a = ""
    button_b = ""
    button_c = ""
    button_d = ""
    button_e = ""

    if len(get_config()['keyboards'][f'keyboard_{keyboard_number}_btn_1']) > 0:
        btns_btn_a = get_config()['keyboards'][f'keyboard_{keyboard_number}_btn_1']
        button_a = types.KeyboardButton(get_config()['buttons'][btns_btn_a])
        # markup.row(button_a)

    else:
        pass
    if len(get_config()['keyboards'][f'keyboard_{keyboard_number}_btn_2']) > 0:
        btns_btn_b = get_config()['keyboards'][f'keyboard_{keyboard_number}_btn_2']
        button_b = types.KeyboardButton(get_config()['buttons'][btns_btn_b])
        # markup.row(button_b)
    else:
        pass
    if len(get_config()['keyboards'][f'keyboard_{keyboard_number}_btn_3']) > 0:
        btns_btn_c = get_config()['keyboards'][f'keyboard_{keyboard_number}_btn_3']
        button_c = types.KeyboardButton(get_config()['buttons'][btns_btn_c])
        # markup.row(button_c)
    else:
        pass
    if len(get_config()['keyboards'][f'keyboard_{keyboard_number}_btn_4']) > 0:
        btns_btn_d = get_config()['keyboards'][f'keyboard_{keyboard_number}_btn_4']
        button_d = types.KeyboardButton(get_config()['buttons'][btns_btn_d])
        # markup.row(button_d)
    else:
        pass
    if len(get_config()['keyboards'][f'keyboard_{keyboard_number}_btn_5']) > 0:
        btns_btn_e = get_config()['keyboards'][f'keyboard_{keyboard_number}_btn_5']
        button_e = types.KeyboardButton(get_config()['buttons'][btns_btn_e])
        # markup.row(button_e)
    else:
        pass
    markup.row(button_a, button_b)
    markup.row(button_c, button_d, button_e)
    if get_config()["keyboards"][f"keyboard_{keyboard_number}_ReplyKeyboardRemove"] == "True":
        markup = types.ReplyKeyboardRemove(selective=True)
    return markup



def get_keyboard_reply_markup(btn):
    if get_config()['button_belong_keyboard'][btn] == "keyboard_1":
        reply_markup = keyboard("1")
    if get_config()['button_belong_keyboard'][btn] == "keyboard_2":
        reply_markup = keyboard("2")
    if get_config()['button_belong_keyboard'][btn] == "keyboard_3":
        reply_markup = keyboard("3")
    if get_config()['button_belong_keyboard'][btn] == "keyboard_4":
        reply_markup = keyboard("4")
    if get_config()['button_belong_keyboard'][btn] == "keyboard_5":
        reply_markup = keyboard("5")
    if get_config()['button_belong_keyboard'][btn] == "keyboard_6":
        reply_markup = keyboard("6")
    if get_config()['button_belong_keyboard'][btn] == "keyboard_7":
        reply_markup = keyboard("7")
    if get_config()['button_belong_keyboard'][btn] == "keyboard_8":
        reply_markup = keyboard("8")
    if get_config()['button_belong_keyboard'][btn] == "keyboard_9":
        reply_markup = keyboard("9")
    if get_config()['button_belong_keyboard'][btn] == "keyboard_10":
        reply_markup = keyboard("10")

    return reply_markup

############# Order data ##############################################################################################################################

def get_order_data(message):
    if message.text == get_config()['buttons']['btn4']:
        send_typing(message)
        bot.send_message(message.from_user.id, text=get_config()['messages']['msg4'][1], reply_markup=get_keyboard_reply_markup('btn1'))
        bot.register_next_step_handler(message, cancel)
    else:
        send_typing(message)
        bot.send_message(message.from_user.id, text=get_config()['order_data']['ord1'])
        zero = message.text
        bot.register_next_step_handler(message, get_order_data_0, zero)

def get_order_data_0(message, zero):
    one = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord2'])
    bot.register_next_step_handler(message, get_order_data_1, zero, one)


def get_order_data_1(message, zero, one):
    two = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord3'])
    bot.register_next_step_handler(message, get_order_data_2, zero, one, two)

def get_order_data_2(message, zero, one, two):
    three = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord4'])
    bot.register_next_step_handler(message, get_order_data_3, zero, one, two, three)


def get_order_data_3(message, zero, one, two, three):
    four = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord5'])
    bot.register_next_step_handler(message, get_order_data_4, zero, one, two, three, four)


def get_order_data_4(message, zero, one, two, three, four):
    five = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord6'])
    bot.register_next_step_handler(message, get_order_data_5, zero, one, two, three, four, five)


def get_order_data_5(message, zero, one, two, three, four, five):
    six = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord7'])
    bot.register_next_step_handler(message, get_order_data_6, zero, one, two, three, four, five, six)


def get_order_data_6(message, zero, one, two, three, four, five, six):
    seven = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord8'])
    bot.register_next_step_handler(message, get_order_data_7, zero, one, two, three, four, five, six, seven)


def get_order_data_7(message, zero, one, two, three, four, five, six, seven):
    eight = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord9'])
    bot.register_next_step_handler(message, get_order_data_8, zero, one, two, three, four, five, six, seven, eight)


def get_order_data_8(message, zero, one, two, three, four, five, six, seven, eight):
    nine = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['add_vars']['thanks_for_order'], reply_markup=get_keyboard_reply_markup('btn1'))
    send_typing(message)
    bot.send_message(message.from_user.id, text=f"{zero}, {one}, {two}, {three}, {four}, {five}, {six}, {seven}, {eight}, {nine}", reply_markup=get_keyboard_reply_markup('btn1'))
    # bot.send_message(931750534, text=f"{one}\n{two}\n{three}\n{four}\n{five}\n{six}\n{seven}\n{eight}\n{nine}", reply_markup=get_keyboard_reply_markup('btn1'))


################ Media Buttons #########################################################################################################################

# https://github.com/eternnoir/pyTelegramBotAPI#telebot

def send_image(message):
    # sendPhoto
    # print(message.from_user.id)
    send_typing_image(message)
    photo = open('media_samples/image.jpg', 'rb')
    bot.send_photo(message.from_user.id, photo, reply_markup=get_keyboard_reply_markup('btn1'))
    # bot.send_photo(message.from_user.id, "FILEID")


def send_video(message):

    # send_typing_video(message)
    video = open('media_samples/video.mp4', 'rb')
    bot.send_video(message.from_user.id, video, reply_markup=get_keyboard_reply_markup('btn1'))
    # bot.send_video(message.from_user.id, "FILEID")


def send_audio(message):

    # sendAudio
    # send_typing_audio(message)
    audio = open('media_samples/audio.mp3', 'rb')
    bot.send_audio(message.from_user.id, audio, reply_markup=get_keyboard_reply_markup('btn1'))
    # bot.send_audio(message.from_user.id, "FILEID")

    # sendVoice
    # voice = open('/tmp/voice.ogg', 'rb')
    # bot.send_voice(chat_id, voice)
    # bot.send_voice(chat_id, "FILEID")


# sendLocation
# bot.send_location(chat_id, lat, lon)

############### Name and Phone #############################################################################################################################

def get_user_name(message):
    if message.text == get_config()['buttons']['btn4']:
        send_typing(message)
        bot.send_message(message.from_user.id, text=get_config()['messages']['msg4'][1])
        bot.register_next_step_handler(message, cancel)
    else:
        name = message.text
        send_typing(message)
        bot.send_message(message.from_user.id, text=f"{get_config()['add_vars']['phone']} ?")
        bot.register_next_step_handler(message, get_user_phone, name)


def get_user_phone(message, name):
    phone = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=f"{get_config()['add_vars']['name']}: {name}\n{get_config()['add_vars']['phone']}: {phone}", reply_markup=get_keyboard_reply_markup('btn1'))
    # bot.send_message(931750534, text=f"{name} {phone}", reply_markup=get_keyboard_reply_markup('btn1'))


####################   Cancel Button  ###############################################################################################################

def cancel(message):
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['messages']['msg1'], reply_markup=get_keyboard_reply_markup('btn13'))

###########################################################################################################################################################


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['messages']['msg1'], reply_markup=get_keyboard_reply_markup('btn13'))
    # bot.register_next_step_handler(message, handler)


@bot.message_handler(content_types=["text"])
def handler(message):
    try:
        if message.text in [v for v in get_config()['buttons'].values()]:
            btn = [k for k, v in get_config()['buttons'].items() if message.text == v][0]
            msg_content = get_config()['messages'][f'msg{btn[3:]}']

            if type(msg_content) is str:
                msg = msg_content
                send_typing(message)
                bot.send_message(message.from_user.id, text=msg, reply_markup=get_keyboard_reply_markup(btn))
            if type(msg_content) is list:
                func = eval(msg_content[0])
                msg = msg_content[1]
                bot.send_message(message.from_user.id, text=msg, reply_markup=get_keyboard_reply_markup(btn))
                bot.register_next_step_handler(message, func)





    except Exception as e:
        bot.send_message(message.from_user.id, text=str(e))



# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
# bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
# bot.load_next_step_handlers()

bot.polling(none_stop=False, interval=0, timeout=20)
