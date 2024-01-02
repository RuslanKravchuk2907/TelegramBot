import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types


TOKEN = "6750867931:AAG5s9jlEZOkp6y45bvh7V6QK5YqWud_Nks"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message()
async def echo_message(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Start processing...",
    )
    await bot.send_message(
        chat_id=message.chat.id,
        text="Wait a second...",
        reply_to_message_id=message.message_id,
    )
    await message.answer(
        text="Detected message...",
    )
    await message.reply(text=message.text)
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())