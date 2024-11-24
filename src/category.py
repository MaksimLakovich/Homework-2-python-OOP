from itertools import product
from typing import Optional

from src.product import Product


class Category:
    """Класс Category - шаблон для создания объекта 'категория'."""

    name: str
    description: str
    # # После того как сделали ПРИВАТНЫМ products нужно убрать аннотацию products из тела класса,
    # # просто закомментировал и оставил это для себя:
    # products: Optional[list]  # Категория товаров может быть создана и без товаров в ней
    category_count = 0  # Атрибут класса: подсчет общего количества категорий
    product_count = 0  # Атрибут класса: подсчет общего количества позиций товаров (не складские остатки)

    def __init__(self, name: str, description: str, products: Optional[list] = None) -> None:
        """Конструктор для инициализации нового объекта (экземпляра класса). Т.е. для создания категории."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        """Магический метод для вывода количества продуктов в данной категории (общее кол-во всех продуктов на складе).
        :return: Строка в заданном формате."""
        # # ПРОСТОЙ ВАРИАНТ ЗАПИСИ СУММИРОВАНИЯ ПРОДУКТОВ:
        # self.total_quantity = 0
        # for product in self.__products:
        #     self.total_quantity += product.quantity
        self.total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {self.total_quantity} шт."

    def add_product(self, new_product: "Product") -> None:
        """Метод класса для добавления нового продукта в категорию.
        :type new_product: Object Product."""
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError("Возникла ошибка TypeError при добавлении не продукта")

    @property
    def products(self) -> str:
        """Геттер для вывода списка продуктов, который ранее был сделан приватным свойством класса.
        :return: Возвращает все продукты в строке, где каждый продукт с новой строки."""
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]
        )

    def middle_price(self) -> float:
        """Метод для вычисления среднего ценника всех продуктов в категории.
        :return: Средний ценник продуктов или 0, если продуктов нет."""
        try:
            return float(sum(product.price for product in self.__products) / len(self.__products))
        except ZeroDivisionError:
            return 0
