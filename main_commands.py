from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram import Router, F
from main_kb import create_goods_keyboard
from aiogram.types import FSInputFile, InputMediaPhoto
import math

router_commands = Router()

# ------------------------------------------------ #
goods = {"Кофемашина": 
         {"price": 35000, "description": "Автоматическая кофемашина с капучинатором", "photo": "images/tovar_dlya_prodazhi.jpg"},
         "Электрочайник": 
         {"price": 2800, "description": "Стеклянный чайник с подсветкой и терморегулятором", "photo": "images/anons.webp"},
         "Микроволновая печь": 
         {"price": 15000, "description": "Микроволновая печь с грилем и конвекцией", "photo": "images/articles-6085_l_md_1x.png"},
         "Холодильник": 
         {"price": 60000, "description": "Холодильник с системой No Frost и инверторным компрессором", "photo": "images/images.png"},
         "Стиральная машина": 
         {"price": 40000, "description": "Стиральная машина с функцией сушки и инверторным мотором", "photo": "images/articles-6085_l_md_1x.png"},
         "Увлажнитель воздуха": 
         {"price": 5000, "description": "Увлажнитель воздуха с функцией ароматерапии", "photo": "images/images.png"},
         "Портативная колонка": 
         {"price": 7000, "description": "Портативная колонка с Bluetooth и водонепроницаемым корпусом", "photo": "images/images.png"},
         "Планшет": 
         {"price": 25000, "description": "Планшет с 10-дюймовым экраном и 128 ГБ памяти", "photo": "images/images.png"},
         "Электронная книга": 
         {"price": 8000, "description": "Электронная книга с подсветкой и 8 ГБ памяти", "photo": "images/tovar_dlya_prodazhi.jpg"},
         "Игровая приставка": 
         {"price": 20000, "description": "Игровая приставка с 1 ТБ памяти и поддержкой 4K", "photo": "images/tovar_dlya_prodazhi.jpg"}
         }
goods_list = list(goods.items())
# ------------------------------------------------ #

per_page = 1
max_page = math.ceil(len(goods) / per_page)

# ------------------------------------------------ #

def get_goods_page(page):
    name, info = goods_list[page - 1]
    text = f"{name}:\n Цена: {info["price"]}\n Описание: {info["description"]}\n\n"
    return text, info["photo"]

    
@router_commands.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я бот для просмотра товаров. Используй команду /goods, чтобы увидеть список товаров.")

@router_commands.message(Command("goods"))
async def goods_command(message: Message):
    text, photo = get_goods_page(1)
    await message.answer_photo(photo=FSInputFile(photo), caption=text, reply_markup=create_goods_keyboard(1, max_page))

@router_commands.callback_query(F.data.startswith("page:"))
async def goods_page_callback(callback: CallbackQuery):
    page = int(callback.data.split(":")[-1])
    text, photo = get_goods_page(page)
    media = InputMediaPhoto(media=FSInputFile(photo), caption=text)
    await callback.message.edit_media(media=media, reply_markup=create_goods_keyboard(page, max_page))
    await callback.answer()

@router_commands.callback_query(F.data == "ignore")
async def ignore_callback(callback: CallbackQuery):
    await callback.answer()