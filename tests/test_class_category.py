from src.category import Category


def test_init_class_category_with_products(category_tv_with_products: Category) -> None:
    """Тест успешной инициализации объекта Category с продуктами (будут инициализированы объекты Product)"""

    assert category_tv_with_products.name == "Телевизоры"
    assert category_tv_with_products.description == "Современный телевизор позволяет наслаждаться просмотром"
    assert len(category_tv_with_products.products) == 3


def test_init_class_category_without_products(category_smartphones_without_products: Category) -> None:
    """Тест успешной инициализации объекта Category без продуктов (пустой список продуктов)"""

    assert category_smartphones_without_products.name == "Смартфоны"
    assert category_smartphones_without_products.description == "Смартфоны, как средство многих других благ"
    assert category_smartphones_without_products.products == []


def test_product_count_and_category_count(
    category_smartphones_without_products: Category, category_tv_with_products: Category
) -> None:
    """Тест счетчиков для подсчета количества категорий и для количества продуктов"""

    assert category_tv_with_products.product_count == 6
    assert category_tv_with_products.category_count == 4
