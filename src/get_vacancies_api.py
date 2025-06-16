from abc import ABC, abstractmethod
from typing import Any


class GetVacanciesAPI(ABC):
    """Абстрактный класс для получения вакансии с hh.ru"""

    @abstractmethod
    def get_response(self, keyword: str, per_page: str) -> Any:
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, per_page: int) -> Any:
        pass
