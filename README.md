# Weather Bot for Telegram / Телеграм-бот для прогноза погоды

This repository contains a Telegram bot that provides weather updates for any city specified by the user. The bot uses the OpenWeather API to fetch weather data and responds with details such as temperature, humidity, wind speed, and sun timings.

Этот репозиторий содержит телеграм-бота, который предоставляет информацию о погоде в любом указанном пользователем городе. Бот использует API OpenWeather для получения данных о погоде и отвечает деталями такими, как температура, влажность, скорость ветра и времена восхода и заката.

## Features / Функциональность

- **/start command**: Initiates interaction with the bot.
- **Weather query**: Users can send the name of a city in English, and the bot will respond with the current weather information.

- **Команда /start**: Запускает взаимодействие с ботом.
- **Запрос погоды**: Пользователи могут отправить название города на английском, и бот ответит текущей информацией о погоде.

## Technologies Used / Используемые технологии

- **Python 3.11**: The bot is written in Python.
- **aiogram**: This asynchronous framework is used to handle Telegram bot interactions.
- **OpenWeather API**: Used to retrieve current weather data.

- **Python 3.11**: Бот написан на Python.
- **aiogram**: Этот асинхронный фреймворк используется для обработки взаимодействий с ботом в Telegram.
- **API OpenWeather**: Используется для получения текущих данных о погоде.

## Setup and Installation / Установка и настройка

### Prerequisites / Предварительные требования

- Python 3.11 or higher
- A Telegram bot token (you can get one from [BotFather](https://t.me/botfather))
- An API key for OpenWeather (obtainable from [OpenWeatherMap](https://openweathermap.org/api))

- Python 3.11 или выше
- Токен телеграм-бота (можно получить у [BotFather](https://t.me/botfather))
- Ключ API для OpenWeather (можно получить на [OpenWeatherMap](https://openweathermap.org/api))

### Installation Steps / Шаги установки

1. **Clone the repository / Клонирование репозитория**:

```
   git clone [URL of the repository]
   cd [name of the repository folder]
```

2. Install required packages / Установка необходимых пакетов:

```
  Copy code
  pip install -r requirements.txt
  Configure tokens / Настройка токенов:
```

3. Create a config.py file in the root directory and add your Telegram and OpenWeather tokens:

```
TG_BOT_TOKEN = 'your_telegram_bot_token'
OPEN_WEATHER_TOKEN = 'your_openweather_api_key'
```

4. Run the bot / Запуск бота:

```
python main_weather_tg_bot.py
```

### How to Contribute / Как внести вклад

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

Мы приветствуем вклад в развитие этого проекта! Если вы хотите помочь, пожалуйста, сделайте форк репозитория и используйте ветку для новых функций. Pull-запросы очень приветствуются.