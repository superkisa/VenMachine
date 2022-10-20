class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Item(name = '{self.name}', price = {self.price})"

    def get_price(self) -> float:
        return self.price


class VendingMachine:
    def __init__(self, width: int, length: int, depth: int, currency: str = "\u20BD"):
        self.width = width
        self.length = length
        self.depth = length
        self.currency = currency
        self.wallet = 0
        self.dict_items = {}

    def __repr__(self):
        return (
            "VendingMachine("
            f"width={self.width}, "
            f"length={self.legnth}, "
            f"depth={self.depth}, "
            f"currency={self.currency}"
        )

    def __str__(self):
        return (
            f"This vending machine has {self.width} cells in a row "
            f"and {self.length} in a colunm. There may be not more "
            f"then {self.depth} goods in each cell."
        )

    def deposit_credits(self, amount: float) -> None:
        if amount >= 0:
            self.wallet += amount
            return None
        else:
            raise ValueError("`amount` must be a positive number.")

    def withdraw_credits(self, amount: float) -> None:
        if amount >= 0:
            if self.wallet >= amount:
                self.wallet -= amount
                return None
            elif self.wallet < amount:
                raise ValueError(
                    f"You're withdrawing {amount} {self.currency}, "
                    f"but there's only {self.wallet} {self.currency} "
                    "in the wallet."
                )
        else:
            raise ValueError("`amount` must be a positive number.")
        pass

    def fill_cell(self, item: Item, i: int, j: int) -> dict:
        if i > self.length - 1 or j > self.width - 1 or i < 0 or j < 0:
            print("Error: not currect i or j")
        else:
            if not (item.name in self.dict_items.keys()):
                self.dict_items[item.name] = []
            self.dict_items[item.name].append(
                {"x": i, "y": j, "repletion of the cell": self.depth}
            )
            return self.dict_items

    def present_cells(self):
        if self.dict_items == {}:
            print("Vending machine is empty!")
        else:
            for i in self.dict_items.keys():
                print(i)
                for j in self.dict_items[i]:
                    print("    ", j)

    def empty_all(self):
        self.dict_items = {}

    def buying_item(self, item: Item):
        a = 0
        # a += i['fillness of the sell'] for i in self.dict_items[item.name]
        if self.dict_items == {}:
            print("You can't buy anything now. Vending machine is empty.")
        else:
            for i in self.dict_items[item.name]:
                a += i["repletion of the cell"]
            if a == 0:
                print(f"There is no {item.name}s left 😢")
            else:
                print(f"{item.name} costs {item.get_price()} {self.currency}.")
                b = float(input("Please, insert your cash: "))
                while b < item.get_price():
                    b += float(
                        input(
                            f"Not enouth cash. Add {item.get_price() - b} {self.currency} "
                        )
                    )
                self.wallet += item.get_price()
                if b > item.get_price():
                    print(f"There are your {b - item.get_price()} {self.currency}.")
                for i in self.dict_items[item.name]:
                    if i["repletion of the cell"] != 0:
                        i["repletion of the cell"] -= 1
                        break
                print(f"All ok! Don't forget your {item.name}!")
