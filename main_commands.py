from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram import Router, F
from main_kb import create_goods_keyboard
from aiogram.types import FSInputFile, InputMediaPhoto

from aiogram.fsm.context import FSMContext
from states import OrderForm
from database import add_order, get_products

router_commands = Router()

# ------------------------------------------------ #



# ------------------------------------------------ #
def is_valid_phone(phone: str):
    if phone.startswith("+"):
        phone = phone[1:]
    return phone.isdigit() and 10 <= len(phone) <= 13

def get_goods_page(products, page):
    name, price, description, photo = products[page - 1]
    text = f"{name}:\n Цена: {price}\n Описание: {description}\n\n"
    return text, photo

    
@router_commands.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я бот для просмотра товаров. Используй команду /goods, чтобы увидеть список товаров.")

@router_commands.message(Command("goods"))
async def goods_command(message: Message):
    products = await get_products()
    max_page = len(products)

    text, photo = get_goods_page(products, 1)
    await message.answer_photo(photo=FSInputFile(photo), caption=text, reply_markup=create_goods_keyboard(1, max_page))

@router_commands.callback_query(F.data.startswith("page:"))
async def goods_page_callback(callback: CallbackQuery):
    page = int(callback.data.split(":")[-1])
    products = await get_products()
    max_page = len(products)

    text, photo = get_goods_page(products, page)
    media = InputMediaPhoto(media=FSInputFile(photo), caption=text)
    await callback.message.edit_media(media=media, reply_markup=create_goods_keyboard(page, max_page))
    await callback.answer()

@router_commands.message(Command("cancel"))
async def cancel_order(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Заказ отменен.")

@router_commands.callback_query(F.data.startswith("order:"))
async def order_callback(callback: CallbackQuery, state: FSMContext):
    page = int(callback.data.split(":")[-1])
    products = await get_products()
    name, _, _, _ = products[page - 1]
    await state.update_data(product=name)
    await state.set_state(OrderForm.name)
    await callback.message.answer("Как вас зовут?")
    await callback.answer()

@router_commands.message(OrderForm.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(OrderForm.phone)
    await message.answer("Введите номер телефона: ")

@router_commands.message(OrderForm.phone)
async def get_phone(message: Message, state: FSMContext):
    if not message.text or not is_valid_phone(message.text):
        await message.answer("Введите номер правильно, например +380991234567")
        return
    await state.update_data(phone=message.text)
    data = await state.get_data()
    await add_order(data["product"], data["name"], data["phone"])
    await message.answer(f"Данние о вашем заказе:\nТовар:{data["product"]}\nИмя: {data["name"]}\nТелефон:{data["phone"]}")
    await state.clear()

@router_commands.callback_query(F.data == "ignore")
async def ignore_callback(callback: CallbackQuery):
    await callback.answer()