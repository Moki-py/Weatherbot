"""This is a weather bot for Telegram. """
import datetime

import requests

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TG_BOT_TOKEN as tg_bot_token
from config import OPEN_WEATHER_TOKEN as open_weather_token
from config import CHAT_ID1, CHAT_ID2


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    """Send a message when the command /start is issued. """
    await message.reply(
        "Напиши мне название города на английском и я пришлю тебе погоду!"
        )


@dp.message_handler()
async def get_weather(message: types.Message):
    """Get the weather for the city."""

    print(message.chat.id, message.text)

    code_to_smile = {
        "Clear":  "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain":   "Дождь \U00002614",
        "Drizzle": "Мелкий дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B",
        "Fog": "Туман \U0001F32B",
        "Smoke": "Смог \U0001F32A",
        "Haze": "Мгла \U0001F32A",
        "Dust": "Пыль \U0001F32A",
        "Sand": "Песок \U0001F32A",
        "Ash": "Пепел \U0001F32A",
        "Squall": "Шквал \U0001F32A",
        "Tornado": "Торнадо \U0001F32A",
    }

    try:
        url = (
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}"
            f"&appid={open_weather_token}&units=metric"
        )
        r = requests.get(url, timeout=5)
        data = r.json()

        city_n = data["name"]
        icon = data["weather"][0]["main"]

        weather_disc = code_to_smile.get(icon, "Посмотри в окно")

        temp = data["main"]["temp"]
        temp_feels_like = data["main"]["feels_like"]
        temp_max = data["main"]["temp_max"]
        temp_min = data["main"]["temp_min"]
        humidity = data["main"]["humidity"]

        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        wind_speed = data["wind"]["speed"]

        await message.reply(
              f"Дата {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}:\n"
              f"Город: {city_n}\n\n"
              f"{weather_disc}\n"
              f"Температура: {temp}°C\n"
              f"Ощущается как: {temp_feels_like}°C\n\n"
              f"Максимальная температура: {temp_max}°C\n"
              f"Минимальная температура: {temp_min}°C\n\n"
              f"Влажность: {humidity}%\n\n"
              f"Восход: {sunrise}\n"
              f"Закат: {sunset}\n\n"
              f"Скорость ветра: {wind_speed} м/с")

    except KeyError:
        await message.reply(
            "\U00002620 Проверь название города и пиши по английски \U00002620"
            )


async def send_message():
    """Send a message to the user."""
    await bot.send_message(CHAT_ID1, '<3')
    await bot.send_message(CHAT_ID2, ':]')

if __name__ == "__main__":
    executor.start(dp, send_message())
    executor.start_polling(dp)
