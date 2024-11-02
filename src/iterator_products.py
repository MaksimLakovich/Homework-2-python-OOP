from typing import Iterator

from src.category import Category

# from src.product import Product


class ProductsIteratorInCategory:
    """Класс для перебора продуктов одной категории (например, в цикле for). Класс принимает на вход
    объект класса категории и производит итерацию по продуктам, которые хранятся в данной категории."""

    def __init__(self, category: "Category") -> None:
        """Конструктор класса."""
        self.category = category
        self.index = 0
        # В классе Category список объектов "Продукты (Product)" сделан приватным атрибутом и реализован геттер,
        # который возвращает список продуктов в строковом представлении. Защищенным методом в данном классе
        # я эту строку от геттера сделаю списком со строками равным продуктам (т.е. не одна строка на все продукты,
        # а под каждый продукт отдельная строка) чтоб можно было выполнить итерацию по списку продуктов.
        self.list_products = self._extract_products()

    def __iter__(self) -> Iterator[str]:
        """Магический метод получения итератора для перебора объектов в реализуемом протоколе итерации."""
        # Если сбрасывать в итераторе индекс (т.е., установить 0), то каждый for
        # будет выдавать результат заново, а не только первый for.
        self.index = 0
        return self

    def __next__(self) -> str:
        """Магический метод перехода к следующему значению в реализуемом протоколе итерации."""
        if self.index < len(self.list_products):
            iter_product = self.list_products[self.index]
            self.index += 1
            return iter_product
        else:
            raise StopIteration

    def _extract_products(self) -> list[str]:
        """Метод парсинга строки, которая возвращается геттером, для получения списка объектов Product из строки,
        возвращаемой методом Category.products (смотри код класса Category)."""
        return self.category.products.split("\n")


# if __name__ == "__main__":
#     product_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 80)
#     product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     phone_category = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product_1, product_2, product_3]
#     )
#
#     iterate_products = ProductsIteratorInCategory(phone_category)
#
#     # ПРОВЕРКА ТОГО КАК ЗАЩИЩЕННЫЙ МЕТОД СОЗДАЛ ИЗ СТРОКИ СПИСОК ПРОДУКТОВ (_extract_products):
#     print(iterate_products.list_products)
#
#     # ПРОВЕРКА ИТЕРАЦИИ:
#     for product in iterate_products:
#         print(product)
#     # ПРОВЕРКА ПОВТОРНОЙ ИТЕРАЦИИ КОГДА УСТАНОВЛЕН СБРОС ИТЕРАЦИИ (self.index = 0):
#     for product in iterate_products:
#         print(product)