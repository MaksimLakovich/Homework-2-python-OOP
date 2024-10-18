from typing import Dict, List, Union


class Product:
    """Класс Product - шаблон для создания объекта продукт с данными конкретного товара"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Конструктор для инициализации объекта. Т.е. для создания экземпляра класса (объекта)"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: Dict[str, Union[str, float, int]]) -> "Product":
        """Класс-метод для создания объекта класса Product. Если продукт с таким именем уже существует,
        то обновляется его количество и цена в первоначальной записи.
        :param product_data: Параметры товара в словаре.
        :return: Object Product"""
        # # Также можно часть кода ниже заменить 1-й строкой с распаковкой словаря: "return cls(**product_data)"
        # # Но такой вариант вызовет ошибки mypy и является менее надежным и уязвимым, если на вход придут какие-либо
        # # иные типы данных или иная структура словаря.
        new_product = cls(
            name=str(product_data["name"]),
            description=str(product_data["description"]),
            price=float(product_data["price"]),
            quantity=int(product_data["quantity"]),
        )
        return new_product

    # # ДОДЕЛАТЬ КЛАСС-МЕТОД НА ПРЕДМЕТ ПРОВЕРКИ ДУБЛЯ ПРОДУКТА И СУММИРОВАНИЯ КОЛИЧЕСТВА
    # @classmethod
    # def new_product(
    #     cls, product_data: Dict[str, Union[str, float, int]], existing_products: List["Product"]
    # ) -> "Product":
    #     """Класс-метод для создания объекта класса Product. Если продукт с таким именем уже существует,
    #     то обновляется его количество и цена в первоначальной записи.
    #     :param product_data: Параметры товара в словаре.
    #     :param existing_products: Список существующих продуктов для проверки дубликатов.
    #     :return: Object Product"""
    #     # Проверяю наличие продукта с таким же именем и если есть, то обновляю кол-во и устанавливаю максимальную цену
    #     for product in existing_products:
    #         if product.name == product_data["name"]:
    #             product.quantity += int(product_data["quantity"])
    #             product.price = max(product.price, float(product_data["price"]))
    #             return product
    #     # Если дубликатов не найдено, создаю новый продукт
    #     new_product = cls(
    #         name=str(product_data["name"]),
    #         description=str(product_data["description"]),
    #         price=float(product_data["price"]),
    #         quantity=int(product_data["quantity"]),
    #     )
    #     return new_product
