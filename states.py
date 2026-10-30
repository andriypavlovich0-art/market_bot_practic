from aiogram.fsm.state import State, StatesGroup

class OrderForm(StatesGroup):
    name = State()
    phone = State()

class AddProduct(StatesGroup):
    product_name = State()
    price = State()
    description = State()
    photo = State()
