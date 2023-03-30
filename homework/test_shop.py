"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product
from homework.models import Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity) is True
        assert product.check_quantity(product.quantity + 1) is False
        assert product.check_quantity(product.quantity - 1) is True

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(product.quantity)
        assert product.quantity == 0
        product.buy(product.quantity - 1)
        assert product.quantity == 1

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(product.quantity + 1)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product, 1)
        assert cart.products[product] == 1
        cart.add_product(product, 1)
        assert cart.products[product] == 2

    def test_remove_product_from_cart(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product, 1)
        assert cart.products[product] == 9
        cart.remove_product(product)
        assert cart.products == {}
        cart.add_product(product, 10)
        cart.remove_product(product, 11)
        assert cart.products == {}

    def test_clear_cart(self, cart, product):
        cart.add_product(product, 10)
        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 2)
        assert cart.get_total_price() == (product.price * 2)
        assert isinstance(cart.get_total_price(), float)

    def test_buy_products_from_cart(self, cart, product):
        quantity_product_before_test = product.quantity
        cart.add_product(product, 2)
        cart.buy()
        assert product.quantity + 2 == quantity_product_before_test
        assert cart.products == {}
        cart.products[product] = 1000
        with pytest.raises(ValueError):
            cart.buy()
