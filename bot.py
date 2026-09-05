import asyncio


print("A1: bot.py начал запуск", flush=True)


async def main():
    print("A2: начинаю импорт aiogram", flush=True)

    from aiogram import Bot, Dispatcher

    print("A3: aiogram импортирован", flush=True)

    print("A4: импортирую config", flush=True)

    from config import TOKEN

    print("A5: config импортирован", flush=True)

    print("A6: импортирую handlers", flush=True)

    from handlers import register_handlers

    print("A7: handlers импортированы", flush=True)

    print("A8: создаю Bot", flush=True)

    bot = Bot(TOKEN)
    dp = Dispatcher()

    print("A9: Bot и Dispatcher созданы", flush=True)

    print("A10: регистрирую обработчики", flush=True)

    register_handlers(dp)

    print("A11: обработчики зарегистрированы", flush=True)

    print("A12: проверяю подключение к Telegram", flush=True)

    try:
        me = await bot.get_me()
        print(
            f"A13: подключение успешно! Бот: @{me.username}",
            flush=True
        )
    except Exception as e:
        print(
            f"A13 ERROR: не удалось подключиться к Telegram: {e}",
            flush=True
        )
        await bot.session.close()
        raise

    print("A14: запускаю polling", flush=True)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        print("A15: бот остановлен", flush=True)


if __name__ == "__main__":
    print("A0: запускаю asyncio", flush=True)
    asyncio.run(main())
