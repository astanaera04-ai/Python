import asyncio
import logging
from aiogram import Bot, Dispatcher
from database import StudyDatabase
from handlers import StudyHandlers

TOKEN = "8863300742:AAH3Zg2IHP0uu_S5iN8DfmnHjd3kspEbQ5Y"

async def main():
    db = StudyDatabase()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    study_handlers = StudyHandlers(db)
    dp.include_router(study_handlers.router)

    print("Super Bot Architecture is running smooth and bug-free...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())