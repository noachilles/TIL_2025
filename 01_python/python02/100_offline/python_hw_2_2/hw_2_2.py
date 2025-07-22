class Product():
    product_count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.product_count += 1

    def display_info(self):
        print(f'상품명: {self.name}, 가격: {self.price}')

    @classmethod
    def get_product_count(cls):
        print(f'총 상품 수: {cls.product_count}')


apple = Product("사과", 1000)
banana = Product("바나나", 1500)

apple.display_info()
banana.display_info()

Product.get_product_count()