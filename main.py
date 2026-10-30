import os
import logging
from dotenv import load_dotenv
import asyncio

from aiogram import Bot, Dispatcher
from database import init_db

from main_commands import router_commands
from admin_cm import admin_router
# ------------------------------------------------ #
load_dotenv()
dp = Dispatcher()
dp.include_routers(router_commands, admin_router)

bot = Bot(token=os.getenv("TOKEN"))
# ------------------------------------------------ #

# ------------------------------------------------ #
async def main():
    await init_db()
    logging.info("Бот запущен.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")