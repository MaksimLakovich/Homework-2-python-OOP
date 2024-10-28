# E-COMMERCE: Проект по разработке ядра для интернет-магазина


## 1. Цель проекта:
E-commerce — электронная торговля, или электронная коммерция. На данном этапе работы мы подготовим всё для того, чтобы у нас появилось ядро для интернет-магазина. В дальнейшем для этого ядра возможно будет реализовать любой интерфейс — от сайта до телеграм-бота.


## 2. Описание классов:

1. ***product.py***: содержит класс `Product` - шаблон для создания объекта с данными конкретного товара. 
   - Конструктор класса требует следующий набор параметров:
      - **name:** str
      - **description:** str
      - **__price:** float
      - **quantity:** int
   - Класс-метод `new_product()` для создания объекта класса Product по входящим данным из словаря (dict).
   - `геттер` для получения цены.
   - `сеттер` для установления цены (с проверкой корректности цены (не отрицательное, не ноль) и подтверждением в случае ее понижения).
   - Магический метод `__str__` для возврата продукта в строковом отображении в формате: *"Название продукта, X руб. Остаток: X шт."*.
   - Магический метод `__add__` для сложения общей цены у двух продуктов (кол-во на складе продуктов умноженное на цену).


2. ***category.py***: содержит класс `Category` - шаблон для создания объекта с данными какой-либо категории под товары.
   - Конструктор класса требует следующий набор параметров:
      - **name:** str
      - **description:** str
      - **__products:** None | list
      - **category_count = 0** (Атрибут класса: подсчет общего количества категорий)
      - **product_count = 0** (Атрибут класса: подсчет общего количества позиций товаров (не складские остатки))
   - Метод класса `add_product()` для добавления нового продукта (object Product) в категорию товаров.
   - `геттер` для вывода списка продуктов в формате строки, который ранее был сделан приватным свойством класса.
   - Магический метод `__str__` для возврата продукта в строковом отображении в формате: *"Название категории, количество продуктов: X шт."*.


3. ***iterator_products.py***: содержит вспомогательный класс `ProductsIteratorInCategory` с помощью которого можно перебирать продукты одной категории (например в цикле for). Для этого данный вспомогательный класс принимает на вход объект класса категории и производит итерацию по продуктам, которые хранятся в данной категории.

   То есть метод выполнения следующего шага итерации возвращает очередной продукт из категории.
   - Конструктор класса требует следующий набор параметров:
      - **category:** Object Category
      - **list_products:** защищенный метод _extract_products()
      - **self.index = 0:** устанавливаем ноль для процедуры сброса индекса.
   - Метод класса `_extract_products()` для парсинга строки, которая возвращается геттером, для получения списка объектов Product из строки, возвращаемой методом Category.products (смотри код класса Category).
   - Магический метод `__iter__` для получения итератора для перебора объектов в реализуемом протоколе итерации.
      - **self.index = 0:** если сбрасывать в итераторе индекс (т.е., установить 0), то каждый for будет выдавать результат заново, а не только первый for.
   - Магический метод `__next__` для перехода к следующему значению в реализуемом протоколе итерации.



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
