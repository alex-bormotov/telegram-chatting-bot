import json

import telebot
from telebot import types


def get_config():
    with open("config.json", "r") as read_file:
        config = json.load(read_file)
        return config

bot = telebot.TeleBot(get_config()["telegram_bot_token"])


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
    bot.send_message(message.from_user.id, text=get_config()['messages']['msg1'], reply_markup=get_keyboard_reply_markup('main_menu_button'))

############### Name and Phone #####################################################
def get_user_name(message):
    if message.text == get_config()['buttons']['cancel_button']:
        bot.send_message(message.from_user.id, text=get_config()['messages']['cancel_message'])
        bot.register_next_step_handler(message, cancel)
    else:
        name = message.text
        bot.send_message(message.from_user.id, text=f"{get_config()['add_vars']['phone']} ?")
        bot.register_next_step_handler(message, get_user_phone, name)


def get_user_phone(message, name):
    phone = message.text
    bot.send_message(message.from_user.id, text=f"{get_config()['add_vars']['name']}: {name}\n{get_config()['add_vars']['phone']}: {phone}", reply_markup=get_keyboard_reply_markup('main_menu_button'))
    # bot.send_message(931750534, text=f"{name} {phone}", reply_markup=get_keyboard_reply_markup('main_menu_button'))



############# Order data ######################################################
def get_order_data(message):
    if message.text == get_config()['buttons']['cancel_button']:
        bot.send_message(message.from_user.id, text=get_config()['messages']['cancel_message'])
        bot.register_next_step_handler(message, cancel)
    else:
        one = message.text
        bot.send_message(message.from_user.id, text=get_config()['order_data']['ord2'])
        bot.register_next_step_handler(message, get_order_data_1, one)


def get_order_data_1(message, one):
    two = message.text
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord3'])
    bot.register_next_step_handler(message, get_order_data_2, one, two)

def get_order_data_2(message, one, two):
    three = message.text
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord4'])
    bot.register_next_step_handler(message, get_order_data_3, one, two, three)


def get_order_data_3(message, one, two, three):
    four = message.text
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord5'])
    bot.register_next_step_handler(message, get_order_data_4, one, two, three, four)


def get_order_data_4(message, one, two, three, four):
    five = message.text
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord6'])
    bot.register_next_step_handler(message, get_order_data_5, one, two, three, four, five)


def get_order_data_5(message, one, two, three, four, five):
    six = message.text
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord7'])
    bot.register_next_step_handler(message, get_order_data_6, one, two, three, four, five, six)


def get_order_data_6(message, one, two, three, four, five, six):
    seven = message.text
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord8'])
    bot.register_next_step_handler(message, get_order_data_7, one, two, three, four, five, six, seven)


def get_order_data_7(message, one, two, three, four, five, six, seven):
    eight = message.text
    bot.send_message(message.from_user.id, text=get_config()['order_data']['ord9'])
    bot.register_next_step_handler(message, get_order_data_8, one, two, three, four, five, six, seven, eight)


def get_order_data_8(message, one, two, three, four, five, six, seven, eight):
    nine = message.text
    bot.send_message(message.from_user.id, text=get_config()['messages']['after_order_message'], reply_markup=get_keyboard_reply_markup('main_menu_button'))
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


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, text=get_config()['messages']['msg1'], reply_markup=get_keyboard_reply_markup('main_menu_button'))
    # bot.register_next_step_handler(message, handler)



@bot.message_handler(content_types=["text"])
def handler(message):
    try:
###########################################################################################################################################################

        if len(get_config()['buttons']['contact_button']) > 0:
            if message.text == get_config()['buttons']['contact_button']:
                bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                bot.register_next_step_handler(message, get_user_name)
        else:
            pass


        if len(get_config()['buttons']['order_button']) > 0:
            if message.text == get_config()['buttons']['order_button']:
                bot.send_message(message.from_user.id, text=get_config()['messages']['order_message'], reply_markup=get_keyboard_reply_markup("order_button"))
                bot.send_message(message.from_user.id, text=get_config()['order_data']['ord1'])
                bot.register_next_step_handler(message, get_order_data)
        else:
            pass

        if len(get_config()['buttons']['main_menu_button']) > 0:
            if message.text == get_config()['buttons']['main_menu_button']:
                bot.send_message(message.from_user.id, text=get_config()['messages']['main_menu_msg'], reply_markup=get_keyboard_reply_markup("main_menu_button"))
        else:
            pass

###########################################################################################################################################################
        if len(get_config()['buttons']['btn1']) > 0:
            if message.text == get_config()['buttons']['btn1']:
                if get_config()['btn_call_contact_form_after']['btn1'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg1'], reply_markup=get_keyboard_reply_markup("btn1"))
        else:
            pass

        if len(get_config()['buttons']['btn2']) > 0:
            if message.text == get_config()['buttons']['btn2']:
                if get_config()['btn_call_contact_form_after']['btn2'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg2'], reply_markup=get_keyboard_reply_markup("btn2"))
        else:
            pass

        if len(get_config()['buttons']['btn3']) > 0:
            if message.text == get_config()['buttons']['btn3']:
                if get_config()['btn_call_contact_form_after']['btn3'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg3'], reply_markup=get_keyboard_reply_markup("btn3"))
        else:
            pass

        if len(get_config()['buttons']['btn4']) > 0:
            if message.text == get_config()['buttons']['btn4']:
                if get_config()['btn_call_contact_form_after']['btn4'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg4'], reply_markup=get_keyboard_reply_markup("btn4"))
        else:
            pass

        if len(get_config()['buttons']['btn5']) > 0:
            if message.text == get_config()['buttons']['btn5']:
                if get_config()['btn_call_contact_form_after']['btn5'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg5'], reply_markup=get_keyboard_reply_markup("btn5"))
        else:
            pass

        if len(get_config()['buttons']['btn6']) > 0:
            if message.text == get_config()['buttons']['btn6']:
                if get_config()['btn_call_contact_form_after']['btn6'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg6'], reply_markup=get_keyboard_reply_markup("btn6"))
        else:
            pass

        if len(get_config()['buttons']['btn7']) > 0:
            if message.text == get_config()['buttons']['btn7']:
                if get_config()['btn_call_contact_form_after']['btn7'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg7'], reply_markup=get_keyboard_reply_markup("btn7"))
        else:
            pass

        if len(get_config()['buttons']['btn8']) > 0:
            if message.text == get_config()['buttons']['btn8']:
                if get_config()['btn_call_contact_form_after']['btn8'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg8'], reply_markup=get_keyboard_reply_markup("btn8"))
        else:
            pass

        if len(get_config()['buttons']['btn9']) > 0:
            if message.text == get_config()['buttons']['btn9']:
                if get_config()['btn_call_contact_form_after']['btn9'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg9'], reply_markup=get_keyboard_reply_markup("btn9"))
        else:
            pass

        if len(get_config()['buttons']['btn10']) > 0:
            if message.text == get_config()['buttons']['btn10']:
                if get_config()['btn_call_contact_form_after']['btn10'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg10'], reply_markup=get_keyboard_reply_markup("btn10"))
        else:
            pass

        if len(get_config()['buttons']['btn11']) > 0:
            if message.text == get_config()['buttons']['btn11']:
                if get_config()['btn_call_contact_form_after']['btn11'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg11'], reply_markup=get_keyboard_reply_markup("btn11"))
        else:
            pass

        if len(get_config()['buttons']['btn12']) > 0:
            if message.text == get_config()['buttons']['btn12']:
                if get_config()['btn_call_contact_form_after']['btn12'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg12'], reply_markup=get_keyboard_reply_markup("btn12"))
        else:
            pass

        if len(get_config()['buttons']['btn13']) > 0:
            if message.text == get_config()['buttons']['btn13']:
                if get_config()['btn_call_contact_form_after']['btn13'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg13'], reply_markup=get_keyboard_reply_markup("btn13"))
        else:
            pass

        if len(get_config()['buttons']['btn14']) > 0:
            if message.text == get_config()['buttons']['btn14']:
                if get_config()['btn_call_contact_form_after']['btn14'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg14'], reply_markup=get_keyboard_reply_markup("btn14"))
        else:
            pass

        if len(get_config()['buttons']['btn15']) > 0:
            if message.text == get_config()['buttons']['btn15']:
                if get_config()['btn_call_contact_form_after']['btn15'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg15'], reply_markup=get_keyboard_reply_markup("btn15"))
        else:
            pass

        if len(get_config()['buttons']['btn16']) > 0:
            if message.text == get_config()['buttons']['btn16']:
                if get_config()['btn_call_contact_form_after']['btn16'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg16'], reply_markup=get_keyboard_reply_markup("btn16"))
        else:
            pass

        if len(get_config()['buttons']['btn17']) > 0:
            if message.text == get_config()['buttons']['btn17']:
                if get_config()['btn_call_contact_form_after']['btn17'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg17'], reply_markup=get_keyboard_reply_markup("btn17"))
        else:
            pass

        if len(get_config()['buttons']['btn18']) > 0:
            if message.text == get_config()['buttons']['btn18']:
                if get_config()['btn_call_contact_form_after']['btn18'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg18'], reply_markup=get_keyboard_reply_markup("btn18"))
        else:
            pass

        if len(get_config()['buttons']['btn19']) > 0:
            if message.text == get_config()['buttons']['btn19']:
                if get_config()['btn_call_contact_form_after']['btn19'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg19'], reply_markup=get_keyboard_reply_markup("btn19"))
        else:
            pass

        if len(get_config()['buttons']['btn20']) > 0:
            if message.text == get_config()['buttons']['btn20']:
                if get_config()['btn_call_contact_form_after']['btn20'] == "True":
                    bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=get_keyboard_reply_markup("contact_button"))
                    bot.register_next_step_handler(message, get_user_name)
                else:
                    bot.send_message(message.from_user.id, text=get_config()['messages']['msg20'], reply_markup=get_keyboard_reply_markup("btn20"))
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

bot.polling()
