from typing import Any

import requests
from requests import Response

from src.get_vacancies_api import GetVacanciesAPI


class HeadHunterAPI(GetVacanciesAPI):
    """Класс для подключения к hh.ru"""

    def __init__(self) -> None:
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params: dict[str, str | int | bool] = {"text": "", "per_page": "", "only_with_salary": True}

    def get_response(self, keyword: str, per_page: str) -> Response:
        self.params["text"] = keyword
        self.params["per_page"] = per_page
        return requests.get(self.url, params=self.params)

    def get_vacancies(self, keyword: str, per_page: int = 20) -> Any:
        return self.get_response(keyword, str(per_page)).json()["items"]
