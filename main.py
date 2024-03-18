import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, F
from aiogram.client import bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BotCommand
from root import TOKEN
from buttons import *

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hi bro! Bot now working!", reply_markup=kirish1_set)


@dp.message(F.text == "Golds")
async def golds(message: Message):
    await message.answer("Siz Golds bo'limiga kirdingiz!", reply_markup=golds_set)

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)
    await bot.set_my_commands([
        BotCommand(command="botni ishga tushirish!", description="start"),
        BotCommand(command="foydalanuvchiga yordam berish!", description="help"),
        BotCommand(command="foydalanuvchini kanalga olib kiradi!", description="silka")])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
