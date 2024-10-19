from typing import Optional

from src.product import Product


class Category:
    """Класс Category - шаблон для создания объекта с данными какой-либо категории товаров."""

    name: str
    description: str
    # # После того как сделали ПРИВАТНЫМ products нужно убрать аннотацию products из тела класса,
    # # просто закомментировал и оставил это для себя:
    # products: Optional[list]  # Категория товаров может быть создана и без товаров в ней

    category_count = 0  # Атрибут класса: подсчет общего количества категорий
    product_count = 0  # Атрибут класса: подсчет общего количества позиций товаров (не складские остатки)

    def __init__(self, name: str, description: str, products: Optional[list] = None) -> None:
        """Конструктор для инициализации нового объекта категория (нового экземпляра класса)."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, new_product: "Product") -> None:
        """Метод класса для добавления нового продукта в категорию товаров.
        :type new_product: Object Product."""
        self.__products.append(new_product)
        Category.product_count += 1

    # # Условия ЗАДАНИЯ 2 в ДЗ 14.2 немного запутанные, поэтому вот еще вариант реализации ГЕТТЕРА,
    # # если необходимо все-таки выводить строки продуктов в СПИСКЕ, а не просто строками:
    # @property
    # def products(self) -> list:
    #     str_products = []
    #     for product in self.__products:
    #         str_products.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
    #     return str_products

    @property
    def products(self) -> str:
        """Геттер для вывода списка продуктов, который ранее был сделан приватным свойством класса.
        :return: Возвращает все продукты в строке, где каждый продукт с новой строки."""
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]
        )
