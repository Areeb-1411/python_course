p_id=int(input("Enter product id: "))
p_name=input("Enter product name: ")
price=int(input("Enter product price: "))
discount=float(input("Enter discount percentage: "))

categories=input("Enter categories (comma separated): ").split(',')

features=set(input("Enter product features (comma separated): ").split(','))

available_stock=int(input("Enter available stock: "))
sold_stock=int(input("Enter sold stock: "))

supplier={
    "name": input("Enter supplier name: "),
    "contact": input("Enter supplier contact: "),
    "location": input("Enter supplier location: ")
}

print("\n--- Product Details ---")
print("Product ID:", p_id, ", Name:", p_name, ", Price: ", price)
print("Discount: %.2f%%"% discount)
print(f"Available Stock: {available_stock} units, Sold Stock: {sold_stock} units")
print("Categories: {}".format(categories))
print("Features: {}".format(','.join(features)))
print(f"\nSupplier Name: {supplier['name']}")
print(f"Contact: {supplier['contact']}")
print(f"Location: {supplier['location']}")
