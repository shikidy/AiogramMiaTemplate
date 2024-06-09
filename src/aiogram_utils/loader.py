from aiogram import Bot, Dispatcher

from .config import Config


bot = Bot(Config().bot["token"], parse_mode="html")
dp = Dispatcher(bot)