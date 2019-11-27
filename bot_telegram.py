import telebot
from telebot import types
from config import get_config
from notification import send_email



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
    if get_config()['button_belong_keyboard'][btn] == "keyboard_11":
        reply_markup = keyboard("11")
    if get_config()['button_belong_keyboard'][btn] == "keyboard_12":
        reply_markup = keyboard("12")
    if get_config()['button_belong_keyboard'][btn] == "keyboard_13":
        reply_markup = keyboard("13")
    if get_config()['button_belong_keyboard'][btn] == "keyboard_14":
        reply_markup = keyboard("14")
    if get_config()['button_belong_keyboard'][btn] == "keyboard_15":
        reply_markup = keyboard("15")

    return reply_markup

############# Order data ##############################################################################################################################

def leave_order(message):
    if message.text == get_config()['buttons']['btn4']:
        send_typing(message)
        bot.send_message(message.from_user.id, text=get_config()['messages']['msg4'][1], reply_markup=get_keyboard_reply_markup('btn1'))
        bot.register_next_step_handler(message, cancel)
    else:
        send_typing(message)
        bot.send_message(message.from_user.id, text=get_config()['order_data']['ord_question_1'])
        bot.register_next_step_handler(message, leave_order_0)


def leave_order_0(message):
    one = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord_question_2'])
    bot.register_next_step_handler(message, leave_order_1, one)


def leave_order_1(message, one):
    two = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord_question_3'])
    bot.register_next_step_handler(message, leave_order_2, one, two)

def leave_order_2(message, one, two):
    three = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord_question_4'])
    bot.register_next_step_handler(message, leave_order_3, one, two, three)


def leave_order_3(message, one, two, three):
    four = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord_question_5'])
    bot.register_next_step_handler(message, leave_order_4, one, two, three, four)


def leave_order_4(message, one, two, three, four):
    five = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord_question_6'])
    bot.register_next_step_handler(message, leave_order_5, one, two, three, four, five)


def leave_order_5(message, one, two, three, four, five):
    six = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord_question_7'])
    bot.register_next_step_handler(message, leave_order_6, one, two, three, four, five, six)


def leave_order_6(message, one, two, three, four, five, six):
    seven = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord_question_8'])
    bot.register_next_step_handler(message, leave_order_7, one, two, three, four, five, six, seven)


def leave_order_7(message, one, two, three, four, five, six, seven):
    eight = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord_question_9'])
    bot.register_next_step_handler(message, leave_order_8, one, two, three, four, five, six, seven, eight)


def leave_order_8(message, one, two, three, four, five, six, seven, eight):
    nine = message.text
    send_typing(message)

    send_email(f"{one}, {two}, {three}, {four}, {five}, {six}, {seven}, {eight}, {nine}")

    bot.send_message(message.from_user.id, text=get_config()['order_data']['thanks_for_order'], reply_markup=get_keyboard_reply_markup('btn1'))
    # send_typing(message)
    # bot.send_message(message.from_user.id, text=f"{one}, {two}, {three}, {four}, {five}, {six}, {seven}, {eight}, {nine}", reply_markup=get_keyboard_reply_markup('btn1'))
    # bot.send_message(931750534, text=f"{one}\n{two}\n{three}\n{four}\n{five}\n{six}\n{seven}\n{eight}\n{nine}", reply_markup=get_keyboard_reply_markup('btn1'))



############### Name and Phone #############################################################################################################################

def leave_contacts(message):
    if message.text == get_config()['buttons']['btn4']:
        send_typing(message)
        bot.send_message(message.from_user.id, text=get_config()['messages']['msg4'][1])
        bot.register_next_step_handler(message, cancel)
    else:
        name = message.text
        send_typing(message)
        bot.send_message(message.from_user.id, text=f"{get_config()['order_data']['phone']}")
        bot.register_next_step_handler(message, get_user_phone, name)


def get_user_phone(message, name):
    phone = message.text
    send_typing(message)
    # bot.send_message(message.from_user.id, text=f"{get_config()['order_data']['name']}: {name}\n{get_config()['order_data']['phone']}: {phone}", reply_markup=get_keyboard_reply_markup('btn1'))
    # bot.send_message(931750534, text=f"{name} {phone}", reply_markup=get_keyboard_reply_markup('btn1'))

    send_email(f"{name}, {phone}")

    bot.send_message(message.from_user.id, text=get_config()['order_data']['tnahks'], reply_markup=get_keyboard_reply_markup('btn1'))

####################   Cancel Button  ###############################################################################################################

def cancel(message):
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['messages']['msg1'], reply_markup=get_keyboard_reply_markup('btn13'))


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
