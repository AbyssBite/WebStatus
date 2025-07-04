import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from config import BOT_TOKEN, ADMIN_IDS

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    if message.from_user.id in ADMIN_IDS:
        await message.answer("👑 Welcome, Admin! Use /help to manage your settings.")
    else:
        await message.answer(
            "✅ Welcome! This bot monitors website status. Stay tuned."
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
