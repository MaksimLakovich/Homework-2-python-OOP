import json
import logging
import os
from pathlib import Path

from src.category import Category
from src.product import Product

# Для логов определяю корневую директорию проекта (это вариант 1, а ниже в функции есть вариант 2 как еще можно)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_directory = os.path.join(BASE_DIR, "logs")
log_file = os.path.join(log_directory, "read_json_file_and_create_objects_product_and_category.log")

# Проверяем, существует ли директория logs, и создаем ее, если нет
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logger_read_json_and_create_objects = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file, "w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger_read_json_and_create_objects.addHandler(file_handler)
logger_read_json_and_create_objects.setLevel(logging.DEBUG)


def read_json_file(file_name: str) -> list:
    """Функция для чтения данных по категориям и товарам из файла JSON.
    :param file_name: На вход получаем текстовое имя файла, который должен быть в папке data в корне проекта.
    :return: На выводе отдаем преобразованные данные в формат Python."""

    logger_read_json_and_create_objects.info("Начат процесс поиска json-файла")
    BASE_DIR = Path(__file__).resolve().parent.parent  # Определяю директорию проекта
    path_to_json = BASE_DIR / "data" / file_name  # Определяю путь к файлу

    try:
        logger_read_json_and_create_objects.debug("Json-файл найден и начат процесс считывания данных")
        with open(path_to_json, "r", encoding="utf-8") as file:
            try:
                input_data = json.load(file)  # Загружаю данные из формата JSON и преобразую их в объект Python
                if isinstance(input_data, list):
                    logger_read_json_and_create_objects.debug("Данные успешно считаны и возвращены в формате Python")
                    return input_data
                else:
                    logger_read_json_and_create_objects.debug(f"В файле '{file_name}' данные не в формате списка")
                    return []
            except json.JSONDecodeError as info:
                logger_read_json_and_create_objects.error(f"Возвращен пустой список (проблема с декодировкой: {info})")
                return []
    except FileNotFoundError:
        logger_read_json_and_create_objects.error(f"Возвращен пустой список (файл не найден: {path_to_json})")
        return []


def create_objects_product_and_category_from_json(input_data: list) -> list:
    """Функция для создания объектов класса Product и Category из прочитанных данных json.
    :param input_data: На вход получаем прочитанные и преобразованные в формат Python данные.
    :return: На выходе отдаем список экземпляров класса Category и вложенных в них экземпляров класса Product."""

    categories = []

    logger_read_json_and_create_objects.info("Начат процесс создания объектов класса Product и Category из файла")
    for category in input_data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    logger_read_json_and_create_objects.info("Объекты класса Product и Category созданы и возвращены списком")
    return categories


# # Проверка работы модуля:
# if __name__ == "__main__":
#
#     # проверка чтения файла
#     data = read_json_file("products.json")
#     print(data)
#
#     # проверка чтения созданных экземпляров класса
#     class_data = create_objects_product_and_category_from_json(data)
#     print(class_data)
#
#     # выборочно проверяю корректное отображение значения из класса (тут смотрю имя 3-го продукта в 1-й категории)
#     print(class_data[0].products[2].name)
