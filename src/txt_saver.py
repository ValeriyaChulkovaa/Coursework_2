from src.saver import Saver


class TXTSaver(Saver):
    """Класс для записи в txt-файл"""

    def __init__(self, filename: str) -> None:
        """Конструктор класса"""

        super().__init__(filename)

    def write_data(self, vacancies: str) -> None:
        """Запись данных в txt"""

        with open(self.filename, "a", encoding="utf=8") as file:
            file.write(vacancies)

    def get_data(self) -> list:
        """Получение данных txt"""

        with open(self.filename, encoding="utf-8") as file:
            return file.readlines()

    def del_data(self) -> None:
        """Удаление данных из файла"""

        with open(self.filename, "w", encoding="utf-8"):
            pass
