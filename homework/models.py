class Product:
    """
    Класс продукта без реализации методов
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        Верните True если количество продукта больше или равно запрашиваемому
        и False в обратном случае
        """
        raise NotImplementedError

    def buy(self, quantity):
        raise NotImplementedError

    def __hash__(self):
        return hash(self.name + self.description)


class ProductByCount(Product):
    """
    Класс продукта, который продается поштучно.
    TODO реализуйте метод покупки и метод проверки количества.
        Метод покупки поштучно не должен позволять покупать дробное количество продукта
    """
    pass


class ProductByWeight(Product):
    """
    Класс продукта, который продается весом.
    # TODO реализуйте методы
    """
    pass


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, quantity=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        raise NotImplementedError

    def remove_product(self, product: Product, quantity=None):
        """
        Метод удаления продукта из корзины.
        Если quantity не передан, то удаляется вся позиция
        Если quantity больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    def get_total_price(self) -> float:
        raise NotImplementedError

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        raise NotImplementedError
