import asyncio

from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers import register_handlers


async def main():
    print("1. Запуск LoveBot...")

    bot = Bot(TOKEN)
    dp = Dispatcher()

    print("2. Bot и Dispatcher созданы")

    register_handlers(dp)

    print("3. Обработчики зарегистрированы")

    try:
        me = await bot.get_me()
        print(f"4. LoveBot v2.0 запущен как @{me.username}")
    except Exception as e:
        print(f"ОШИБКА при подключении к Telegram: {e}")
        await bot.session.close()
        raise

    print("5. Запускаю polling...")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        print("6. Бот остановлен")


if __name__ == "__main__":
    asyncio.run(main())
