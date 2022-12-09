# Classing with 💞💖
from vending.vending20 import Item, VendingMachine


def main_test():
    apple = Item("🍎", 10)
    ven1 = VendingMachine(4, 8, 10)
    print(ven1)
    print()

    ven1.fill_cell(apple, 0, 0)
    ven1.fill_cell(apple, 0, 1)
    print(ven1.dict_items)
    print("\n`````````````````\n")

    ven1.present_cells()

    ven1.buying_item(apple)

    print(repr(ven1))

    # print(VendingMachine.show_methods())


main_test()
