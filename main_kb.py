from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_goods_keyboard(page, max_page):
    row1 = []
    if page > 1:
        row1.append(
            InlineKeyboardButton(text="<-", callback_data=f"page:{page - 1}")
        )
    row1.append(
        InlineKeyboardButton(text=f"{page}/{max_page}", callback_data="ignore")
    )
    if page < max_page:
        row1.append(
            InlineKeyboardButton(text="->", callback_data=f"page:{page + 1}")
        )
    row2 = [InlineKeyboardButton(text="🛒 Заказать", callback_data=f"order:{page}")]
    return InlineKeyboardMarkup(inline_keyboard=[row1, row2])

