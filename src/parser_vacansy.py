from abc import ABC, abstractmethod


class BaseAPIhhParse(ABC):
    """Абстрактный класс для получения вакансии с hh.ru"""

    @abstractmethod
    def get_response(self, keyword: str, per_page: str) -> None:
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, per_page: int) -> None:
        pass
