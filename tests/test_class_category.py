from src.category import Category
from src.product import Product


def test_init_class_category_with_products(category_tv_with_products: Category) -> None:
    """Тест успешной инициализации объекта Category с продуктами (будут инициализированы объекты Product)."""
    assert category_tv_with_products.name == "Телевизоры"
    assert category_tv_with_products.description == "Современный телевизор позволяет наслаждаться просмотром"
    # Так как геттер в классе Category список продуктов возвращает строками, а не списком. И возвращает
    # каждый новый продукт с новой строки, то использую .split("\n") чтоб определить кол-во строк.
    assert len(category_tv_with_products.products.split("\n")) == 3


def test_init_class_category_without_products(category_smartphones_without_products: Category) -> None:
    """Тест успешной инициализации объекта Category без продуктов (пустой список продуктов).
    А также проверка работы геттера, который возвращает продукты в строке."""
    assert category_smartphones_without_products.name == "Смартфоны"
    assert category_smartphones_without_products.description == "Смартфоны, как средство многих других благ"
    assert category_smartphones_without_products.products == ""


def test_product_count_and_category_count(
    category_smartphones_without_products: Category, category_tv_with_products: Category
) -> None:
    """Тест счетчиков для подсчета количества категорий и для количества продуктов."""
    # product_count и category_count работает накопительным итогом (добавляются рез-ты предыдущих тестов)
    assert category_tv_with_products.product_count == 6
    assert category_tv_with_products.category_count == 4


def test_add_product(product_phone_samsung: Product, category_smartphones_without_products: Category) -> None:
    """Тест добавления продукта с помощью метода add_product."""
    # Проверяю, что до добавления нового продукта методом add_product() список пуст
    assert len(category_smartphones_without_products.products) == 0
    # Добавляю новый продукт и проверяю изменения
    category_smartphones_without_products.add_product(product_phone_samsung)
    # Так как геттер в классе Category список продуктов возвращает строками, а не списком. И возвращает
    # каждый новый продукт с новой строки, то использую .split("\n") чтоб определить кол-во строк.
    assert len(category_smartphones_without_products.products.split("\n")) == 1
    # product_count работает накопительным итогом (добавляются рез-ты предыдущих тестов)
    assert category_smartphones_without_products.product_count == 7
