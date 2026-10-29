import os
import logging
from dotenv import load_dotenv
import asyncio

from aiogram import Bot, Dispatcher

from main_commands import router_commands
# ------------------------------------------------ #
load_dotenv()
dp = Dispatcher()
dp.include_router(router_commands)

bot = Bot(token=os.getenv("TOKEN"))
# ------------------------------------------------ #

























# ------------------------------------------------ #
async def main():
    logging.info("Бот запущен.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")