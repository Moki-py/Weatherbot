"""Get the weather for the city."""
import datetime
import requests
from config import OPEN_WEATHER_TOKEN as open_weather_token


def get_weather(city: str, token: str):
    """Get the weather for the city."""

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
            f"http://api.openweathermap.org/data/2.5/weather?q={city}"
            f"&appid={token}&units=metric"
        )
        r = requests.get(url, timeout=5)
        data = r.json()

        city_n = data["name"]
        icon = data["weather"][0]["main"]

        if icon in code_to_smile:
            weather_disc = code_to_smile[icon]
        else:
            weather_disc = "Глянь в окно"
        temp = data["main"]["temp"]
        temp_feels_like = data["main"]["feels_like"]
        temp_max = data["main"]["temp_max"]
        temp_min = data["main"]["temp_min"]
        humidity = data["main"]["humidity"]

        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        wind_speed = data["wind"]["speed"]

        print(f"Дата {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}:\n"
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
    except requests.exceptions.RequestException as ex:
        print("Ошибка: ", ex)


def main():
    """Main function."""
    city = input("Введи город: ")
    get_weather(city, open_weather_token)


if __name__ == "__main__":
    main()
