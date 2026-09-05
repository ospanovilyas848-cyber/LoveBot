import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

from config import TOKEN


async def main():
    print("BOT START", flush=True)

    bot = Bot(TOKEN)
    dp = Dispatcher()

    @dp.message(CommandStart())
    async def start(message: Message):
        print(
            f"START RECEIVED: user={message.from_user.id}, text={message.text}",
            flush=True
        )

        await message.answer("❤️ Я получил твоё сообщение! Бот работает.")


    @dp.message()
    async def any_message(message: Message):
        print(
            f"MESSAGE RECEIVED: user={message.from_user.id}, text={message.text}",
            flush=True
        )


    me = await bot.get_me()
    print(f"CONNECTED: @{me.username}", flush=True)

    print("POLLING START", flush=True)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
