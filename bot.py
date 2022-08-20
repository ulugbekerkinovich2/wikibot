import logging

import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5680080868:AAH5oDC1biXf2bnJ-Eh0GOp7OMWt8PjLNdc'
wikipedia.set_lang('uz')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("salom bu bot yaratilmoqda.")


@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("bu mavzuga oid maqola yoq")


@dp.message_handler(commands=['chat_id'])
async def get_chat_id(self, message: types.Message):
    '''
    Telegram chat type can be either "private", "group", "supergroup" or
    "channel".
    Return user ID if it is of type "private", chat ID otherwise.
    '''
    if message.chat.type == 'private':
        return message.user.id

    return message.chat.id


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
