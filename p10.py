from pathlib import Path


class Inventory:
    def __init__(self):
        self.items = {}  # naam -> (quantity, price)

    def add_item(self, name, quantity, price):
        self.items[name] = (quantity, price)

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(name)
        del self.items[name]

    def total_value(self):
        return sum(q * p for q, p in self.items.values())

    def __len__(self):
        return len(self.items)


inv = Inventory()

with open(Path(__file__).parent / "stock.txt") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) != 3:
            continue
        try:
            inv.add_item(parts[0], int(parts[1]), int(parts[2]))
        except ValueError:
            print("Invalid line skip:", line.strip())

print("Items:", len(inv))
print("Total value:", inv.total_value())

inv.remove_item("pen")
print("Pen ke baad total:", inv.total_value())

try:
    inv.remove_item("laptop")
except KeyError as e:
    print("Item nahi mila:", e)
