import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command
import config


dp = Dispatcher()

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f"Hello, {message.from_user.full_name}!")

@dp.message(Command("help"))
async def handel_help(message: types.Message):
    text = "I`m echo bot.\nSend me any message!"
    await message.answer(text=text)
@dp.message()
async def echo_message(message: types.Message):
    #await bot.send_message(
    #    chat_id=message.chat.id,
    #    text="Start processing...",
    #)
    #await bot.send_message(
    #    chat_id=message.chat.id,
    #    text="Wait a second...",
    #    reply_to_message_id=message.message_id,
    #)
    await message.answer(
        text="Detected message...",
    )
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Something new")
    await message.reply(text=message.text)
async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())