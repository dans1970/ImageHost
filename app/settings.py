import os

import dotenv

dotenv.load_dotenv('.env')
"""
Блок постоянных значений:
адрес сервера
путь к папке static
путь к папке images
используемые расширения файлов
максимальный размер файла
путь и имя файла для логов программы
html файл для вывода ошибки
"""
SERVER_ADDRESS = ('0.0.0.0', 8000)
STATIC_PATH = 'static/'
IMAGES_PATH = 'images/'
ALLOWED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif']
MAX_FILE_SIZE = 5 * 1024 * 1024
LOG_PATH = 'logs/'
LOG_FILE = 'app.log'
ERROR_FILE = 'upload_failed.html'

# Настройка PostgreSQL
POSTGRES_NAME = os.getenv('POSTGRES_NAME') or 'postgres'
POSTGRES_USER = os.getenv('POSTGRES_USER') or 'postgres'
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD') or 'postgres'
POSTGRES_HOST = os.getenv('POSTGRES_HOST') or 'db'
POSTGRES_PORT = os.getenv('POSTGRES_PORT') or '5432'

# Количество строк на страницу
PAGE_LIMIT = 10