from src.product import Product


class LawnGrass(Product):
    """Подкласс LawnGrass - наследник класса Product для создания объекта 'Трава газонная'."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Конструктор для инициализации объекта (экземпляра класса). Т.е. для создания травы газонной."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
