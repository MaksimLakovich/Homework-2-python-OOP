from src.smartphone import Smartphone


def test_init_class_product(product_from_class_smartphone: "Smartphone") -> None:
    """Тест успешной работы конструктора класса по инициализации объекта Smartphone."""
    assert product_from_class_smartphone.name == "Iphone 15"
    assert product_from_class_smartphone.description == "512GB, Gray space"
    assert product_from_class_smartphone.price == 210000.0
    assert product_from_class_smartphone.quantity == 8
    assert product_from_class_smartphone.efficiency == 98.2
    assert product_from_class_smartphone.model == "15"
    assert product_from_class_smartphone.memory == 512
    assert product_from_class_smartphone.color == "Gray space"
