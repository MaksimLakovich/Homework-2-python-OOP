from typing import Dict, Union


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
        """Класс-метод для создания объекта класса Product.
        :param product_data: Параметры товара в словаре.
        :return: Object Product"""
        product = cls(
            name=str(product_data["name"]),
            description=str(product_data["description"]),
            price=float(product_data["price"]),
            quantity=int(product_data["quantity"]),
        )
        return product
