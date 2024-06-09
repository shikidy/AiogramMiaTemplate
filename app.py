import logging

from aiogram.utils import executor

from src import dp


logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)