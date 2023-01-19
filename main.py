import os
import logging

from aiogram import Bot, Dispatcher, executor, types
import aiohttp
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv('TELEGRAM_TOKEN')
PROXY_URL = os.getenv('TELEGRAM_URL')
ID_USER = 331891251

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def auth(func):
    async def wrapper(message):
        if message['from']['id'] != ID_USER:
            return await message.reply('Access Denied', reply=False)
        return await func(message)
    return wrapper


@dp.message_handler(commands=['start', 'help'])
@auth
async def send_welcome(message: types.Message):
    await message.reply(
        'Бот для учета финансов\n\n'
        'Добавить расход: 250 такси\n'
        'Сегодняшняя статистика: /today\n'
        'За текущий месяц: /month\n'
        'Последние внесенные расходы: /expenses\n'
        'Категории трат: /categories',
        reply=False
    )
