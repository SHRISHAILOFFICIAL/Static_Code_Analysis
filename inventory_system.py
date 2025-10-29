import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Warning: Tried to remove missing item '{item}'")


def get_qty(item):
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            stock_data.clear()
            stock_data.update(data)
    except FileNotFoundError:
        stock_data.clear()


def save_data(file="inventory.json"):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data():
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return list of items below a stock threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main program logic."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item("grapes", 5)
    remove_item("apple", 3)
    remove_item("orange", 1)

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())

    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
