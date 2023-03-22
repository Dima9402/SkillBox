import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.dispatcher.filters import Command
from TOKEN import TOKEN_API
from excel_reader import read_excel


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)

# Создаем папку для сохранения документов, если ее нет
if not os.path.exists("documents"):
    os.makedirs("documents")


# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Загрузите Excel-документ, чтобы начать работу с ботом.")

# Обработчик входящих документов
@dp.message_handler(content_types=['document'])
async def handle_document(message: types.Message):
    # Загрузить документ
    file = await message.document.download()
    file_name = message.document.file_name

    # Сохраняем документ в папку
    file_path = f"documents/{file_name}"
    os.replace(file.name, file_path)

    # Прочитать данные из Excel-документа
    response = read_excel(file.path)

    # Отправить сообщение с данными
    await message.reply(response)






if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)