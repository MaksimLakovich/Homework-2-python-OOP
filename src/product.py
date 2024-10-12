class Product:
    """Класс Product - шаблон для создания объектов"""

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


# if __name__ == "__main__":
#     prod_1 = Product("Nokia", "Орехокол", 10.99, 6)
#     print(prod_1)
#     print(prod_1.name)
#     print(prod_1.description)
#     print(prod_1.price)
#     print(prod_1.quantity)
