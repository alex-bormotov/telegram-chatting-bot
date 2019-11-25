import json
from functools import wraps


import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton

from uuid import uuid4



def get_config():
    with open("config.json", "r") as read_file:
        config = json.load(read_file)
        return config


# LIST_OF_ADMINS = [12345678, 87654321]
# def restricted(func):
#     @wraps(func)
#     def wrapped(update, context, *args, **kwargs):
#         user_id = update.effective_user.id
#         if user_id not in LIST_OF_ADMINS:
#             # print("Unauthorized access denied for {}.".format(user_id))
#             context.bot.send_message(
#                 chat_id=LIST_OF_ADMINS[0],
#                 text=("Unauthorized access denied for {}.".format(user_id)),
#             )
#             return
#         return func(update, context, *args, **kwargs)
#
#     return wrapped
#
#
# @restricted
# def secret_resource():
#     print('secret')




# def start(update, context):
#     context.bot.send_message(
#         chat_id=update.effective_chat.id,
#         text=get_config()['messages']['1'],
#     )
#



def start(update, context):
  update.message.reply_text(main_menu_message(),
                            reply_markup=main_menu_keyboard())



def main_menu(update, context):
  query = update.callback_query
  context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())



def first_menu(update, context):
  query = update.callback_query
  context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=first_menu_message(),
                        reply_markup=our_servises_keyboard())






def make_order(update, context):
    query = update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat_id,
                                 message_id=query.message.message_id,
                                 text=make_order_message(),
                                 reply_markup=make_order_keyboard())


def deals(update, context):
    query = update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat_id,
                                 message_id=query.message.message_id,
                                 text=deals_message(),
                                 reply_markup=our_servises_keyboard())


def seasons(update, context):
    query = update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat_id,
                                 message_id=query.message.message_id,
                                 text=seasons_message(),
                                 reply_markup=our_servises_keyboard())


def extra_deals(update, context):
    query = update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id,
                                  text=extra_deals_message(),
                                  reply_markup=our_servises_keyboard())



def birthday_in_cafe(update, context):
    query = update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat_id,
                                 message_id=query.message.message_id,
                                 text=birthday_in_cafe_message(),
                                 reply_markup=send_order_keyboard())


def birthday_in_studio(update, context):
    query = update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat_id,
                                 message_id=query.message.message_id,
                                 text=birthday_in_studio_message(),
                                 reply_markup=send_order_keyboard())










def send_order(update, context):
    query = update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat_id,
                                 message_id=query.message.message_id,
                                 text=send_order_message(context))



def contact_us(update, context):

    # context.bot.send_message(chat_id=update.effective_chat.id, text="Как Вас зовут?")
    # name = " ".join(context.args)

    # context.bot.send_message(chat_id=update.effective_chat.id, text=f"{name}")

    # update.message.reply_text(get_config()['messages']['4'])

    # query = update.callback_query
    #
    # query.edit_message_text(text="{}".format(query.data))

    update.message.reply_text(update.message.text)

    context.bot.send_message(chat_id=update.effective_chat.id, text=get_config()['messages']['4'])

    # updater.bot.reply_text(chat_id=update.effective_chat.id, text=context.args)

         # updater.bot.send_message(chat_id=LIST_OF_ADMINS[0], text=str(e))


############################ Keyboards #########################################

def main_menu_keyboard():
        keyboard = [[InlineKeyboardButton(get_config()['buttons']['2'], callback_data='our_servises')],
                    [InlineKeyboardButton(get_config()['buttons']['3'], callback_data='make_order')],
                    [InlineKeyboardButton(get_config()['buttons']['4'], callback_data='contact_us')]]
        return InlineKeyboardMarkup(keyboard)



def our_servises_keyboard():
        keyboard = [[InlineKeyboardButton(get_config()['buttons']['5'], callback_data='deals')],
                    [InlineKeyboardButton(get_config()['buttons']['6'], callback_data='seasons')],
                    [InlineKeyboardButton(get_config()['buttons']['7'], callback_data='extra_deals')],
                    [InlineKeyboardButton('Main menu', callback_data='main')]]
        return InlineKeyboardMarkup(keyboard)



def make_order_keyboard():
        keyboard = [[InlineKeyboardButton(get_config()['buttons']['8'], callback_data='birthday_in_cafe')],
                    [InlineKeyboardButton(get_config()['buttons']['9'], callback_data='birthday_in_studio')],
                    [InlineKeyboardButton(get_config()['buttons']['10'], callback_data='contact_us')],
                    [InlineKeyboardButton('Main menu', callback_data='main')]]
        return InlineKeyboardMarkup(keyboard)



def send_order_keyboard():
         keyboard = [[InlineKeyboardButton(get_config()['buttons']['11'], callback_data='send_order')],
                     [InlineKeyboardButton('Main menu', callback_data='main')]]
         return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def main_menu_message():
        return get_config()['messages']['1']


def first_menu_message():
        return get_config()['messages']['2']


def make_order_message():
        return get_config()['messages']['3']


def deals_message():
        return get_config()['messages']['5']


def seasons_message():
        return get_config()['messages']['6']


def extra_deals_message():
        return get_config()['messages']['7']


def birthday_in_cafe_message():
        return get_config()['messages']['8']


def birthday_in_studio_message():
        return get_config()['messages']['9']


# def put(update, context):
#     """Usage: /put value"""
#     # Generate ID and seperate value from command
#     key = str(uuid4())
#     value = update.message.text.partition(' ')[2]
#
#     # Store value
#     context.user_data[key] = value
#
#     update.message.reply_text(key)
#
# def get(update, context):
#     """Usage: /get uuid"""
#     # Seperate ID from command
#     key = update.message.text.partition(' ')[2]
#
#     # Load value
#     try:
#         value = context.user_data[key]
#         update.message.reply_text(value)
#
#     except KeyError:
#         update.message.reply_text('Not found')



############################# Handlers #########################################
if __name__ == "__main__":

        bot=telegram.Bot(get_config()["telegram_bot_token"])
        updater = Updater(get_config()["telegram_bot_token"], use_context=True)

        updater.dispatcher.add_handler(CommandHandler('start', start))

        updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
        updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='our_servises'))
        updater.dispatcher.add_handler(CallbackQueryHandler(make_order, pattern='make_order'))
        updater.dispatcher.add_handler(CallbackQueryHandler(deals, pattern='deals'))
        updater.dispatcher.add_handler(CallbackQueryHandler(seasons, pattern='seasons'))
        updater.dispatcher.add_handler(CallbackQueryHandler(extra_deals, pattern='extra_deals'))
        updater.dispatcher.add_handler(CallbackQueryHandler(birthday_in_cafe, pattern='birthday_in_cafe'))
        updater.dispatcher.add_handler(CallbackQueryHandler(birthday_in_studio, pattern='birthday_in_studio'))




        updater.dispatcher.add_handler(CallbackQueryHandler(contact_us, pattern='contact_us'))
        updater.dispatcher.add_handler(CallbackQueryHandler(send_order, pattern='send_order'))

        updater.dispatcher.add_handler(MessageHandler(Filters.text, contact_us))


        updater.start_polling()
        # updater.idle()
