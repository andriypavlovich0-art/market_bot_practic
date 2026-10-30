import asyncio
from database import add_product, init_db

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


async def push_products():
    await init_db()
    for name, info in goods.items():
        await add_product(name, info["price"], info["description"], info["photo"])
    print("Товары добавлены!")

asyncio.run(push_products())