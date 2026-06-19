product_list = []

while True:
    try:
        menu = int(input("\n1-Add | 2-List | 3-Remove | 4-Exit: "))
    except ValueError:
        print("Error: Enter only the NUMBER of the options.")
        continue

    if menu == 1:
        try:
            name = input("Name: ").strip()
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))

            if quantity <= 0 or price <= 0:
                print("❌ ERROR: Invalid values (must be > 0).")
            else:
                item = {"name": name, "quantity": quantity, "price": price}
                product_list.append(item)
                print(f"✅ {name} added!")
        except ValueError:
            print("❌ ERROR: Quantity and Price must be numbers!")

    elif menu == 2:
        if not product_list:
            print("List is empty.")
        else:
            for i, p in enumerate(product_list):
                print(f"[{i}] {p['name']} - Qty: {p['quantity']} - $ {p['price']:.2f}")

    elif menu == 3:
        if not product_list:
            print("Nothing to remove.")
            continue

        try:
            for i, p in enumerate(product_list):
                print(f"{i}: {p['name']}")

            choice = int(input("Index to remove: "))
            removed = product_list.pop(choice)
            print(f"🗑️ {removed['name']} removed!")
        except (ValueError, IndexError):
            print("❌ ERROR: Choose a valid index (list number).")

    elif menu == 4:
        print("Exiting...")
        break
