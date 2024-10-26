import pytest
import os

from src.category import Category
from src.product import Product


@pytest.fixture
def product_phone_samsung():
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def product_phone_xiaomi():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )


@pytest.fixture
def product_from_dictionary():
    return {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }


@pytest.fixture
def category_tv_with_products():
    return Category(
        name="Телевизоры",
        description="Современный телевизор позволяет наслаждаться просмотром",
        products=[
            Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7),
            Product("32", "Среднее качество картинки", 35000.0, 2),
            Product("65\" FULL HD", "Фоновая подсветка", 105000.0, 4),
        ]
    )


@pytest.fixture
def category_smartphones_without_products():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство многих других благ",
        products=None
    )


@pytest.fixture
def fixture_for_expected_json_data():
    return [
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {
                    "name": "55\" QLED 4K",
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7
                }
            ]
        }
    ]


@pytest.fixture
def fixture_for_expected_path_to_json_file():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "products.json")
