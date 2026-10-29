from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram import Router, F
from main_kb import create_goods_keyboard

import math

router_commands = Router()

# ------------------------------------------------ #
goods = {"Кофемашина": 
         {"price": 35000, "description": "Автоматическая кофемашина с капучинатором"},
         "Электрочайник": 
         {"price": 2800, "description": "Стеклянный чайник с подсветкой и терморегулятором"},
         "Микроволновая печь": 
         {"price": 15000, "description": "Микроволновая печь с грилем и конвекцией"},
         "Холодильник": 
         {"price": 60000, "description": "Холодильник с системой No Frost и инверторным компрессором"},
         "Стиральная машина": 
         {"price": 40000, "description": "Стиральная машина с функцией сушки и инверторным мотором"},
         "Увлажнитель воздуха": 
         {"price": 5000, "description": "Увлажнитель воздуха с функцией ароматерапии"},
         "Портативная колонка": 
         {"price": 7000, "description": "Портативная колонка с Bluetooth и водонепроницаемым корпусом"},
         "Планшет": 
         {"price": 25000, "description": "Планшет с 10-дюймовым экраном и 128 ГБ памяти"},
         "Электронная книга": 
         {"price": 8000, "description": "Электронная книга с подсветкой и 8 ГБ памяти"},
         "Игровая приставка": 
         {"price": 20000, "description": "Игровая приставка с 1 ТБ памяти и поддержкой 4K"}
         }
goods_list = list(goods.items())
# ------------------------------------------------ #

per_page = 3
max_page = math.ceil(len(goods) / per_page)

# ------------------------------------------------ #

def get_goods_page(page, per_page):
    start = (page - 1) * per_page
    end = start + per_page

    text = ""
    for name, info in goods_list[start:end]:
        text += f"{name}:\n Цена: {info["price"]}\n Описание: {info["description"]}\n\n"
    return text

    
@router_commands.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я бот для просмотра товаров. Используй команду /goods, чтобы увидеть список товаров.")

@router_commands.message(Command("goods"))
async def goods_command(message: Message):
    page = 1
    
    await message.answer("Список товаров:\n\n" + get_goods_page(page, per_page), reply_markup=create_goods_keyboard(page, max_page))

@router_commands.callback_query(F.data.startswith("page:"))
async def goods_page_callback(callback: CallbackQuery):
    page = int(callback.data.split(":")[-1])

    await callback.message.edit_text("Список товаров:\n\n" + get_goods_page(page, per_page), reply_markup=create_goods_keyboard(page, max_page))
    await callback.answer()

@router_commands.callback_query(F.data == "ignore")
async def ignore_callback(callback: CallbackQuery):
    await callback.answer()