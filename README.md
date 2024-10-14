# E-COMMERCE: Проект по разработке ядра для интернет-магазина


## 1. Цель проекта:
E-commerce — электронная торговля, или электронная коммерция. На данном этапе работы мы подготовим всё для того, чтобы у нас появилось ядро для интернет-магазина. В дальнейшем для этого ядра возможно будет реализовать любой интерфейс — от сайта до телеграм-бота.


## 2. Описание классов:

1. ***product.py***: содержит класс `Product` - шаблон для создания объекта с данными конкретного товара.

   Конструктор класса требует следующий набор параметров:
   - **name:** str
   - **description:** str
   - **price:** float
   - **quantity:** int

2. ***category.py***: содержит класс `Category` - шаблон для создания объекта с данными какой-либо категории под товары.

   Конструктор класса требует следующий набор параметров:
   - **name:** str
   - **description:** str
   - **products:** None | list
   - **category_count = 0** (Атрибут класса: подсчет общего количества категорий)
   - **product_count = 0** (Атрибут класса: подсчет общего количества позиций товаров (не складские остатки))


## 3. Описание модулей:

1. ***create_products_and_categories_from_json.py*** - содержит две функции:
   - функция `read_json_file`: чтение данных по категориям и товарам из файла JSON.
     - :param file_name: На вход получаем текстовое имя файла, который должен быть в папке data в корне проекта.
     - :return: На выводе отдаем преобразованные данные в формат Python.
   - функция `create_objects_product_and_category_from_json`: создание объектов класса Product и Category из прочитанных данных json.
     - :param input_data: На вход получаем прочитанные и преобразованные в формат Python данные.
     - :return: На выходе отдаем список экземпляров класса Category и вложенных в них экземпляров класса Product.


## 4. Установка проекта:
1. Клонируйте репозиторий:
```
git clone https://github.com/MaksimLakovich/Homework-2-python-OOP
```

2. Установите зависимости:
```
poetry install
```


## 5. Модульное тестирование:

1. Тесты подготовлены отдельными файлами под каждый класс и модуль проекта:
   - _test_class_product.py_
   - _test_class_category.py_
   - _test_modul_create_class_from_json.py_

 
2. Для повышения качества тестирования используются фикстуры (файл: conftest.py) и параметризация тестов.

### Запуск тестирования:
1. Установить `pytest` в группу dev через Poetry:
```
poetry add --group dev pytest
```
2. Запустить выполнение тестов:
```
pytest -v
```

### Анализ покрытия кода тестами:
1. Установить `pytest-cov` в группу dev через Poetry:
```
poetry add --group dev pytest-cov
```
2. Запустить выполнение тестов:
```
pytest --cov=tests
```


## 6. Логирование модулей:

1. Реализована запись логов в файл для следующих модулей проекта:
   - модуль `create_products_and_caregories_fromjson.py`.
2. Логи записываются в папку ***logs*** в корне проекта;
3. Формат записи лога в файл включает метку времени, название модуля, уровень серьезности и сообщение, описывающее событие или ошибку, которые произошли; 
4. Лог перезаписывается при каждом запуске приложения.