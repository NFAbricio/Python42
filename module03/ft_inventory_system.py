import sys

def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = {}
    
    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error invalid parameter '{arg}'")
            continue
        item, quantity_str = arg.split(":", 1)
        if item in inventory:
            print(f"Redundant item '{item}' discarding")
            continue
        try:
            inventory[item] = int(quantity_str)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    
    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")
    
    if total_qty > 0:
        for item, qty in inventory.items():
            pct = (qty / total_qty) * 100
            print(f"Item {item} represents {round(pct, 1)}%")
            
        most_abundant = max(inventory, key=inventory.get)
        least_abundant = min(inventory, key=inventory.get)
        print(f"Item most abundant: {most_abundant} with quantity {inventory[most_abundant]}")
        print(f"Item least abundant: {least_abundant} with quantity {inventory[least_abundant]}")
        
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")

if __name__ == "__main__":
    main()