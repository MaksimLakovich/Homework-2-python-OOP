import pytest

from src.lawn_grass import LawnGrass
from src.smartphone import Smartphone


def test_mixin_print_init_info(
    capsys: pytest.CaptureFixture,
    product_from_class_smartphone: "Smartphone",
    product_from_class_lawngrass: "LawnGrass",
) -> None:
    """Тест успешного вывода в консоль информации из миксин MixinPrintInitInfo о том,
    от какого класса и с какими параметрами был создан объект."""
    message = capsys.readouterr()
    assert (
        message.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)\n"
        "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
    )
