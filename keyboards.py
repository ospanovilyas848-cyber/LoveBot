from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💌 Письмо"), KeyboardButton(text="🫂 Обнимашка")],
        [KeyboardButton(text="😘 Поцелуй"), KeyboardButton(text="🌹 Комплимент")],
        [KeyboardButton(text="❤️ Почему ты особенная")],
        [KeyboardButton(text="💭 Скучаю по тебе")],
        [KeyboardButton(text="☀️ Доброе утро"), KeyboardButton(text="🌙 Спокойной ночи")],
        [KeyboardButton(text="🎲 Чем займёмся?"), KeyboardButton(text="🎵 Наша музыка")],
        [KeyboardButton(text="🫶 Поддержка")],
    ],
    resize_keyboard=True
)