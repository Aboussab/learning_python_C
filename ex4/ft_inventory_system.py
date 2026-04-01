import sys
from typing import List, Tuple


try:
    if not sys.argv[1:]:
        print("Error: No inventory items provided.")
        print(f"Usage: python3 {sys.argv[0]}\
 <item:quantity> <item:quantity> ...")
        sys.exit(1)
except Exception:
    sys.exit(1)

args = sys.argv[1:]
inventory_master: dict[str, int] = {}
invalid: List[str] = []
cant_cast: List[Tuple[str, str]] = []

print("=== Inventory System Analysis ===")

for arg in args:
    kes_valu = arg.split(":")
    if len(kes_valu) != 2:
        invalid += kes_valu
        continue
    try:
        if kes_valu[0] in inventory_master.keys():
            print(f"Redundant item '{kes_valu[0]}' - discarding")
            continue
        inventory_master[kes_valu[0]] = int(kes_valu[1])
    except (ValueError, IndexError):
        cant_cast.append((kes_valu[0], kes_valu[1]))

for x in invalid:
    print(f"Error - invalid parameter '{x}'")
for name in cant_cast:
    print(f"Quantity error for {name[0]}: invalid literal for int()\
with base 10: {name[1]}")
print(f"Got inventory: {inventory_master}")
print(f"Item list: {list(inventory_master.keys())}")


sum_items = sum(inventory_master.values())
print(f"Total quantity of the {len(inventory_master)} items: {sum_items}")


most: str | None = None
least: str | None = None
for item in inventory_master.keys():
    if most is None or inventory_master[item] > inventory_master[most]:
        most = item
    if least is None or inventory_master[item] < inventory_master[least]:
        least = item
    percentage = round((inventory_master[item] / sum_items) * 100, 1)
    print(f"Item {item} represents {percentage}%")
if most and least:
    print(f"Item most abundant: {most} with quantity {inventory_master[most]}")
    print(f"Item least abundant: {least}\
with quantity {inventory_master[least]}")


inventory_master.update({'magic_item': 1})
print(f"Updated inventory: {inventory_master}")
