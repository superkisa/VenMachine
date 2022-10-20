# Classing with homie 💞💖
from vending.vending import Item, VendingMachine

apple = Item("🍎", 10)
ven1 = VendingMachine(4, 8, 10)
print(ven1)
print()

ven1.fill_cell(apple, 0, 0)
ven1.fill_cell(apple, 0, 1)
print(ven1.dict_items)
print("\n`````````````````\n")

# test = {'apple': [{"x": 0, "y": 0, "depth": 8}, {"x": 0, "y": 1, "depth": 8}]}

# test["apple"].append({"x": 0, "y": 2, "depth": 8})

# print(test["apple"])

ven1.present_cells()
# for i in range(17):
#     ven1.buying_item(apple)
ven1.buying_item(apple)

# ven1.empty_all()
# ven1.present_cells()
# ven1.buying_item(apple)
# dick = {"big": [25, 30, 40], "small": "🍆"}
# dick["black"] = 12
# dick.update({"big": 50})
# print(dick)
# print("big" in dick.keys())
