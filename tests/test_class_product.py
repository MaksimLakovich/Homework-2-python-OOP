from unittest.mock import MagicMock, patch

import pytest

from src.lawn_grass import LawnGrass
from src.product import Product, confirm_price_reduction
from src.smartphone import Smartphone


def test_init_class_product(product_phone_samsung: "Product") -> None:
    """Тест успешной работы конструктора класса по инициализации объекта Product."""
    assert product_phone_samsung.name == "Samsung Galaxy C23 Ultra"
    assert product_phone_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_phone_samsung.price == 180_000.0
    assert product_phone_samsung.quantity == 5


def test_create_class_from_dictionary(product_from_dictionary: dict) -> None:
    """Тест успешной работы класс-метода new_product по инициализации объекта Product."""
    test_product_1 = Product.new_product(product_from_dictionary)
    assert test_product_1.name == "Samsung Galaxy C23 Ultra"
    assert test_product_1.description == "256GB, Серый цвет, 200MP камера"
    assert test_product_1.price == 180_000.0
    assert test_product_1.quantity == 5


def test_get_price(product_phone_samsung: "Product") -> None:
    """Тест работы геттера для получения цены, которая ранее была сделана приватным свойством класса."""
    assert product_phone_samsung.price == 180_000.0


def test_set_new_higher_price(product_phone_samsung: "Product") -> None:
    """Тест установления более высокой цены для существующего продукта."""
    product_phone_samsung.price = 1_000_000
    assert product_phone_samsung.price == 1_000_000


@patch("src.product.confirm_price_reduction", return_value=True)
def test_set_new_lower_price_with_confirmation(mock_confirm: MagicMock, product_phone_samsung: "Product") -> None:
    """Тест установления более низкой цены для существующего продукта с подтверждением."""
    # Замокал (подменил) confirm_price_reduction и теперь он всегда возвращает True
    product_phone_samsung.price = 1_000
    assert product_phone_samsung.price == 1_000


@patch("src.product.confirm_price_reduction", return_value=False)
def test_set_new_lower_price_without_confirmation(mock_confirm: MagicMock, product_phone_samsung: "Product") -> None:
    """Тест отказа от установления более низкой цены для существующего продукта."""
    # Замокал (подменил) confirm_price_reduction и теперь он всегда возвращает False
    product_phone_samsung.price = 1_000
    assert product_phone_samsung.price == 180_000


def test_set_negative_price(product_phone_samsung: "Product") -> None:
    """Тест невозможности установить отрицательную цену и сохранение предыдущей старой цены."""
    product_phone_samsung.price = -100
    assert product_phone_samsung.price == 180_000


def test_set_zero_price(product_phone_samsung: "Product") -> None:
    """Тест невозможности установить нулевую цену и сохранение предыдущей старой цены."""
    product_phone_samsung.price = 0
    assert product_phone_samsung.price == 180_000


# Замокал функцию print
@patch("builtins.print", return_value="Цена не должна быть нулевая или отрицательная")
def test_warning_print_for_zero_and_negative_price(mock_print: MagicMock, product_phone_samsung: "Product") -> None:
    """Тест проверки вывода ошибки через print."""
    product_phone_samsung.price = 0
    # Проверяю, что print был вызван один раз с нужным сообщением
    mock_print.assert_called_once_with("Цена не должна быть нулевая или отрицательная")
    assert product_phone_samsung.price == 180_000


# Замокал функцию input
@patch("builtins.input", return_value="y")
def test_confirm_price_reduction(mock_input: MagicMock) -> None:
    """Тест функции confirm_price_reduction, когда пользователь вводит 'y' для подтверждения понижения цены."""
    assert confirm_price_reduction() is True
    # Проверяю, что input был вызван один раз
    mock_input.assert_called_once()


def test_magic_method_product_in_string(product_phone_samsung: "Product") -> None:
    """Тест магического метода вывода данных о продукте в строковом отображении."""
    assert str(product_phone_samsung) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_magic_method_addition_obj_products(product_phone_samsung: "Product", product_phone_xiaomi: "Product") -> None:
    """Положительный тест магического метода сложения экземпляров класса продукт."""
    assert product_phone_samsung + product_phone_xiaomi == 1334000


def test_magic_method_addition_exception(
    product_from_class_smartphone: "Smartphone", product_from_class_lawngrass: "LawnGrass"
) -> None:
    """Негативный тест магического метода сложения и возбуждения исключения."""
    with pytest.raises(TypeError) as info_expectation:
        product_from_class_smartphone + product_from_class_lawngrass
    assert str(info_expectation.value) == "Возникла ошибка TypeError при попытке сложения"


def test_if_quantity_is_null() -> None:
    """Тест ValueError в конструкторе, если создают продукт с нулевым количеством."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
