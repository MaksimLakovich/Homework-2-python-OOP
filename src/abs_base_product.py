from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс BaseProduct для создания в классе Product объекта 'продукт'.
    Выделена общая функциональность, которая должна быть у каждого объекта 'продукт'."""

    @abstractmethod
    def __init__(self) -> None:
        """Конструктор для инициализации объекта класса Product (экземпляра класса). Т.е. для создания продукта."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Магический метод для возврата продукта в строковом отображении.
        :return: Строка в заданном формате."""
        pass

    @abstractmethod
    def __add__(self, other: object) -> float:
        """Магический метод сложения общей цены у двух продуктов (кол-во на складе продуктов умноженное на цену).
        :return: Итоговая цифра в формате float."""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict) -> object:
        """Класс-метод для создания объекта класса Product по входящим данным из СЛОВАРЯ.
        :param product_data: Словарь с данными создаваемого продукта.
        :return: Object Product"""
        pass
