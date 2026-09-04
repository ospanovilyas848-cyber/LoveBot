from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards import main_menu
from memory import get_unique_text
import texts


def register_handlers(dp: Dispatcher):

    @dp.message(CommandStart())
    async def start(message: Message):
        await message.answer(
            "🌸 **Добро пожаловать, Эля ❤️**\n\n"
            "Я всегда рядом, даже если между нами километры.\n\n"
            "Выбери, что хочешь получить ✨",
            reply_markup=main_menu,
            parse_mode="Markdown"
        )

    @dp.message(lambda m: m.text == "💌 Письмо")
    async def letter(message: Message):
        text = get_unique_text(message.from_user.id, "letters", texts.letters)
        await message.answer(text)

    @dp.message(lambda m: m.text == "🫂 Обнимашка")
    async def hug(message: Message):
        text = get_unique_text(message.from_user.id, "hugs", texts.hugs)
        await message.answer(text)

    @dp.message(lambda m: m.text == "😘 Поцелуй")
    async def kiss(message: Message):
        text = get_unique_text(message.from_user.id, "kisses", texts.kisses)
        await message.answer(text)

    @dp.message(lambda m: m.text == "🌹 Комплимент")
    async def compliment(message: Message):
        text = get_unique_text(message.from_user.id, "compliments", texts.compliments)
        await message.answer(text)

    @dp.message(lambda m: m.text == "❤️ Почему ты особенная")
    async def reason(message: Message):
        text = get_unique_text(message.from_user.id, "reasons", texts.reasons)
        await message.answer(text)

    @dp.message(lambda m: m.text == "💭 Скучаю по тебе")
    async def miss(message: Message):
        text = get_unique_text(message.from_user.id, "miss_you", texts.miss_you)
        await message.answer(text)

    @dp.message(lambda m: m.text == "☀️ Доброе утро")
    async def morning(message: Message):
        text = get_unique_text(message.from_user.id, "good_morning", texts.good_morning)
        await message.answer(text)

    @dp.message(lambda m: m.text == "🌙 Спокойной ночи")
    async def night(message: Message):
        text = get_unique_text(message.from_user.id, "good_night", texts.good_night)
        await message.answer(text)

    @dp.message(lambda m: m.text == "🫶 Поддержка")
    async def support(message: Message):
        text = get_unique_text(message.from_user.id, "support", texts.support)
        await message.answer(text)

    @dp.message(lambda m: m.text == "🎲 Чем займёмся?")
    async def activity(message: Message):
        text = get_unique_text(message.from_user.id, "activities", texts.activities)
        await message.answer(text)

    @dp.message(lambda m: m.text == "🎵 Наша музыка")
    async def music(message: Message):
        await message.answer(
            "🎵 Пока здесь будет наша любимая песня.\n\n"
            "Когда выберешь её, мы добавим ссылку прямо сюда. ❤️"
        )