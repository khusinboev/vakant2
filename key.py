from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()


TOKEN = "6846010816:AAHjzDte6tr-lRSMJriM1OSMPG1wEiJxcqw"

bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot, storage=storage)
