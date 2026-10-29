from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_goods_keyboard(page, max_page):
    keyboard = []
    if page > 1:
        keyboard.append(
            InlineKeyboardButton(text="<-", callback_data=f"page:{page - 1}")
        )
    keyboard.append(
        InlineKeyboardButton(text=f"{page}/{max_page}", callback_data="ignore")
    )
    if page < max_page:
        keyboard.append(
            InlineKeyboardButton(text="->", callback_data=f"page:{page + 1}")
        )
    return InlineKeyboardMarkup(inline_keyboard=[keyboard])

