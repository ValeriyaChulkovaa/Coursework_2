import json
from typing import Any

from src.saver import Saver


class JSONSaver(Saver):
    """Класс для записи в json-файл"""

    def __init__(self, filename: str) -> None:
        """Конструктор класса"""

        super().__init__(filename)

    def write_data(self, vacancies: str) -> None:
        """Запись данных в json"""

        data = self.get_data()
        data.extend(vacancies)

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_data(self) -> Any:
        """Получение данных json"""

        try:
            return json.load(open(self.filename, encoding="utf-8"))
        except FileNotFoundError:
            return []

    def del_data(self) -> None:
        """Удаление данных из файла"""

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
