from product import Product
from order_processor import OrderProcessor

if __name__ == "__main__":
    # Імітація кошика покупця
    cart = [
        Product("Ноутбук HP", 15000.0),
        Product("Мишка Logitech", 500.0),
        Product("Навушники Sony", 2000.0)
    ]

    # Обробка замовлення
    processor = OrderProcessor()
    processor.process_order("Студент Вар.16", True, cart)
