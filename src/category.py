class Category:
    """Класс Product - шаблон для создания объекта с данными какой-либо категории под товары"""

    name: str
    description: str
    products: None | list  # Категория товаров может быть создана и без товаров в ней

    category_count = 0  # Атрибут класса: подсчет общего количества категорий
    product_count = 0  # Атрибут класса: подсчет общего количества позиций товаров (не складские остатки)

    def __init__(self, name: str, description: str, products: None | list = None) -> None:
        """Конструктор для инициализации объекта. Т.е. для создания экземпляра класса (объекта)"""
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0
