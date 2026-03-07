from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu():
    buttons = [
        [KeyboardButton(text="Umra Paketlar 🕋"), KeyboardButton(text="Ziyoratgohlar 🕌")],
        [KeyboardButton(text="Biz Haqimizda ✈️"), KeyboardButton(text="Bog'lanish 📞")],
        [KeyboardButton(text="Foydali Ma'lumotlar 💡")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_ziyorat_menu():
    buttons = [
        [KeyboardButton(text="Mahalliy Ziyoratlar 🕌"), KeyboardButton(text="Umra Safarlari 🕋")],
        [KeyboardButton(text="Ziyorat turlari ℹ️")],
        [KeyboardButton(text="🔙 Orqaga")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_info_menu():
    buttons = [
        [KeyboardButton(text="Sayohatga tayyorgarlik 🎒"), KeyboardButton(text="Viza masalalari 🛂")],
        [KeyboardButton(text="Ziyorat Odoblari & Duolar 📖")],
        [KeyboardButton(text="Tez-tez so'raladigan savollar ❓")],
        [KeyboardButton(text="🔙 Orqaga")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_religious_menu():
    buttons = [
        [KeyboardButton(text="Ehrom kiyish tartibi 🕋"), KeyboardButton(text="Safar duolari ✈️")],
        [KeyboardButton(text="Tavof va Sa'y duolari 🤲"), KeyboardButton(text="Madina ziyorati odoblari 🕌")],
        [KeyboardButton(text="⬅️ Foydali Ma'lumotlar")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_umra_menu():
    buttons = [
        [InlineKeyboardButton(text="Individual Reja Tuzish 📋", url="https://agent.jotform.com/019b9d53800276e59b6c31fa4efb381e5c2f")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
