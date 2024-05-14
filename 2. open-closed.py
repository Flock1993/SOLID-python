# Принцип открытости-закрытости
# Класс закрыт для модификации, но открыт для расширения
# Полиморфизм + абстрактные классы
from abc import ABC, abstractmethod

class Save(ABC):
    @abstractmethod
    def save(self):
        pass




if __name__ == '__main__':


