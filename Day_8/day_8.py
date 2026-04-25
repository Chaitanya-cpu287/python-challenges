import copy

roll_number = 549  
def create_inventory():
    return [
        {
            "item": "Laptop",
            "details": {
                "price": 50000,
                "stock": 10,
                "supplier_rating": 4.5
            }
        },
        {
            "item": "Phone",
            "details": {
                "price": 20000,
                "stock": 25,
                "supplier_rating": 4.3
            }
        },
        {
            "item": "Tablet",
            "details": {
                "price": 30000,
                "stock": 15,
                "supplier_rating": 4.2
            }
        }
    ]

def apply_discount(data):
    index = roll_number % len(data)
    for i in range(len(data)):
        if i == index:   # Custom mutation rule
            data[i]["details"]["price"] = int(
                data[i]["details"]["price"] * 0.9
            )
            data[i]["details"]["stock"] -= 5

def compare_data(original, modified):
    changed = 0
    unchanged = 0

    for i in range(len(original)):
        if original[i] == modified[i]:
            unchanged += 1
        else:
            changed += 1

    return (changed, unchanged)

inventory = create_inventory()
shallow_copy = copy.copy(inventory)
deep_copy = copy.deepcopy(inventory)
apply_discount(shallow_copy)
apply_discount(deep_copy)

print("ORIGINAL INVENTORY")
for item in inventory:
    print(item)

print("\nSHALLOW COPY RESULT")
for item in shallow_copy:
    print(item)

print("\nDEEP COPY RESULT")
for item in deep_copy:
    print(item)

print("\nDIFFERENCES OBSERVED")
print("Roll Number =", roll_number)
print("Modified Index =", roll_number % len(inventory))

print("\nShallow Copy Evidence:")
print("Original and shallow copy show same changed nested values.")
print("Reason: shallow copy copied only outer list.")
print("Inner dictionaries are shared, so changes entered original data.")

print("\nDeep Copy Evidence:")
print("Deep copy changed values only inside copied data.")
print("Original list not linked with deep copy nested dictionaries.")

print("\nTUPLE SUMMARY")
print("Shallow Copy:", compare_data(inventory, shallow_copy))
print("Deep Copy:", compare_data(inventory, deep_copy))