import json
from unittest.mock import mock_open, patch

from src.create_products_and_categories_from_json import read_json_file


def test_read_json_data(
    fixture_for_expected_json_data: list[dict], fixture_for_expected_path_to_json_file: str
) -> None:
    """Тест успешного чтения данных"""

    mock_data = json.dumps(fixture_for_expected_json_data)
    # Мокаем функцию open и возвращаем данные из фикстуры
    with patch("builtins.open", mock_open(read_data=mock_data)):
        # Мокаем функцию os.path.exists
        with patch("os.path.exists", return_value=True):
            data = read_json_file(fixture_for_expected_path_to_json_file)
            assert data == fixture_for_expected_json_data


def test_json_file_not_found(fixture_for_expected_path_to_json_file: str) -> None:
    """Тест на случай, если файл не найден"""

    # Мокаем вызов функции open, чтобы она выбросила ошибку FileNotFoundError
    with patch("builtins.open", mock_open()) as mocked_open:
        mocked_open.side_effect = FileNotFoundError  # Симулируем ошибку "файл не найден"
        data = read_json_file(fixture_for_expected_path_to_json_file)
        assert data == []  # Ожидаем пустой список


def test_file_json_with_invalid_data(fixture_for_expected_path_to_json_file: str) -> None:
    """Тест на случай, если файл содержит некорректный JSON"""

    # Мокаем функцию open, чтобы файл содержал некорректные JSON-данные
    with patch("builtins.open", mock_open(read_data="invalid json")):
        data = read_json_file(fixture_for_expected_path_to_json_file)
        assert data == []  # Ожидаем пустой список


def test_file_json_not_a_list(fixture_for_expected_path_to_json_file: str) -> None:
    """Тест на случай, если JSON содержит не список"""

    # Мокаем функцию open, чтобы JSON содержал не список, а другой тип данных
    mock_data = json.dumps({"not": "a list"})  # Подделываем данные, чтобы это был не список
    with patch("builtins.open", mock_open(read_data=mock_data)):
        data = read_json_file(fixture_for_expected_path_to_json_file)
        assert data == []  # Ожидаем пустой список

