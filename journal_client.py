import requests

from settings import TOKEN
from settings import USER
from settings import PASSWD
from datetime import datetime

dt_now = datetime.now()
today = dt_now.strftime('%d.%m.%Y')
user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

print(today)


class get_journal:
    URL_REFERER = "https://one.43edu.ru/auth/login"
    URL_AUTH = "https://passport.43edu.ru/auth/login"
    URL_TOKEN = TOKEN
    URL_PARAM_FORMAT = "xls"
    URL_PARAM_MODE = "homework-mode=previous"
    
    def get_xls(self):
        """
        Метод для получения xls файла
        Файл небольшой, храним в памяти
        """
        auth_data = {'login': USER, 'password': PASSWD, "submit": "submit", "returnTo": "https://one.43edu.ru"}
        session = requests.Session()
        auth__req = session.post(self.URL_AUTH, data=data)
        url_xls_base = f'https://one.43edu.ru/edv/index/report/diary/{self.URL_TOKEN}'
        url_xls_data = {'format': 'xls',
                        'date': today,
                        'homework-mode': 'previous'}
        get_xls_req = session.get(url_xls_base,data=url_xls_data)

        return get_xls_req
    
journal = get_journal()

print(journal.get_xls().text)