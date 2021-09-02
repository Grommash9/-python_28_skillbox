from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests
import time

def status_check(tx):

    final_link = f'https://chain.api.btc.com/v3/tx/{tx}?verbose=3'

    response = requests.get(final_link)

    my_dict = response.json()

    return my_dict['data']['confirmations']

bot = Bot(token='1975741586:AAFJQilNIPrGBoDBLZ450uVNTtx8jw6PaU4')
dp = Dispatcher(bot)


@dp.message_handler()
async def process_start_command(message: types.Message):
    answer = status_check(message.text)
    print(message)
    while answer <= 0:
        await message.reply('Ваша транзакиця ещё не прошла, мы будем автоматически проверять её статус каждые 60 секунд')
        time.sleep(60)
        answer = status_check(message.text)
    await message.reply('Ваша транзакция успешно прошла, вот ваш товар')
    await bot.send_document(message.from_user.id, open('sdds.txt', 'rb'))



@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
