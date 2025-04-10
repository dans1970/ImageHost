"""
Блок постоянных значений:
адрес сервера
путь к папке static
путь к папке images
используемые расширения файлов
максимальный размер файла
путь и имя файла для логов
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
