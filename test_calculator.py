from calculator import add_numbers


def test_add_numbers_positive():
    """Тест сложения положительных чисел."""
    assert add_numbers(2, 3) == 5


def test_add_numbers_negative():
    """Тест сложения отрицательных чисел."""
    assert add_numbers(-2, -3) == -5


def test_add_numbers_float():
    """Тест сложения дробных чисел."""
    assert add_numbers(1.5, 2.5) == 4.0 
