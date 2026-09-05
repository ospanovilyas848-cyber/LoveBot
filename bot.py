import asyncio

print("A0: старт", flush=True)

async def main():
    from aiogram import Bot, Dispatcher

    from config import TOKEN
    from handlers import register_handlers

    print("A1: создаю Bot", flush=True)
    bot = Bot(TOKEN)

    print("A2: проверяю Telegram", flush=True)
    me = await bot.get_me()
    print(f"A3: @{me.username} работает", flush=True)

    print("A4: проверяю pending updates", flush=True)
    updates = await bot.get_updates(offset=-1)

    print(f"A5: Telegram вернул {len(updates)} update(s)", flush=True)

    if updates:
        print(f"A6: последний update_id = {updates[-1].update_id}", flush=True)

    dp = Dispatcher()

    print("A7: регистрирую handlers", flush=True)
    register_handlers(dp)

    print("A8: запускаю polling", flush=True)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
