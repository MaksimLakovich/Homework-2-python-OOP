from src.product import Product


def test_init_class_product(product_phone_samsung: Product) -> None:
    """Тест успешной инициализации объекта Product"""

    assert product_phone_samsung.name == "Samsung Galaxy C23 Ultra"
    assert product_phone_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_phone_samsung.price == 180000.0
    assert product_phone_samsung.quantity == 5
