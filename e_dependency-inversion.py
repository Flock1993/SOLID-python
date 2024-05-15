# Принцип инверсии зависимостей
# Класс должен зависеть от интерфейсов и абстрактных классов, а не от конкретных классов и функций
# Идёт речь об аргументах, особенно с ЯП со строгой типизацией
from abc import ABC


class ModelFormBad:
    def __init__(self, id_: int, old: int, first_name: str):
        self.id: int = id_
        self.old: int = old
        self.first_name: str = first_name


class PostgresBad:
    """Класс жестко завязан на ModelForm"""
    def save(self, model_: ModelFormBad):
        print(f"Запись формы в БД формы с id {model_.id}")


class WebframeworkBad:
    """Класс жестко завязан на ModelForm"""
    def save(self, model_: ModelFormBad):
        db = Postgres()
        db.save(model_)


# Рефакторинг ----------------------------------------------------------------------------------------------------------


class IForm(ABC):
    pass


class ISQL(ABC):
    pass


class ModelForm(IForm):
    def __init__(self, id_: int, old: int, first_name: str):
        self.id: int = id_
        self.old: int = old
        self.first_name: str = first_name


class Postgres(ISQL):
    def save(self, model_: IForm):
        print(f"Запись формы в БД формы с id {model_.id}")


class Webframework:
    def save(self, model_: IForm):
        db: ISQL = Postgres()
        db.save(model_)


if __name__ == '__main__':
    model = ModelForm(1, 27, "Matvey")
    framework = Webframework()
    framework.save(model)

