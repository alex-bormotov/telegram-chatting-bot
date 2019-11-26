import json

import telebot
from telebot import types


def get_config():
    with open("config.json", "r") as read_file:
        config = json.load(read_file)
        return config

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

def keyboard_1():
    markup = types.ReplyKeyboardMarkup()

    if len(get_config()['keyboards']['keyboard_1_btn_1']) > 0:
        btns_btn_a = get_config()['keyboards']['keyboard_1_btn_1']
        button_a = types.KeyboardButton(get_config()['buttons'][btns_btn_a])
        markup.row(button_a)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_1_btn_2']) > 0:
        btns_btn_b = get_config()['keyboards']['keyboard_1_btn_2']
        button_b = types.KeyboardButton(get_config()['buttons'][btns_btn_b])
        markup.row(button_b)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_1_btn_3']) > 0:
        btns_btn_c = get_config()['keyboards']['keyboard_1_btn_3']
        button_c = types.KeyboardButton(get_config()['buttons'][btns_btn_c])
        markup.row(button_c)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_1_btn_4']) > 0:
        btns_btn_d = get_config()['keyboards']['keyboard_1_btn_4']
        button_d = types.KeyboardButton(get_config()['buttons'][btns_btn_d])
        markup.row(button_d)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_1_btn_5']) > 0:
        btns_btn_e = get_config()['keyboards']['keyboard_1_btn_5']
        button_e = types.KeyboardButton(get_config()['buttons'][btns_btn_e])
        markup.row(button_e)
    else:
        pass
    # markup.row(button_a, button_b, button_c)
    # markup.row(itembtnc, itembtnd, itembtne)
    if get_config()["keyboards"]["keyboard_1_ReplyKeyboardRemove"] == "True":
        markup = types.ReplyKeyboardRemove(selective=True)
    return markup


def keyboard_2():
    markup = types.ReplyKeyboardMarkup()

    if len(get_config()['keyboards']['keyboard_2_btn_1']) > 0:
        btns_btn_a = get_config()['keyboards']['keyboard_2_btn_1']
        button_a = types.KeyboardButton(get_config()['buttons'][btns_btn_a])
        markup.row(button_a)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_2_btn_2']) > 0:
        btns_btn_b = get_config()['keyboards']['keyboard_2_btn_2']
        button_b = types.KeyboardButton(get_config()['buttons'][btns_btn_b])
        markup.row(button_b)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_2_btn_3']) > 0:
        btns_btn_c = get_config()['keyboards']['keyboard_2_btn_3']
        button_c = types.KeyboardButton(get_config()['buttons'][btns_btn_c])
        markup.row(button_c)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_2_btn_4']) > 0:
        btns_btn_d = get_config()['keyboards']['keyboard_2_btn_4']
        button_d = types.KeyboardButton(get_config()['buttons'][btns_btn_d])
        markup.row(button_d)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_2_btn_5']) > 0:
        btns_btn_e = get_config()['keyboards']['keyboard_2_btn_5']
        button_e = types.KeyboardButton(get_config()['buttons'][btns_btn_e])
        markup.row(button_e)
    else:
        pass
    # markup.row(button_a, button_b, button_c)
    # markup.row(itembtnc, itembtnd, itembtne)
    if get_config()["keyboards"]["keyboard_2_ReplyKeyboardRemove"] == "True":
        markup = types.ReplyKeyboardRemove(selective=True)
    return markup


def keyboard_3():
    markup = types.ReplyKeyboardMarkup()

    if len(get_config()['keyboards']['keyboard_3_btn_1']) > 0:
        btns_btn_a = get_config()['keyboards']['keyboard_3_btn_1']
        button_a = types.KeyboardButton(get_config()['buttons'][btns_btn_a])
        markup.row(button_a)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_3_btn_2']) > 0:
        btns_btn_b = get_config()['keyboards']['keyboard_3_btn_2']
        button_b = types.KeyboardButton(get_config()['buttons'][btns_btn_b])
        markup.row(button_b)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_3_btn_3']) > 0:
        btns_btn_c = get_config()['keyboards']['keyboard_3_btn_3']
        button_c = types.KeyboardButton(get_config()['buttons'][btns_btn_c])
        markup.row(button_c)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_3_btn_4']) > 0:
        btns_btn_d = get_config()['keyboards']['keyboard_3_btn_4']
        button_d = types.KeyboardButton(get_config()['buttons'][btns_btn_d])
        markup.row(button_d)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_3_btn_5']) > 0:
        btns_btn_e = get_config()['keyboards']['keyboard_3_btn_5']
        button_e = types.KeyboardButton(get_config()['buttons'][btns_btn_e])
        markup.row(button_e)
    else:
        pass
    # markup.row(button_a, button_b, button_c)
    # markup.row(itembtnc, itembtnd, itembtne)
    if get_config()["keyboards"]["keyboard_3_ReplyKeyboardRemove"] == "True":
        markup = types.ReplyKeyboardRemove(selective=True)
    return markup


def keyboard_4():
    markup = types.ReplyKeyboardMarkup()

    if len(get_config()['keyboards']['keyboard_4_btn_1']) > 0:
        btns_btn_a = get_config()['keyboards']['keyboard_4_btn_1']
        button_a = types.KeyboardButton(get_config()['buttons'][btns_btn_a])
        markup.row(button_a)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_4_btn_2']) > 0:
        btns_btn_b = get_config()['keyboards']['keyboard_4_btn_2']
        button_b = types.KeyboardButton(get_config()['buttons'][btns_btn_b])
        markup.row(button_b)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_4_btn_3']) > 0:
        btns_btn_c = get_config()['keyboards']['keyboard_4_btn_3']
        button_c = types.KeyboardButton(get_config()['buttons'][btns_btn_c])
        markup.row(button_c)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_4_btn_4']) > 0:
        btns_btn_d = get_config()['keyboards']['keyboard_4_btn_4']
        button_d = types.KeyboardButton(get_config()['buttons'][btns_btn_d])
        markup.row(button_d)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_4_btn_5']) > 0:
        btns_btn_e = get_config()['keyboards']['keyboard_4_btn_5']
        button_e = types.KeyboardButton(get_config()['buttons'][btns_btn_e])
        markup.row(button_e)
    else:
        pass
    # markup.row(button_a, button_b, button_c)
    # markup.row(itembtnc, itembtnd, itembtne)
    if get_config()["keyboards"]["keyboard_4_ReplyKeyboardRemove"] == "True":
        markup = types.ReplyKeyboardRemove(selective=True)
    return markup


def keyboard_5():
    markup = types.ReplyKeyboardMarkup()

    if len(get_config()['keyboards']['keyboard_5_btn_1']) > 0:
        btns_btn_a = get_config()['keyboards']['keyboard_5_btn_1']
        button_a = types.KeyboardButton(get_config()['buttons'][btns_btn_a])
        markup.row(button_a)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_5_btn_2']) > 0:
        btns_btn_b = get_config()['keyboards']['keyboard_5_btn_2']
        button_b = types.KeyboardButton(get_config()['buttons'][btns_btn_b])
        markup.row(button_b)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_5_btn_3']) > 0:
        btns_btn_c = get_config()['keyboards']['keyboard_5_btn_3']
        button_c = types.KeyboardButton(get_config()['buttons'][btns_btn_c])
        markup.row(button_c)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_5_btn_4']) > 0:
        btns_btn_d = get_config()['keyboards']['keyboard_5_btn_4']
        button_d = types.KeyboardButton(get_config()['buttons'][btns_btn_d])
        markup.row(button_d)
    else:
        pass
    if len(get_config()['keyboards']['keyboard_5_btn_5']) > 0:
        btns_btn_e = get_config()['keyboards']['keyboard_5_btn_5']
        button_e = types.KeyboardButton(get_config()['buttons'][btns_btn_e])
        markup.row(button_e)
    else:
        pass
    # markup.row(button_a, button_b, button_c)
    # markup.row(itembtnc, itembtnd, itembtne)
    if get_config()["keyboards"]["keyboard_5_ReplyKeyboardRemove"] == "True":
        markup = types.ReplyKeyboardRemove(selective=True)
    return markup


#####################################################

def cancel(message):
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['messages']['msg1'], reply_markup=get_keyboard_reply_markup('main_menu_button'))

############### Name and Phone #####################################################
def get_user_name(message):
    if message.text == get_config()['buttons']['cancel_button']:
        send_typing(message)
        bot.send_message(message.from_user.id, text=get_config()['messages']['cancel_message'])
        bot.register_next_step_handler(message, cancel)
    else:
        name = message.text
        send_typing(message)
        bot.send_message(message.from_user.id, text=f"{get_config()['add_vars']['phone']} ?")
        bot.register_next_step_handler(message, get_user_phone, name)


def get_user_phone(message, name):
    phone = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=f"{get_config()['add_vars']['name']}: {name}\n{get_config()['add_vars']['phone']}: {phone}", reply_markup=get_keyboard_reply_markup('main_menu_button'))
    # bot.send_message(931750534, text=f"{name} {phone}", reply_markup=get_keyboard_reply_markup('main_menu_button'))



############# Order data ######################################################
def get_order_data(message):
    if message.text == get_config()['buttons']['cancel_button']:
        send_typing(message)
        bot.send_message(message.from_user.id, text=get_config()['messages']['cancel_message'])
        bot.register_next_step_handler(message, cancel)
    else:
        one = message.text
        send_typing(message)
        bot.send_message(message.from_user.id, text=get_config()['order_data']['ord2'])
        bot.register_next_step_handler(message, get_order_data_1, one)


def get_order_data_1(message, one):
    two = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord3'])
    bot.register_next_step_handler(message, get_order_data_2, one, two)

def get_order_data_2(message, one, two):
    three = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord4'])
    bot.register_next_step_handler(message, get_order_data_3, one, two, three)


def get_order_data_3(message, one, two, three):
    four = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord5'])
    bot.register_next_step_handler(message, get_order_data_4, one, two, three, four)


def get_order_data_4(message, one, two, three, four):
    five = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord6'])
    bot.register_next_step_handler(message, get_order_data_5, one, two, three, four, five)


def get_order_data_5(message, one, two, three, four, five):
    six = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord7'])
    bot.register_next_step_handler(message, get_order_data_6, one, two, three, four, five, six)


def get_order_data_6(message, one, two, three, four, five, six):
    seven = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord8'])
    bot.register_next_step_handler(message, get_order_data_7, one, two, three, four, five, six, seven)


def get_order_data_7(message, one, two, three, four, five, six, seven):
    eight = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord9'])
    bot.register_next_step_handler(message, get_order_data_8, one, two, three, four, five, six, seven, eight)


def get_order_data_8(message, one, two, three, four, five, six, seven, eight):
    nine = message.text
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['messages']['after_order_message'], reply_markup=get_keyboard_reply_markup('main_menu_button'))
    send_typing(message)
    bot.send_message(message.from_user.id, text=f"{one}, {two}, {three}, {four}, {five}, {six}, {seven}, {eight}, {nine}", reply_markup=get_keyboard_reply_markup('main_menu_button'))
    # bot.send_message(931750534, text=f"{one}\n{two}\n{three}\n{four}\n{five}\n{six}\n{seven}\n{eight}\n{nine}", reply_markup=get_keyboard_reply_markup('main_menu_button'))



def get_keyboard_reply_markup(btn):
    if get_config()['button_belong_keyboard'][btn] == "keyboard_1":
        reply_markup = keyboard_1()
    if get_config()['button_belong_keyboard'][btn] == "keyboard_2":
        reply_markup = keyboard_2()
    if get_config()['button_belong_keyboard'][btn] == "keyboard_3":
        reply_markup = keyboard_3()
    if get_config()['button_belong_keyboard'][btn] == "keyboard_4":
        reply_markup = keyboard_4()
    if get_config()['button_belong_keyboard'][btn] == "keyboard_5":
        reply_markup = keyboard_5()

    return reply_markup


#######################################################################################################################################################
def next_func_after_btn_msg_contact(message):
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
    bot.register_next_step_handler(message, get_user_name)


def next_func_after_btn_msg_send_image(message):
    # sendPhoto
    photo = open('media_samples/image.jpg', 'rb')
    send_typing_image(message)
    bot.send_photo(message.from_user.id, photo)
    bot.send_photo(message.from_user.id, "FILEID")


def next_func_after_btn_msg_send_video(message):

    video = open('media_samples/video.mp4', 'rb')
    send_typing_video(message)
    bot.send_video(message.from_user.id, video)
    bot.send_video(message.from_user.id, "FILEID")


def next_func_after_btn_msg_send_audio(message):

    # sendAudio
    audio = open('media_samples/audio.mp3', 'rb')
    send_typing_audio(message)
    bot.send_audio(message.from_user.id, audio)
    bot.send_audio(message.from_user.id, "FILEID")

    # sendVoice
    # voice = open('/tmp/voice.ogg', 'rb')
    # bot.send_voice(chat_id, voice)
    # bot.send_voice(chat_id, "FILEID")


# sendLocation
# bot.send_location(chat_id, lat, lon)


def send_next_func_after_msg(message, btn, msg):
    if get_config()['next_func_after_btn_msg'][btn] == "contact":
        next_func_after_btn_msg_contact(message)
    if get_config()['next_func_after_btn_msg'][btn] == "video":
        next_func_after_btn_msg_send_video(message)
    if get_config()['next_func_after_btn_msg'][btn] == "audio":
        next_func_after_btn_msg_send_audio(message)
    if get_config()['next_func_after_btn_msg'][btn] == "image":
        next_func_after_btn_msg_send_image(message)
    else:
        bot.send_message(message.from_user.id, text=get_config()['messages'][msg], reply_markup=get_keyboard_reply_markup(btn))

###########################################################################################################################################################
###########################################################################################################################################################
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    send_typing(message)
    bot.send_message(message.from_user.id, text=get_config()['messages']['msg1'], reply_markup=get_keyboard_reply_markup('main_menu_button'))
    # bot.register_next_step_handler(message, handler)



@bot.message_handler(content_types=["text"])
def handler(message):
    try:
############################## Buttons with next step ########################################################################################################

        if len(get_config()['buttons']['contact_button']) > 0:
            if message.text == get_config()['buttons']['contact_button']:
                send_typing(message)
                bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                bot.register_next_step_handler(message, get_user_name)
        else:
            pass


        if len(get_config()['buttons']['order_button']) > 0:
            if message.text == get_config()['buttons']['order_button']:
                send_typing(message)
                bot.send_message(message.from_user.id, text=get_config()['messages']['order_message'], reply_markup=get_keyboard_reply_markup("order_button"))
                send_typing(message)
                bot.send_message(message.from_user.id, text=get_config()['order_data']['ord1'])
                bot.register_next_step_handler(message, get_order_data)
        else:
            pass

        if len(get_config()['buttons']['main_menu_button']) > 0:
            if message.text == get_config()['buttons']['main_menu_button']:
                send_typing(message)
                bot.send_message(message.from_user.id, text=get_config()['messages']['main_menu_msg'], reply_markup=get_keyboard_reply_markup("main_menu_button"))
        else:
            pass

###########################################################################################################################################################
        if len(get_config()['buttons']['btn1']) > 0:
            if message.text == get_config()['buttons']['btn1']:
                send_next_func_after_msg(message, 'btn1', 'msg1')
        else:
            pass

        if len(get_config()['buttons']['btn2']) > 0:
            if message.text == get_config()['buttons']['btn2']:
                send_next_func_after_msg(message, 'btn2', 'msg2')
        else:
            pass

        if len(get_config()['buttons']['btn3']) > 0:
            if message.text == get_config()['buttons']['btn3']:
                send_next_func_after_msg(message, 'btn3', 'msg3')
        else:
            pass

        if len(get_config()['buttons']['btn4']) > 0:
            if message.text == get_config()['buttons']['btn4']:
                send_next_func_after_msg(message, 'btn4', 'msg4')
        else:
            pass

        if len(get_config()['buttons']['btn5']) > 0:
            if message.text == get_config()['buttons']['btn5']:
                send_next_func_after_msg(message, 'btn5', 'msg5')
        else:
            pass

        if len(get_config()['buttons']['btn6']) > 0:
            if message.text == get_config()['buttons']['btn6']:
                send_next_func_after_msg(message, 'btn6', 'msg6')
        else:
            pass

        if len(get_config()['buttons']['btn7']) > 0:
            if message.text == get_config()['buttons']['btn7']:
                send_next_func_after_msg(message, 'btn7', 'msg7')
        else:
            pass

        if len(get_config()['buttons']['btn8']) > 0:
            if message.text == get_config()['buttons']['btn8']:
                send_next_func_after_msg(message, 'btn8', 'msg8')
        else:
            pass

        if len(get_config()['buttons']['btn9']) > 0:
            if message.text == get_config()['buttons']['btn9']:
                send_next_func_after_msg(message, 'btn9', 'msg9')
        else:
            pass

        if len(get_config()['buttons']['btn10']) > 0:
            if message.text == get_config()['buttons']['btn10']:
                send_next_func_after_msg(message, 'btn10', 'msg10')
        else:
            pass

        if len(get_config()['buttons']['btn11']) > 0:
            if message.text == get_config()['buttons']['btn11']:
                send_next_func_after_msg(message, 'btn11', 'msg11')
        else:
            pass

        if len(get_config()['buttons']['btn12']) > 0:
            if message.text == get_config()['buttons']['btn12']:
                send_next_func_after_msg(message, 'btn12', 'msg12')
        else:
            pass

        if len(get_config()['buttons']['btn13']) > 0:
            if message.text == get_config()['buttons']['btn13']:
                send_next_func_after_msg(message, 'btn13', 'msg13')
        else:
            pass

        if len(get_config()['buttons']['btn14']) > 0:
            if message.text == get_config()['buttons']['btn14']:
                send_next_func_after_msg(message, 'btn14', 'msg14')
        else:
            pass

        if len(get_config()['buttons']['btn15']) > 0:
            if message.text == get_config()['buttons']['btn15']:
                send_next_func_after_msg(message, 'btn15', 'msg15')
        else:
            pass

        if len(get_config()['buttons']['btn16']) > 0:
            if message.text == get_config()['buttons']['btn16']:
                send_next_func_after_msg(message, 'btn16', 'msg16')
        else:
            pass

        if len(get_config()['buttons']['btn17']) > 0:
            if message.text == get_config()['buttons']['btn17']:
                send_next_func_after_msg(message, 'btn17', 'msg17')
        else:
            pass

        if len(get_config()['buttons']['btn18']) > 0:
            if message.text == get_config()['buttons']['btn18']:
                send_next_func_after_msg(message, 'btn18', 'msg18')
        else:
            pass

        if len(get_config()['buttons']['btn19']) > 0:
            if message.text == get_config()['buttons']['btn19']:
                send_next_func_after_msg(message, 'btn19', 'msg19')
        else:
            pass

        if len(get_config()['buttons']['btn20']) > 0:
            if message.text == get_config()['buttons']['btn20']:
                send_next_func_after_msg(message, 'btn20', 'msg20')
        else:
            pass


    except Exception as e:
        bot.send_message(message.from_user.id, text=message.text)







# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
# bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
# bot.load_next_step_handlers()

bot.polling(none_stop=False, interval=0, timeout=20)
