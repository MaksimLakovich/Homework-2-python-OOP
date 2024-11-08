from typing import Generic, Protocol, TypeVar


class PrintableProduct(Protocol):
    """Создаю интерфейс PrintableProduct, который указывает, что любой класс, реализующий его должен иметь атрибуты
    name, description, price, quantity. Миксин может затем требовать, чтобы класс-наследник соответствовал этому
    интерфейсу. Это необходимо так как при проверке mypy он требует у MixinPrintInitInfo, что у объектов, которые его
    наследуют, будут атрибуты name, description, price, quantity. Но mypy не может это гарантировать, так как
    MixinPrintInitInfo сам по себе не имеет этих атрибутов. Тут и помогает этот PrintableProduct."""

    name: str
    description: str
    price: float
    quantity: int


# Чтобы mypy корректно распознавал, что эти атрибуты появятся только в классах, которые реализуют PrintableProduct,
# можно указать, что класс MixinPrintInitInfo должен использоваться только с классами, совместимыми с PrintableProduct.
# Это делается с помощью Generic и TypeVar. Тогда mypy сможет связать типы и корректно проверить атрибуты.
# Решение с использованием Generic и TypeVar:
# 1) Создаю тип T, который будет представлять любой класс, совместимый с PrintableProduct.
# 2) Сделаю MixinPrintInitInfo обобщенным классом (Generic), где T является подтипом PrintableProduct

T = TypeVar("T", bound=PrintableProduct)

# T = TypeVar("T", bound=PrintableProduct) означает, что T может быть любым типом, который реализует PrintableProduct.
# MixinPrintInitInfo(Generic[T]) — теперь mypy понимает, что любые классы, использующие MixinPrintInitInfo, будут
# совместимы с PrintableProduct и должны содержать указанные атрибуты


class MixinPrintInitInfo(Generic[T]):
    """Класс-миксин для печати в консоли информации о том, от какого класса и с какими параметрами был создан объект.
    То есть печатать работу методов __init__ в классах."""

    def __init__(self: T) -> None:
        print(repr(self))

    def __repr__(self: T) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
