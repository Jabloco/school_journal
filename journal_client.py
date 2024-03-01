import requests

from settings import TOKEN
from settings import USER
from settings import PASSWD
from datetime import datetime

dt_now = datetime.now()
today = dt_now.strftime('%d.%m.%Y')


class get_journal:
    URL_REFERER = "https://one.43edu.ru/auth/login"
    URL_AUTH = "https://passport.43edu.ru/auth/login"
    URL_TOKEN = TOKEN
    URL_PARAM_FORMAT = "xls"
    URL_PARAM_MODE = "homework-mode=previous"

    def __init__(self):
        self.session = requests.Session()

    def auth(self):
        auth_data = {'login': USER,
                     'password': PASSWD,
                     "submit": "submit",
                     "returnTo": "https://one.43edu.ru"
                     }
        auth__req = self.session.post(self.URL_AUTH, data=auth_data)

    def get_xls(self):
            url_xls_base = f'https://one.43edu.ru/edv/index/report/diary/{self.URL_TOKEN}'
            url_xls_data = {'format': 'xls',
                            'date': today,
                            'homework-mode': 'previous'}
            get_xls_req = self.session.get(url_xls_base, data=url_xls_data)

            return get_xls_req
