from src.product import Product


class Smartphone(Product):
    """Подкласс Smartphone - наследник класса Product для создания объекта 'смартфон'."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Конструктор для инициализации объекта (экземпляра класса). Т.е. для создания cмартфона."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

