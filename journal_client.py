import requests

from settings import TOKEN
from datetime import datetime
# https://one.43edu.ru/edv/index/report/diary/TOKEN?format=xls&date=29.01.2024&homework-mode=previous
# https://one.43edu.ru/#diary

dt_now = datetime.now()
today = dt_now.strftime('%d.%m.%Y')
print(today)


class get_journal:
    URL_BASE = "https://one.43edu.ru/edv/index/report/diary/"
    URL_TOKEN = TOKEN
    URL_PARAM_FORMAT = "format=xls"
    URL_PARAM_MODE = "homework-mode=previous"

    def get_xls(self):
        """
        Метод для получения xls файла
        Файл небольшой, храним в памяти
        Необходимо передавать дату
        """