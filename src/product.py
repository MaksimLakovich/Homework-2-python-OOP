class Product:
    """Класс Product - шаблон для создания объекта с данными конкретного товара"""

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
