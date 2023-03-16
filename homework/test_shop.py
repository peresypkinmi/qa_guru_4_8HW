"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import ProductByCount, ProductByWeight


@pytest.fixture
def product_by_count():
    return ProductByCount("book", 100, "This is a book", 1000)


@pytest.fixture
def product_by_weight():
    return ProductByWeight("apple", 10, "Just an apple", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product и его наследников
    """

    def test_product_by_count_check_quantity(self, product_by_count):
        # TODO напишите проверки на метод check_quantity класса ProductByCount
        pass

    def test_product_by_count_buy(self, product_by_count):
        # TODO напишите проверки на метод buy класса ProductByCount
        pass

    def test_product_by_weight_check_quantity(self, product_by_weight):
        # TODO напишите проверки на метод check_quantity класса ProductByWeight
        pass

    def test_product_by_weight_buy(self, product_by_weight):
        # TODO напишите проверки на метод buy класса ProductByWeight
        pass


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises чтобы проверить это)
    """
