import asyncio

from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers import register_handlers


async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()

    register_handlers(dp)

    me = await bot.get_me()
    print(f"LoveBot v2.0 запущен как @{me.username}")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())