from database import get_orders
from aiogram.fsm.context import FSMContext
import os
from dotenv import load_dotenv
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from states import AddProduct
from database import add_product

# ------------------------------------------------ #
load_dotenv()
ADMIN_ID = int(os.getenv("ADMIN_ID"))

admin_router = Router()
# ------------------------------------------------ #

@admin_router.message(Command("orders"), F.from_user.id == ADMIN_ID)
async def get_orders_cm(message: Message):
    orders = await get_orders()
    if not orders:
        await message.answer("Заказов пока нет")
        return 
    text = "📋 Заказы:\n\n"
    for order_id, product, name, phone in orders:
        text += f"#{order_id} {product}\n{name}, {phone}\n\n"
    await message.answer(text)

@admin_router.message(Command("add_product"), F.from_user.id == ADMIN_ID)
async def add_product_cm(message: Message, state: FSMContext):
     await state.set_state(AddProduct.product_name)
     await message.answer("Введите название нового товара: ")

@admin_router.message(AddProduct.product_name)
async def get_product_name(message: Message, state: FSMContext):
    await state.update_data(product_name=message.text)
    await state.set_state(AddProduct.price)
    await message.answer("Введите цену товара: ")

@admin_router.message(AddProduct.price)
async def get_price(message: Message, state: FSMContext):
    try:
        int_price = int(message.text)
        await state.update_data(price=int_price)
        await state.set_state(AddProduct.description)
        await message.answer("Введите описание товара: ")
    except (ValueError, TypeError):
        await message.answer("Пожалуйста, отправьте корректную цену")

@admin_router.message(AddProduct.description)
async def get_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(AddProduct.photo)
    await message.answer("Пришлите фото товара: ")


@admin_router.message(AddProduct.photo, F.photo)
async def get_photo(message: Message, state: FSMContext):
    file_id = message.photo[-1].file_id
    await state.update_data(photo=file_id)
    data = await state.get_data()
    await add_product(data["product_name"], data["price"], data["description"], data["photo"])
    await message.answer("✅ Товар добавлен!")
    await state.clear()

@admin_router.message(AddProduct.photo)
async def answer_photo(message: Message):
    await message.answer("Пришлите именно фото.")