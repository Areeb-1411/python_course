
product_id = int(input("Enter Product ID : "))

product_name = input("Enter Product Name : ")

price = float(input("Enter Price of the product (₹): "))

cat_i = input("Enter Categories (comma-separated): ").split(',')
categories = []
for cat in cat_i:
    categories.append(cat.strip())


available_stock = int(input("Enter Available Stock: "))
sold_stock = int(input("Enter Sold Stock: "))
stock_details = (available_stock, sold_stock)



discount_percentage = float(input("Enter Discount Percentage: "))

features_input = input("Enter Product Features (comma-separated): ")
product_features = set([feat.strip() for feat in features_input.split(',')])

supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")
supplier_details = {
    "name": supplier_name,
    "contact": supplier_contact,
    "location": supplier_location
}

print("\nProduct ID, Name, Price:", product_id, product_name, price, sep=',')
print("Product Discount: %.2f%%" % discount_percentage)

print(f"\n Product Name: {product_name}")
print(f" Price: ₹{price}")
print(f" Discount: {discount_percentage}%")
print(f" Stock Available: {stock_details[0]} units")
print(f" Units Sold: {stock_details[1]}")
print(f" categories: {categories}")
print(f" features: {','.join(product_features)}")


print("\n Supplier Details: Name - {}, Contact - {}, Location - {}".format(
    supplier_details["name"],
    supplier_details["contact"],
    supplier_details["location"]
))

