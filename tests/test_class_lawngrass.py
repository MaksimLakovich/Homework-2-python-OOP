from src.lawn_grass import LawnGrass


def test_init_class_lawngrass(product_from_class_lawngrass: "LawnGrass") -> None:
    """Тест успешной работы конструктора класса по инициализации объекта Lawn grass."""
    assert product_from_class_lawngrass.name == "Газонная трава"
    assert product_from_class_lawngrass.description == "Элитная трава для газона"
    assert product_from_class_lawngrass.price == 500.0
    assert product_from_class_lawngrass.quantity == 20
    assert product_from_class_lawngrass.country == "Россия"
    assert product_from_class_lawngrass.germination_period == "7 дней"
    assert product_from_class_lawngrass.color == "Зеленый"

