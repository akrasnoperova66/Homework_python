import pytest
from string_utils import StringUtils


string_utils = StringUtils()

#позитивные тесты
#первая утилита - capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

#вторая утилита - trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "skypro"),
    ("  hello world", "hello world"),
    ("  python ", "python "),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

#третья утилита - contains
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol_str, expected_bool", [
    ("skypro", "w", False),
    ("skypro", "pro", True),
])
def test_contains_pozitive(input_str, symbol_str, expected_bool):
    assert string_utils.contains(input_str, symbol_str) == expected_bool

#четвертая утилита - delete
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol_str, expected", [
    ("skypro", "k", "sypro"),
    ("hello world", "llo", "he world"),
])
def test_delete_pozitive(input_str, symbol_str, expected):
    assert string_utils.delete_symbol(input_str, symbol_str) == expected


#негативные тесты
#первая утилита - capitalize
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

#вторая утилита - trim
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("  123", "123"),
    ("   ", ""),
    ("", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

#третья утилита - contains
@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol_str, expected_bool", [
    ("123", "034", False),
    ("    ", "", True),
])

def test_contains_negative(input_str, symbol_str, expected_bool):
    assert string_utils.contains(input_str, symbol_str) == expected_bool

#четвертая утилита - delete
@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol_str, expected", [
    ("   ", "  ", " "),
    ("", "", ""),
    ("123456789", "1234", "56789"),
])
def test_delete_negative(input_str, symbol_str, expected):
    assert string_utils.delete_symbol(input_str, symbol_str) == expected

#негативные проверки с ожидаемыми ошибками 
#Ожидается ошибка: Неверный атрибут - trim
@pytest.mark.parametrize("input_str", [None, []])
def test_trim_raises(input_str):
    with pytest.raises(AttributeError):
        string_utils.trim(input_str)

# Ожидается ошибка: Неверный атрибут - contains
@pytest.mark.parametrize("input_str, symbol", [
    (None, "0"),
])
def test_contains_raises(input_str, symbol):
    with pytest.raises(AttributeError):
        string_utils.contains(input_str, symbol)


# Проверяем, что вызывается ожидаемое исключение - delete
@pytest.mark.parametrize("input_str, symbol_str, expected", [
    (None, "2", AttributeError),  # Проверяем, что вызывается AttributeError
    ("python", None, TypeError),  # Проверяем, что вызывается TypeError
])
def test_delete_raises(input_str, symbol_str, expected):
    with pytest.raises(expected):
        string_utils.delete_symbol(input_str, symbol_str)

