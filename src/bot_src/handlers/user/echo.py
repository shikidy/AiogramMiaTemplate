from aiogram.types import Message

from src import dp


@dp.message_handler()
async def echo(msg: Message):
    await msg.answer(msg.text)