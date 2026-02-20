from menu import Menu
from product import ProductCard


one_card = ProductCard(
    "Молоко", 200, "состоит на учёте",
    102, 1000, '1242', "Коровье молоко",
    "Напитки", "Белый", "Россия",
    "Простоквашино"
)

products = [one_card]

menu = Menu(products)
1
menu.main_menu()