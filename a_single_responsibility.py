# Принцип единственной ответственности
# Каждый класс должен выполнять строго одну функцию

class ComputerGod:
    def __init__(self, name: str, memory_size: int):
        self.name: str = name
        self.memory_size: int = memory_size

    def save_to_file(self):
        """Если мы заходим сохранять не в файл, а в БД, то придётся создавать ещё методы"""
        print(f"Сохранение объекта класса {self.name} в файл")

    def load_from_file(self):
        print(f"Сохранение объекта класса {self.name} из файла")

# Рефакторинг


class Computer:
    def __init__(self, name: str, memory_size: int):
        self.name: str = name
        self.memory_size: int = memory_size


class SaveComputer:
    """Нарушается принцип открытости-закрытости, его исправление можно посмотреть в b_open-closed.py"""
    def __init__(self, computer: Computer):
        self.computer: Computer = computer

    def save_to_file(self):
        print(f"Сохранение объекта класса {self.computer.name} в файл")

    def save_to_db(self):
        print(f"Сохранение объекта класса {self.computer.name} в БД")


if __name__ == '__main__':
    inst = ComputerGod("HP", 256)
    inst.load_from_file()

    inst_ = Computer("Xiaomi", 512)
    save_comp = SaveComputer(inst_)
    save_comp.save_to_file()

