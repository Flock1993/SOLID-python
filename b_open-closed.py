# Принцип открытости-закрытости
# Класс закрыт для модификации, но открыт для расширения
# Реализация: полиморфизм + абстрактные классы
# Для нового функционала создаём новый класс, а не модифицируем существующие классы
from abc import ABC, abstractmethod
from a_single_responsibility import Computer


class Save(ABC):
    @abstractmethod
    def save(self, computer: Computer):
        pass


class SaveToFile(Save):
    def save(self, computer: Computer):
        print(f"Сохранение объекта {computer.name} в файл")


class SaveToDB(Save):
    def save(self, computer: Computer):
        print(f"Сохранение объекта {computer.name} в БД")


if __name__ == '__main__':
    inst = Computer("Xiaomi", 128)
    file_save = SaveToFile()
    file_save.save(inst)


