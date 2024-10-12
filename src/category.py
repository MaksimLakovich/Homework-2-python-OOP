class Category:
    """Класс Product - шаблон для создания объектов"""

    name: str
    description: str
    products: list

    def __init__(self, name: str, description: str, products: list) -> None:
        """Конструктор для инициализации объекта. Т.е. для создания экземпляра класса (объекта)"""
        self.name = name
        self.description = description
        self.products = products  # ВАРИАНТ С ПУСТЫМ СПИСКОМ
