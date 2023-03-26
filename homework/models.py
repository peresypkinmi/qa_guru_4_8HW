class Product:
    """
    Класс продукта
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
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError(f'Продукта {self.name} не достаточно на складе')

    def __hash__(self):
        return hash(self.name + self.description)


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
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def remove_product(self, product: Product, quantity=None):
        """
        Метод удаления продукта из корзины.
        Если quantity не передан, то удаляется вся позиция
        Если quantity больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if quantity == None or quantity >= self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= quantity

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        products_list = list(self.products.keys())
        quantity_list = list(self.products.values())
        total_price = 0
        for i in range(len(products_list)):
            total_price += (products_list[i].price * quantity_list[i])
        return float(total_price)

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        products_list = list(self.products.keys())
        quantity_list = list(self.products.values())
        for i in range(len(products_list)):
            if quantity_list[i] <= products_list[i].quantity:
                products_list[i].quantity = (products_list[i].quantity - quantity_list[i])
            else:
                raise ValueError(f'Товара {products_list[i].name} в корзине больше чем есть в наличии на складе')
