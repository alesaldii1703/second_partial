# https://replit.com/join/xwkcqwqglq-alejandrasaldiv
"""
Code that calculates multiple discounts
"""
# Here are my inputs
price = float(input("Enter the price of the product: "))
category = input("Enter the category (A, B, or C): ")
units = int(input("Enter the number of units purchased: "))

# Here is my declaration of variables
discount = 0
additional_discount = 0

# Here is my conditional statement for the category
if category == "A":
    discount = 10
elif category == "B":
    discount = 5
elif category == "C":
    discount = 2
# Here is my second conditional statement for an additional discount
if units > 10:
    additional_discount = 5

# Here are my operations
discounted_price = price - (price * (discount + additional_discount) / 100)

# This is my output
print("\nPrice before discount: ${:.2f}".format(price))
print("Discount applied: {}%".format(discount))
print("Additional discount applied (more than 10 units): {}%".format(additional_discount))
print("Final price after discounts: ${:.2f}".format(discounted_price))
