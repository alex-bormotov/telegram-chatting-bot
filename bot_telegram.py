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
    button_a = types.KeyboardButton(get_config()['buttons']['btn2'])
    button_b = types.KeyboardButton(get_config()['buttons']['btn3'])
    button_c = types.KeyboardButton(get_config()['buttons']['contact_button'])
    markup.row(button_a)
    markup.row(button_b)
    markup.row(button_c)
    # markup.row(button_a, button_b, button_c)
    # markup.row(itembtnc, itembtnd, itembtne)
    return markup


def keyboard_2():
    markup = types.ReplyKeyboardMarkup()
    button_a = types.KeyboardButton(get_config()['buttons']['btn5'])
    button_b = types.KeyboardButton(get_config()['buttons']['btn6'])
    button_c = types.KeyboardButton(get_config()['buttons']['btn7'])
    button_d = types.KeyboardButton(get_config()['buttons']['btn12'])
    markup.row(button_a)
    markup.row(button_b)
    markup.row(button_c)
    markup.row(button_d)
    # markup.row(button_a, button_b, button_c)
    # markup.row(itembtnc, itembtnd, itembtne)
    return markup


def keyboard_3():
    markup = types.ReplyKeyboardMarkup()
    button_a = types.KeyboardButton(get_config()['buttons']['btn8'])
    button_b = types.KeyboardButton(get_config()['buttons']['btn9'])
    button_c = types.KeyboardButton(get_config()['buttons']['btn10'])
    button_d = types.KeyboardButton(get_config()['buttons']['btn12'])
    markup.row(button_a)
    markup.row(button_b)
    markup.row(button_c)
    markup.row(button_d)
    # markup.row(button_a, button_b, button_c)
    # markup.row(itembtnc, itembtnd, itembtne)
    return markup


def keyboard_4():
    markup = types.ReplyKeyboardMarkup()
    # button_a = types.KeyboardButton(get_config()['buttons']['contact_button'])
    button_b = types.KeyboardButton(get_config()['buttons']['btn13'])
    # markup.row(button_a)
    markup.row(button_b)
    # markup = types.ReplyKeyboardRemove(selective=True)
    return markup


def keyboard_5():
    markup = types.ReplyKeyboardMarkup()
    button_a = types.KeyboardButton(get_config()['buttons']['contact_button'])
    button_b = types.KeyboardButton(get_config()['buttons']['order_button'])
    button_c = types.KeyboardButton(get_config()['buttons']['btn12'])
    markup.row(button_a, button_b)
    markup.row(button_c)
    return markup



def keyboard_6():
    markup = types.ReplyKeyboardMarkup()
    button_a = types.KeyboardButton(get_config()['buttons']['btn13'])
    markup.row(button_a)
    # markup = types.ReplyKeyboardRemove(selective=True)
    return markup



def cancel(message):
    bot.send_message(message.from_user.id, text=get_config()['messages']['msg1'], reply_markup=keyboard_1())

############### Name and Phone #####################################################
def get_user_name(message):
    if message.text == get_config()['buttons']['btn13']:
        bot.send_message(message.from_user.id, text=get_config()['buttons']['cancel'])
        bot.register_next_step_handler(message, cancel)
    else:
        name = message.text
        bot.send_message(message.from_user.id, text=get_config()['add_vars']['adv3'])
        bot.register_next_step_handler(message, get_user_phone, name)


def get_user_phone(message, name):
    phone = message.text
    bot.send_message(message.from_user.id, text=f"{get_config()['add_vars']['adv1']}: {name}\n{get_config()['add_vars']['adv2']}: {phone}", reply_markup=keyboard_1())
    # bot.send_message(931750534, text=f"{name} {phone}", reply_markup=keyboard_1())



############# Order data ######################################################
def get_order_data(message):
    if message.text == get_config()['buttons']['btn13']:
        bot.send_message(message.from_user.id, text=get_config()['buttons']['cancel'])
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
    bot.send_message(message.from_user.id, text=f"{one}\n{two}\n{three}\n{four}\n{five}\n{six}\n{seven}\n{eight}\n{nine}", reply_markup=keyboard_1())
    # bot.send_message(931750534, text=f"{one}\n{two}\n{three}\n{four}\n{five}\n{six}\n{seven}\n{eight}\n{nine}", reply_markup=keyboard_1())





@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, text=get_config()['messages']['msg1'], reply_markup=keyboard_1())
    # bot.register_next_step_handler(message, handler)



@bot.message_handler(content_types=["text"])
def handler(message):
    try:
        if len(get_config()['buttons']['btn1']) > 0:
            if message.text == get_config()['buttons']['btn1']:
                bot.send_message(message.from_user.id, text=get_config()['messages']['msg1'], reply_markup=keyboard_2())
        else:
            pass

        if len(get_config()['buttons']['btn2']) > 0:
            if message.text == get_config()['buttons']['btn2']:
                bot.send_message(message.from_user.id, text=get_config()['messages']['msg2'], reply_markup=keyboard_2())
        else:
            pass
        if len(get_config()['buttons']['btn3']) > 0:
            if message.text == get_config()['buttons']['btn3']:
                bot.send_message(message.from_user.id, text=get_config()['messages']['msg3'], reply_markup=keyboard_3())
        else:
            pass

        if len(get_config()['buttons']['contact_button']) > 0:
            if message.text == get_config()['buttons']['contact_button']:
                bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=keyboard_4())
                bot.register_next_step_handler(message, get_user_name)
        else:
            pass

        if len(get_config()['buttons']['btn5']) > 0:
            if message.text == get_config()['buttons']['btn5']:
                bot.send_message(message.from_user.id, text=get_config()['messages']['msg5'], reply_markup=keyboard_5())
        else:
            pass

        if len(get_config()['buttons']['btn6']) > 0:
            if message.text == get_config()['buttons']['btn6']:
                bot.send_message(message.from_user.id, text=get_config()['messages']['msg6'], reply_markup=keyboard_4())
                bot.register_next_step_handler(message, get_user_name)
        else:
            pass

        if len(get_config()['buttons']['btn7']) > 0:
            if message.text == get_config()['buttons']['btn7']:
                bot.send_message(message.from_user.id, text=get_config()['messages']['msg7'], reply_markup=keyboard_5())
        else:
            pass

        if len(get_config()['buttons']['btn8']) > 0:
            if message.text == get_config()['buttons']['btn8']:
                bot.send_message(message.from_user.id, text=get_config()['messages']['msg8'], reply_markup=keyboard_5())
        else:
            pass

        if len(get_config()['buttons']['btn9']) > 0:
            if message.text == get_config()['buttons']['btn9']:
                bot.send_message(message.from_user.id, text=get_config()['messages']['msg9'], reply_markup=keyboard_5())
        else:
            pass

        if len(get_config()['buttons']['btn10']) > 0:
            if message.text == get_config()['buttons']['btn10']:
                bot.send_message(message.from_user.id, text=get_config()['messages']['contact_message'], reply_markup=keyboard_4())
                bot.register_next_step_handler(message, get_user_name)
        else:
            pass

        if len(get_config()['buttons']['order_button']) > 0:
            if message.text == get_config()['buttons']['order_button']:
                bot.send_message(message.from_user.id, text=get_config()['messages']['order_message'], reply_markup=keyboard_6())
                bot.send_message(message.from_user.id, text=get_config()['order_data']['ord1'])
                bot.register_next_step_handler(message, get_order_data)
        else:
            pass

        if len(get_config()['buttons']['btn12']) > 0:
            if message.text == get_config()['buttons']['btn12']:
                bot.send_message(message.from_user.id, text=get_config()['buttons']['btn12'], reply_markup=keyboard_1())
        else:
            pass

        if len(get_config()['buttons']['btn13']) > 0:
            if message.text == get_config()['buttons']['btn13']:
                bot.send_message(message.from_user.id, text=get_config()['buttons']['btn13'], reply_markup=keyboard_1())
        else:
            pass

        if len(get_config()['buttons']['btn14']) > 0:
            if message.text == get_config()['buttons']['btn14']:
                bot.send_message(message.from_user.id, text=get_config()['buttons']['btn14'], reply_markup=keyboard_1())
        else:
            pass

        if len(get_config()['buttons']['btn15']) > 0:
            if message.text == get_config()['buttons']['btn15']:
                bot.send_message(message.from_user.id, text=get_config()['buttons']['btn15'], reply_markup=keyboard_1())
        else:
            pass

        if len(get_config()['buttons']['btn16']) > 0:
            if message.text == get_config()['buttons']['btn16']:
                bot.send_message(message.from_user.id, text=get_config()['buttons']['btn16'], reply_markup=keyboard_1())
        else:
            pass

        if len(get_config()['buttons']['btn17']) > 0:
            if message.text == get_config()['buttons']['btn17']:
                bot.send_message(message.from_user.id, text=get_config()['buttons']['btn17'], reply_markup=keyboard_1())
        else:
            pass

        if len(get_config()['buttons']['btn18']) > 0:
            if message.text == get_config()['buttons']['btn18']:
                bot.send_message(message.from_user.id, text=get_config()['buttons']['btn18'], reply_markup=keyboard_1())
        else:
            pass

        if len(get_config()['buttons']['btn19']) > 0:
            if message.text == get_config()['buttons']['btn19']:
                bot.send_message(message.from_user.id, text=get_config()['buttons']['btn19'], reply_markup=keyboard_1())
        else:
            pass

        if len(get_config()['buttons']['btn20']) > 0:
            if message.text == get_config()['buttons']['btn20']:
                bot.send_message(message.from_user.id, text=get_config()['buttons']['btn20'], reply_markup=keyboard_1())
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
