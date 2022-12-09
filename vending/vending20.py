class DescriptorPrice:
    def __get__(self, obj, objtype=None) -> float:
        return obj._price

    def __set__(self, obj, new_price: float):
        obj._price = new_price


class Item:
    """This class is used for determining the goods that
    we can put in our vending machine.

    Attributes:
        name(str): name of the article
        price(float): price of the article
    """

    price = DescriptorPrice()

    def __init__(self, name: str, price: float):
        self.__name = name
        self._price = price

    def __repr__(self):
        return f"Item(name = '{self.__name}', price = {self._price})"

    @property
    def name(self) -> str:
        return self.__name


class VendingMachine:  # And this is our vending machine.
    """The class implementing a vending machine

    Attributes:
    width
    length
    depth
    currency
    wallet
    dict_items


    Methods:
        deposit_credits(amount)
            This method is used deposit credits to vending machine's internal wallet.
        withdraw_credits(amount)
            This method is used to safely withdraw credits from
            vending machine's internal wallet.
        fill_cell(item, i, j)
            This method is used to place items in cell_ij of the vending machine.
        present_cells()
            Show contents of non-empty cells and.
        empty_all()
            Empty all cells.
        buying_item(item)
            The method used for buying items from vending machine and money exchange.
        show_methods()
            (classmethod) Print all availible methods of this class.
    """

    def __init__(self, width: int, length: int, depth: int, currency: str = "\u20BD"):
        """Initializes vending machine with specified characteristics.

        Args:
            width
            length
            depth
            currency
        """
        self._width = width
        self._length = length
        self._depth = length
        self.currency = currency
        self.wallet = 0
        self.dict_items = {}

    def __repr__(self):
        return (
            "VendingMachine("
            f"width={self._width}, "
            f"length={self._length}, "
            f"depth={self._depth}, "
            f"currency={self.currency}"
            ")"
        )

    def __str__(self):
        return (
            f"This vending machine has {self._width} cells in a row "
            f"and {self._length} in a colunm. There may be not more "
            f"then {self._depth} goods in each cell."
        )

    @property
    def dimensions(self) -> tuple[int, int, int]:
        """Returns capacity of current vending machine in the form of
        (width, length, depth).
        """
        return self._width, self._length, self._depth

    def deposit_credits(self, amount: float) -> None:
        """This method is used deposit credits to vending machine's internal wallet.

        Args:
            amount(float) - amount to deposit
        """
        if amount >= 0:
            self.wallet += amount
            return None
        else:
            raise ValueError("`amount` must be a positive number.")

    def withdraw_credits(self, amount: float) -> None:
        """This method is used to safely withdraw credits from
        vending machine's internal wallet.

        Args:
            amount(float) - amount to withdraw
        """
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
        """This method is used to place items in cell_ij of the vending machine

        Args:
            item(Item): the item to be placed
            i(int)
            j(int)
        Returns:
            self.dict_item(dict)
        """
        if i > self._length - 1 or j > self._width - 1 or i < 0 or j < 0:
            print("Error: not currect i or j")
        else:
            if not (item.name in self.dict_items.keys()):
                self.dict_items[item.name] = []
            self.dict_items[item.name].append(
                {"x": i, "y": j, "repletion of the cell": self._depth}
            )
            return self.dict_items

    def present_cells(self):
        """Show contents of non-empty cells and current balance."""
        if self.dict_items == {}:
            print("Vending machine is empty!")
        else:
            for i in self.dict_items.keys():
                print(f"{i} =>")
                for j in self.dict_items[i]:
                    print("    ", j)
        print(f"\n current balance: {self.wallet} {self.currency}.\n")

    def empty_all(self):
        """Empty all cells."""
        self.dict_items = {}

    @staticmethod
    def count_difference(a, b):
        return b - a

    def buying_item(self, item: Item):
        """The method used for buying items from vending machine and money exchange.

        Args:
            item(Item): Item object for purchase
        """
        a = 0
        if self.dict_items == {}:
            print("You can't buy anything now. Vending machine is empty.")
        else:
            for i in self.dict_items[item.name]:
                a += i["repletion of the cell"]
            if a == 0:
                print(f"There is no {item.name}s left 😢")
            else:
                print(f"{item.name} costs {item.price} {self.currency}.")
                b = float(input("Please, insert your cash: "))
                while b < item.price:
                    b += float(
                        input(
                            f"Not enouth cash. Add {VendingMachine.count_difference(b, item.price)} {self.currency} "
                        )
                    )
                self.wallet += item.price
                if b > item.price:
                    print(
                        f"There are your {VendingMachine.count_difference(item.price, b)} {self.currency}."
                    )
                for i in self.dict_items[item.name]:
                    if i["repletion of the cell"] != 0:
                        i["repletion of the cell"] -= 1
                        break
                print(f"All ok! Don't forget your {item.name}!")

    @classmethod
    def show_methods(cls):
        print(cls.__doc__)
