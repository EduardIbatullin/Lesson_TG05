#  config.py

from dotenv import load_dotenv
import os

#  Загрузка переменных окружения из .env файла
load_dotenv()


#  Класс конфигурации
class Config:
    # Токен Telegram API
    TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN', 'your-telegram-api-token-here')
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'your-weather-api-key-here')
    THE_CAT_API_KEY = os.getenv('THE_CAT_API_KEY', 'your-the-cat-api-key-here')
    NASA_API_KEY = os.getenv('NASA_API_KEY', 'your-nasa-api-key-here')
