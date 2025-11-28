from typing import List
from product import Product

class OrderProcessor:
    VIP_DISCOUNT_RATE = 0.90
    BIG_ORDER_DISCOUNT_RATE = 0.95
    BIG_ORDER_THRESHOLD = 10000.0

    def process_order(self, client_name: str, is_vip: bool, products: List[Product]):
        self._print_header(client_name)
        raw_total = self._calculate_items_total(products)
        final_total = self._apply_discount(raw_total, is_vip)
        self._print_footer(final_total)

    def _calculate_items_total(self, products: List[Product]) -> float:
        total = 0.0
        for product in products:
            print(f"Товар: {product.name} | Ціна: {product.price} грн")
            total += product.price
        return total

    def _apply_discount(self, total: float, is_vip: bool) -> float:
        if is_vip:
            print("(Застосовано VIP знижку 10%)")
            return total * self.VIP_DISCOUNT_RATE
        if total > self.BIG_ORDER_THRESHOLD:
            print("(Застосовано знижку 5% за обсяг)")
            return total * self.BIG_ORDER_DISCOUNT_RATE
        return total

    def _print_header(self, client_name):
        print("=== Чек замовлення ===")
        print(f"Клієнт: {client_name}")

    def _print_footer(self, total):
        print("----------------------")
        print(f"До сплати: {total:.2f} грн")
        print("======================")
