from datetime import datetime

import requests

from settings import TOKEN
from settings import USER
from settings import PASSWD


dt_now = datetime.now()
today = dt_now.strftime('%d.%m.%Y')


class GetJournal:
    URL_REFERER = "https://one.43edu.ru/auth/login"
    URL_AUTH = "https://passport.43edu.ru/auth/login"
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
        url_xls_base = f'https://one.43edu.ru/edv/index/report/diary/{TOKEN}'
        url_xls_data = {'format': 'xls',
                        'date': today,
                        'homework-mode': 'previous'}
        xls_file = self.session.get(url_xls_base, data=url_xls_data)
        return xls_file

    def save_in_file(self, xls_file):
        with open('./journal.xls', 'wb') as f:
            f.write(xls_file)
