import sys


if not sys.argv:
    print("Error: No inventory items provided.")
    print(f"Usage: python3 {sys.argv[0]} <item:quantity> <item:quantity> ...")
    sys.exit(1)


def categories(inventory: dict) -> dict:
    categorie = {"Moderate": {}, "Scarce": {}}
    for key, value in inventory.items():
        if value >= 5:
            categorie["Moderate"].update({key: value})
        else:
            categorie["Scarce"].update({key: value})
    return categorie


try:
    args = sys.argv[1:]
    inventory_master = {}
    for arg in args:
        kes_valu = arg.split(":")
        if len(kes_valu) != 2:
            print(f"Usage: python3 {sys.argv[0]} <item:quantity>"
                  + "<item:quantity> ...")
            sys.exit(1)
        inventory_master[kes_valu[0]] = int(kes_valu[1])
except (ValueError, IndexError):
    print("there is actulley an errore.")
sum_items = 0
for x in inventory_master.values():
    sum_items += x

print("=== Inventory System Analysis ===")
print(f"Total items in inventory: {sum_items}")
print(f"Unique item types: {len(inventory_master)}")

print("\n=== Current Inventory ===")

for key, value in inventory_master.items():
    print(f"{key}: {value} unit(s) ({(value*100) / sum_items:.1f}%)")


print("\n=== Inventory Statistics ===")
biggest_key = None
biggest_value = None

for key, value in inventory_master.items():
    if biggest_value is None or value > biggest_value:
        biggest_value = value
        biggest_key = key
for key, value in inventory_master.items():
    if value == biggest_value:
        print(f"Most abundant: {key} ({value} unites)")
low_value = None
low_key = None
for key, value in inventory_master.items():
    if low_value is None or value < low_value:
        low_value = value
        low_key = key
for key, value in inventory_master.items():
    if value == low_value:
        print(f"Least abundant: {key} ({value} unites)")
        break

print("\n=== Item Categories ===")

nested = categories(inventory_master)

print(f"Moderate: {nested['Moderate']}")
print(f"Scarce: {nested['Scarce']}")


print("\n=== Management Suggestions ===")

low_value = None
low_key = None
for key, value in inventory_master.items():
    if low_value is None or value < low_value:
        low_value = value
        low_key = key
Restock_needed = []
for key, value in inventory_master.items():
    if value == low_value:
        Restock_needed += [key]
print("Restock needed: ", end='')
i = 0
for x in Restock_needed:
    print(x, end='')
    i += 1
    if i < len(Restock_needed):
        print(",", end='')


print('\n=== Dictionary Properties Demo ===')

print("Dictionary keys: ", end="")
i = 0
for key in inventory_master.keys():
    print(key, end="")
    i += 1
    if i < len(inventory_master):
        print(",", end='')

print("\nDictionary values: ", end="")
i = 0
for value in inventory_master.values():
    print(value, end="")
    i += 1
    if i < len(inventory_master):
        print(", ", end='')

print("\nSample lookup - ", end='')
i = 0
for key in inventory_master.keys():
    i += 1
    if key == 'sword':
        print("'sword' in inventory: True")
    elif i >= len(inventory_master):
        print("'sword' in inventory: False")
