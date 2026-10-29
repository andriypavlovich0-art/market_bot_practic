import aiosqlite

BD_NAME = "shop.db"

async def init_db():
    async with aiosqlite.connect(BD_NAME) as bd:
        await bd.execute("""
            CREATE TABLE IF NOT EXISTS products (
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         name TEXT,
                         price INTEGER,
                         description TEXT,
                         photo TEXT
                         )
                        """)
        await  bd.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         product TEXT,
                         name TEXT,
                         phone TEXT
                         )
                        """)
        await bd.commit()
    
async def add_order(product, name, phone):
    async with aiosqlite.connect(BD_NAME) as bd:
        await bd.execute("INSERT INTO orders (product, name, phone) VALUES (?, ?, ?)", (product, name, phone))
        await bd.commit()