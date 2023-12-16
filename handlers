from create_bot import bot, dp

from aiogram.types import ContentType
from googletrans import Translator
from aiogram import types

async def on_startup(dp):
    print("Бот запущен")

@dp.message_handler(commands=["start"])
async def privet(message: types.Message):
    # privet_massage = "Привет! Я бот переводчик"
    await message.reply("Привет! Я бот переводчик")

@dp.message_handler(commands=['help'])
async def on_help(message: types.Message):
    await message.reply("Чем могу помочь?")

@dp.message_handler(content_types=ContentType.TEXT)
async def echo(message: types.Message):
    translator = Translator()
    translation = translator.translate(message.text, dest='en')
    await message.reply(f"Перевод: {translation.text}")


