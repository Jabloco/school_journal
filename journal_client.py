import requests

from settings import TOKEN
from datetime import datetime
# https://one.43edu.ru/edv/index/report/diary/TOKEN?format=xls&date=date&homework-mode=previous
# https://one.43edu.ru/#diary


"""
import requests
def diary():
    session = requests.Session()
    headers = {'Referer': 'https://www.mos.ru/pgu/ru/application/dogm/journal/'}
    auth_url = "https://mrko.mos.ru/dnevnik/services/index.php"
    auth_req = session.get(auth_url, headers=headers, params={"login": ЛОГИН, "password": ПАРОЛЬ_В_MD5}, allow_redirects=False)

    main_req = session.get("https://mrko.mos.ru/dnevnik/services/dnevnik.php?r=1&first=1")

"""

dt_now = datetime.now()
today = dt_now.strftime('%d.%m.%Y')
print(today)


class get_journal:
    URL_BASE = "https://one.43edu.ru/edv/index/report/diary/"
    URL_TOKEN = TOKEN
    URL_PARAM_FORMAT = "xls"
    URL_PARAM_MODE = "homework-mode=previous"

    def get_xls(self):
        """
        Метод для получения xls файла
        Файл небольшой, храним в памяти
        Необходимо передавать дату
        """
        session = requests.Session()
        headers = {'Referer': 'https://one.43edu.ru/#diary'}
        auth_url = "https://passport.43edu.ru/?returnTo=https%3A%2F%2Fone.43edu.ru" #ссылка на страницу аутентификации
        url_for_main_req = f"{self.URL_BASE}{self.URL_TOKEN}"

        req = session.get(url_for_main_req,headers=headers, params={"format":self.URL_PARAM_FORMAT, "date": '29.01.2024', "homework-mode":self.URL_PARAM_MODE})

        return req

journal = get_journal()
# with open('/media/ssd/python_dev/school_journal/1.xls', 'wb') as f:
#     f.write(journal)
print(journal.get_xls().content)