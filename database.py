import aiosqlite

BD_NAME = "shop.db"

async def init_db():
    async with aiosqlite.connect(BD_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS products (
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         name TEXT,
                         price INTEGER,
                         description TEXT,
                         photo TEXT
                         )
                        """)
        await  db.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         product TEXT,
                         name TEXT,
                         phone TEXT
                         )
                        """)
        await db.commit()
    
async def add_order(product, name, phone):
    async with aiosqlite.connect(BD_NAME) as db:
        await db.execute("INSERT INTO orders (product, name, phone) VALUES (?, ?, ?)", (product, name, phone))
        await db.commit()


async def add_product(name, price, description, photo):
    async with aiosqlite.connect(BD_NAME) as db:
        await db.execute("INSERT INTO products (name, price, description, photo) VALUES (?, ?, ?, ?)", (name, price, description, photo))
        await db.commit()

async def get_products():
    async with aiosqlite.connect(BD_NAME) as db:
        cursor = await db.execute("SELECT name, price, description, photo FROM products")
        return await cursor.fetchall()
    

async def update_price(price : int, product : str):
    async with aiosqlite.connect(BD_NAME) as db:
        await db.execute("UPDATE products SET price = ? WHERE name = ?", (price, product))
        await db.commit()
    
async def get_orders():
    async with aiosqlite.connect(BD_NAME) as db:
        cursor = await db.execute("SELECT id, product, name, phone FROM orders")
        return await cursor.fetchall()
