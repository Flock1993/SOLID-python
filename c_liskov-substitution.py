# Принцип подстановки Барбары-Лисков
# Подклассы должны заменять свои базовые классы.
# То есть дочерний класс должен полностью повторять функционал методов базового класса
# Функционал можно расширять, но не менять.
# Если в функции можно использовать родительский класс, то подставив дочерний класс функций не должна сломаться

# Пример 1
class Computer:
    def __init__(self, name: str, memory_size: int):
        self.name: str = name
        self.memory_size: int = memory_size

    def set_data(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.name=} {self.memory_size=}"


class LaptopBad(Computer):
    """Нарушает принцип Лисков, так как изменяет поведение метода, описанного в базовом классе"""
    def set_data(self, name: str):
        self.name = name
        self.memory_size = 1024


class Laptop(Computer):
    def set_data(self, name: str):
        self.name = name


# TODO Пример 2 с плавающей, летающей птицей https://youtu.be/gy-9ml_2Pz8?si=Lk5Toco6UnMpZZjX


if __name__ == '__main__':
    inst = LaptopBad("Xiaomi", 128)
    print(inst)
    inst.set_data("Apple")
    print(inst)

