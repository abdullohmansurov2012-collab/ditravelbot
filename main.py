import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

from handlers import router

async def main():
    load_dotenv()
    
    # PythonAnywhere bepul tarifi uchun proxy sozlamasi
    from aiogram.client.session.aiohttp import AiohttpSession
    session = AiohttpSession(proxy="http://proxy.server:3128")
    
    bot = Bot(token=os.getenv("BOT_TOKEN"), session=session)
    dp = Dispatcher()
    dp.include_router(router)

    logging.basicConfig(level=logging.INFO)
    print("Bot ishga tushmoqda...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
