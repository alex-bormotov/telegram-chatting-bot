import telebot
from telebot import types
from config import get_telegram_config
from email_send import send_email


# https://github.com/python-telegram-bot/python-telegram-bot
bot = telebot.TeleBot(get_telegram_config()["telegram_bot_token"])


def send_typing(message):
    bot.send_chat_action(message.from_user.id, "typing")
    # sendChatAction
    # action_string can be one of the following strings: 'typing', 'upload_photo', 'record_video', 'upload_video',
    # 'record_audio', 'upload_audio', 'upload_document' or 'find_location'.
    # bot.send_chat_action(chat_id, action_string)


def send_typing_image(message):
    bot.send_chat_action(message.from_user.id, "upload_photo")


def send_typing_audio(message):
    bot.send_chat_action(message.from_user.id, "record_audio")


def send_typing_video(message):
    bot.send_chat_action(message.from_user.id, "upload_video")


############### Keyboards #####################################################


def get_keyboard_reply_markup(btn):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button_a = ""
    button_b = ""
    button_c = ""
    button_d = ""
    button_e = ""

    if (
        len(
            get_telegram_config()["keyboards"][
                f"keyboard_{get_telegram_config()['button_belong_keyboard'][btn][9:]}_btn_1"
            ]
        )
        > 0
    ):
        btns_btn_a = get_telegram_config()["keyboards"][
            f"keyboard_{get_telegram_config()['button_belong_keyboard'][btn][9:]}_btn_1"
        ]
        button_a = types.KeyboardButton(get_telegram_config()["buttons"][btns_btn_a])
    else:
        pass
    if (
        len(
            get_telegram_config()["keyboards"][
                f"keyboard_{get_telegram_config()['button_belong_keyboard'][btn][9:]}_btn_2"
            ]
        )
        > 0
    ):
        btns_btn_b = get_telegram_config()["keyboards"][
            f"keyboard_{get_telegram_config()['button_belong_keyboard'][btn][9:]}_btn_2"
        ]
        button_b = types.KeyboardButton(get_telegram_config()["buttons"][btns_btn_b])
    else:
        pass
    if (
        len(
            get_telegram_config()["keyboards"][
                f"keyboard_{get_telegram_config()['button_belong_keyboard'][btn][9:]}_btn_3"
            ]
        )
        > 0
    ):
        btns_btn_c = get_telegram_config()["keyboards"][
            f"keyboard_{get_telegram_config()['button_belong_keyboard'][btn][9:]}_btn_3"
        ]
        button_c = types.KeyboardButton(get_telegram_config()["buttons"][btns_btn_c])
    else:
        pass
    if (
        len(
            get_telegram_config()["keyboards"][
                f"keyboard_{get_telegram_config()['button_belong_keyboard'][btn][9:]}_btn_4"
            ]
        )
        > 0
    ):
        btns_btn_d = get_telegram_config()["keyboards"][
            f"keyboard_{get_telegram_config()['button_belong_keyboard'][btn][9:]}_btn_4"
        ]
        button_d = types.KeyboardButton(get_telegram_config()["buttons"][btns_btn_d])
    else:
        pass
    if (
        len(
            get_telegram_config()["keyboards"][
                f"keyboard_{get_telegram_config()['button_belong_keyboard'][btn][9:]}_btn_5"
            ]
        )
        > 0
    ):
        btns_btn_e = get_telegram_config()["keyboards"][
            f"keyboard_{get_telegram_config()['button_belong_keyboard'][btn][9:]}_btn_5"
        ]
        button_e = types.KeyboardButton(get_telegram_config()["buttons"][btns_btn_e])
    else:
        pass
    markup.row(button_a, button_b)
    markup.row(button_c, button_d, button_e)
    # if (
    #     get_telegram_config()["keyboards"][
    #         f"keyboard_{keyboard_number}_ReplyKeyboardRemove"
    #     ]
    #     == "True"
    # ):
    #     markup = types.ReplyKeyboardRemove(selective=True)
    return markup


############# Order and Contact ##############################################################################################################################
curent_step = 0


def get_step(question_form):
    global curent_step

    total_steps = int(
        [k[9:] for k, v in get_telegram_config()[question_form].items()][-1]
    )
    if curent_step <= total_steps:

        steps = (
            [k for k, v in get_telegram_config()[question_form].items()][curent_step],
            total_steps,
        )
        curent_step += 1
        if curent_step == total_steps:
            curent_step = 0
    return steps


answers_question_form_2 = []
question_form_2_count = 1


def question_form_2(message):
    global answers_question_form_2
    global question_form_2_count

    if (
        message.text
        == get_telegram_config()["buttons"][
            get_telegram_config()["built_in"]["cancel_button"]
        ]
    ):
        send_typing(message)
        bot.send_message(
            message.from_user.id,
            text=get_telegram_config()["built_in"]["cancel_message"],
            reply_markup=get_keyboard_reply_markup(
                get_telegram_config()["built_in"]["main_keyboard"]
            ),
        )
        bot.register_next_step_handler(message, cancel)
    else:
        send_typing(message)
        data = get_step("question_form_2")
        question_form_2_count += 1
        if question_form_2_count <= data[1]:
            bot.send_message(
                message.from_user.id,
                text=get_telegram_config()["question_form_2"][data[0]],
            )
            answers_question_form_2.append(message.text)
            bot.register_next_step_handler(message, question_form_2)
        else:
            bot.send_message(
                message.from_user.id,
                text=get_telegram_config()["built_in"]["thanks_question_form_2"],
                reply_markup=get_keyboard_reply_markup(
                    get_telegram_config()["built_in"]["main_keyboard"]
                ),
            )
            answers_question_form_2.remove(answers_question_form_2[0])
            send_email(str(answers_question_form_2))
            answers_question_form_2 = []
            question_form_2_count = 1
            bot.register_next_step_handler(message, handler)


answers_question_form_1 = []
question_form_1_count = 1


def question_form_1(message):
    global answers_question_form_1
    global question_form_1_count

    if (
        message.text
        == get_telegram_config()["buttons"][
            get_telegram_config()["built_in"]["cancel_button"]
        ]
    ):
        send_typing(message)
        bot.send_message(
            message.from_user.id,
            text=get_telegram_config()["built_in"]["cancel_message"],
            reply_markup=get_keyboard_reply_markup(
                get_telegram_config()["built_in"]["main_keyboard"]
            ),
        )
        bot.register_next_step_handler(message, cancel)
    else:
        send_typing(message)
        data = get_step("question_form_1")
        question_form_1_count += 1
        if question_form_1_count <= data[1]:
            bot.send_message(
                message.from_user.id,
                text=get_telegram_config()["question_form_1"][data[0]],
            )
            answers_question_form_1.append(message.text)
            bot.register_next_step_handler(message, question_form_1)
        else:
            bot.send_message(
                message.from_user.id,
                text=get_telegram_config()["built_in"]["thanks_question_form_1"],
                reply_markup=get_keyboard_reply_markup(
                    get_telegram_config()["built_in"]["main_keyboard"]
                ),
            )
            answers_question_form_1.remove(answers_question_form_1[0])
            send_email(str(answers_question_form_1))
            answers_question_form_1 = []
            question_form_1_count = 1
            bot.register_next_step_handler(message, handler)


####################   Cancel Button  ###############################################################################################################


def cancel(message):
    send_typing(message)
    bot.send_message(
        message.from_user.id,
        text=get_telegram_config()["built_in"]["main_menu_message"],
        reply_markup=get_keyboard_reply_markup(
            get_telegram_config()["built_in"]["main_menu"]
        ),
    )


################ Media Buttons #########################################################################################################################

# https://github.com/eternnoir/pyTelegramBotAPI#telebot


def send_image(message):
    send_typing_image(message)
    photo = open("media_samples/image.jpg", "rb")
    bot.send_photo(
        message.from_user.id,
        photo,
        reply_markup=get_keyboard_reply_markup(
            get_telegram_config()["built_in"]["main_keyboard"]
        ),
    )


def send_video(message):
    send_typing_video(message)
    video = open("media_samples/video.mp4", "rb")
    bot.send_video(
        message.from_user.id,
        video,
        reply_markup=get_keyboard_reply_markup(
            get_telegram_config()["built_in"]["main_keyboard"]
        ),
    )


def send_audio(message):
    send_typing_audio(message)
    audio = open("media_samples/audio.mp3", "rb")
    bot.send_audio(
        message.from_user.id,
        audio,
        reply_markup=get_keyboard_reply_markup(
            get_telegram_config()["built_in"]["main_keyboard"]
        ),
    )


###########################################################################################################################################################


@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    send_typing(message)
    bot.send_message(
        message.from_user.id,
        text=get_telegram_config()["built_in"]["main_menu_message"],
        reply_markup=get_keyboard_reply_markup(
            get_telegram_config()["built_in"]["main_menu"]
        ),
    )


@bot.message_handler(content_types=["text"])
def handler(message):
    try:
        if message.text in [v for v in get_telegram_config()["buttons"].values()]:
            btn = [
                k
                for k, v in get_telegram_config()["buttons"].items()
                if message.text == v
            ][0]
            msg_content = get_telegram_config()["messages"][f"msg{btn[3:]}"]

            if type(msg_content) is str:
                msg = msg_content
                send_typing(message)
                bot.send_message(
                    message.from_user.id,
                    text=msg,
                    reply_markup=get_keyboard_reply_markup(btn),
                )
            if type(msg_content) is list:
                func = eval(msg_content[0])
                msg = msg_content[1]
                bot.send_message(
                    message.from_user.id,
                    text=msg,
                    reply_markup=get_keyboard_reply_markup(btn),
                )
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

bot.polling(none_stop=False, interval=0, timeout=2)
