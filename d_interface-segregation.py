# Принцип разделения интерфейса
# Нужно создавать узкоспециализированные интерфейсы, предназначенные для конкретного клиента
# Т.е. не нужно создавать абстрактные классы со множеством методов.
# Клиенты не должны зависеть от интерфейсов которые они используют
# Клиенты не должны зависеть от методов, которые они не используют
from abc import ABC, abstractmethod


class ShapeBad(ABC):
    @abstractmethod
    def draw_line(self):
        pass

    @abstractmethod
    def draw_circle(self):
        pass

    @abstractmethod
    def draw_rect(self):
        pass


class LineBad(ShapeBad):
    """Обязаны реализовывать все три интерфейса"""
    def draw_line(self):
        print(f"Рисование линии")

    def draw_circle(self):
        pass

    def draw_rect(self):
        pass


class CircleBad(ShapeBad):
    def draw_line(self):
        pass

    def draw_circle(self):
        print(f"Рисование круга")

    def draw_rect(self):
        pass

# Рефакторинг ----------------------------------------------------------------------------------------------------------


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Line(Shape):
    def draw(self):
        print(f"Рисование линии")


class Circle(Shape):
    def draw(self):
        print(f"Рисование круга")


if __name__ == '__main__':
    pass
