from typing import Dict, Union


def confirm_price_reduction() -> bool:
    """Функция подтверждения понижения цены от пользователя."""
    user_solution = input("Подтверждаете понижение цены? ('y' - да / 'n' - нет): ").strip().lower()
    return user_solution == "y"


class Product:
    """Класс Product - шаблон для создания объекта 'продукт'."""

    name: str
    description: str
    # # После того как сделали ПРИВАТНЫМ price нужно убрать аннотацию price из тела класса,
    # # просто закомментировал и оставил это для себя:
    # price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Конструктор для инициализации объекта (экземпляра класса). Т.е. для создания продукта."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Магический метод для возврата продукта в строковом отображении.
        :return: Строка в заданном формате."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Магический метод сложения общей цены у двух продуктов (кол-во на складе продуктов умноженное на цену)."""
        if type(other) is self.__class__:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_data: Dict[str, Union[str, float, int]]) -> "Product":
        """Класс-метод для создания объекта класса Product по входящим данным из СЛОВАРЯ.
        :param product_data: Словарь с данными создаваемого продукта.
        :return: Object Product"""
        # Также можно часть кода ниже заменить 1-й строкой с распаковкой словаря: "return cls(**product_data)"
        # Но такой вариант вызовет ошибки mypy и является менее надежным и уязвимым, если на вход придут какие-либо
        # иные типы данных или иная структура словаря.
        new_product = cls(
            name=str(product_data["name"]),
            description=str(product_data["description"]),
            price=float(product_data["price"]),
            quantity=int(product_data["quantity"]),
        )
        return new_product

    # # ДОДЕЛАТЬ КЛАСС-МЕТОД НА ПРЕДМЕТ ПРОВЕРКИ ДУБЛЯ ПРОДУКТА И СУММИРОВАНИЯ КОЛИЧЕСТВА
    # @classmethod
    # def new_product(
    #     cls, product_data: Dict[str, Union[str, float, int]], existing_products: List["Product"]
    # ) -> "Product":
    #     """Класс-метод для создания объекта класса Product. Если продукт с таким именем уже существует,
    #     то обновляется его количество и цена в первоначальной записи.
    #     :param product_data: Параметры товара в словаре.
    #     :param existing_products: Список существующих продуктов для проверки дубликатов.
    #     :return: Object Product"""
    #     # Проверяю наличие продукта с таким же именем и если есть, то: обновляю кол-во, устанавливаю максимальн. цену
    #     for product in existing_products:
    #         if product.name == product_data["name"]:
    #             product.quantity += int(product_data["quantity"])
    #             product.price = max(product.price, float(product_data["price"]))
    #             return product
    #     # Если дубликатов не найдено, создаю новый продукт
    #     new_product = cls(
    #         name=str(product_data["name"]),
    #         description=str(product_data["description"]),
    #         price=float(product_data["price"]),
    #         quantity=int(product_data["quantity"]),
    #     )
    #     return new_product

    @property
    def price(self) -> float:
        """Геттер для получения цены продукта, которая ранее была сделана приватным свойством класса.
        :return: Возвращает цену продукта."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для проверки корректности цены (не отрицательное, не ноль) и подтверждения новой пониженной цены.
        :param new_price: Новая цена."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            if confirm_price_reduction():
                self.__price = new_price
        else:
            self.__price = new_price
