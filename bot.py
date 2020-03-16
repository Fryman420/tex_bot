import logging
import random
import sqlite3
import numpy as np
import matplotlib.font_manager as fm
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
from aiogram.utils.helper import Helper, HelperMode, ListItem
import matplotlib.pyplot as plt
class TestStates(Helper):
    mode =  HelperMode.snake_case
    TEST_STATE_0  = ListItem()
    TEST_STATE_1  = ListItem()
    TEST_STATE_2  = ListItem()
    TEST_STATE_3  = ListItem()
#API_TOKEN = 'BOT TOKEN HERE'
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware


    #plt.show()
# Configure logging


prop = fm.FontProperties(fname='comic.ttf')
PROXY_URL = 'socks5://127.0.0.1:9150'

token = '1129188006:AAHA-B0NXppF9wxC19ChSV8scPl6944WyHA'
# Initialize bot and dispatcher

bot = Bot(token=token, proxy = PROXY_URL)

dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

logging.basicConfig(level=logging.INFO)

def draw(tex):
### Создание области отрисовки
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.set_axis_off()
    ### Отрисовка формулы
    t = ax.text(0.5, 0.5, tex,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=20, color='black', fontproperties=prop)
            
    ### Определение размеров формулы
    ax.figure.canvas.draw()
    bbox = t.get_window_extent()
    print(bbox.width, bbox.height)

    # Установка размеров области отрисовки
    fig.set_size_inches(bbox.width/70,bbox.height/70) # dpi=80

    ### Отрисовка или сохранение формулы в файл
    #plt.savefig('test.png')
    part_of_file_name = str(random.randint(0,10))
    filename = 'test' + part_of_file_name + '.png'
    plt.savefig(filename, dpi=300)
    return filename
#def_text = 'Привет!\n Если хочешь порадоваться, напиши мне:\n Порадуй меня!\n Пришли картинку!'
@dp.message_handler(commands=['start'])

async def send_welcome(message: types.Message):

    """

    This handler will be called when user sends `/start` or `/help` command

    """

    await message.reply("Привет! Я - бот, который может верстать теховские формулы.\nОтправь мне теховский код и я верну тебе формулу!\nНажми /help чтобы узнать больше о том, как я работаю.")




@dp.message_handler(commands=[ 'help'])

async def send_welcome(message: types.Message):

    """

    This handler will be called when user sends `/start` or `/help` command

    """

    await message.answer("Формулу мне надо присылать без значков $ по бокам.\nВ остальном синтаксис абсолютно тот же самый как и в TeX. Для маленьких выражений использовать меня не очень целесообразно, так как картинки будут получаться шакальные.\nЕще я згнаю команду /examples")


@dp.message_handler(commands=[ 'examples'])

async def send_welcome(message: types.Message):

    """

    This handler will be called when user sends `/start` or `/help` command

    """

    await message.answer("Интеграл 1/x:")
    ex1 = "\\int\\frac{dx}{x} = ln(x) + C"
    tex_1 = "$" + ex1 + "$"
    await message.answer(ex1)
    filename = draw(tex_1)
    plt.savefig(filename, dpi=300)
    with open(filename, 'rb') as photo:
        await message.answer_photo(photo)
    
    await message.answer("Уравнение Шредингера:")
    ex2 = "i\\hbar\\partial_t\\psi = \hat H(p,q)\\psi"
    tex_2 = "$" + ex2 + "$"
    filename = draw(tex_2)
    await message.answer(ex2)
    plt.savefig(filename, dpi=300)
    with open(filename, 'rb') as photo:
        await message.answer_photo(photo)
    
    await message.answer("Определение экспоненты:")
    ex3 = 'e = \\lim_{n\\to\\infty}(1+\\frac{1}{n})^n'
    tex_3 = "$" + ex3 + "$"
    filename = draw(tex_3)
    await message.answer(ex3)
    plt.savefig(filename, dpi=300)
    with open(filename, 'rb') as photo:
        await message.answer_photo(photo)






@dp.message_handler()
async def making_happy(message: types.Message):

    # old style:

    # await bot.send_message(message.chat.id, message.text)

    tex = '$\\frac{1}{\\sqrt{2\\sqrt{2\\pi}}} \\exp\\left(-\\frac{(x-\\mu)^2}{2\\sigma^2}\\right)\\frac{1}{\\sqrt{2\\sqrt{2\\pi}}} \\exp\\left(-\\frac{(x-\\mu)^2}{2\\sigma^2}\\right)$'
    tex = '$x\\approx 1.5$'
    if_andrey_pidor = random.randint(0, 20)
    if if_andrey_pidor != 0:
        tex = '$' + str(message.text) + '$'
    else:
        tex = 'Андрей, ты пидорас!!!!'
    filename = draw(tex)
    plt.savefig(filename, dpi=300)
    #plt.show()
    with open(filename, 'rb') as photo:
        await message.answer_photo(photo, caption='Лови!') 
        #await message.answer('Прости, но я не умею с этим работать((')
@dp.message_handler(state='*', content_types = ContentType.ANY)
async def reply_to_shit(message: types.Message):
    await message.answer('Прости, но я не умею с этим работать((')



if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
