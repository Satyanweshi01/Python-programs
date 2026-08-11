# Write a program for net amount payable on purchasing Electronic goods
# If Cost >= 50000 discount : 15%
# If Cost in between 30000 to 50000 discount: 10%
# If Cost in between 20000 to 30000 discount : 5%.

cost = int(input("Enter the cost: "))
discount = 0
if cost>=50000:
    discount = 15
elif 30000 <= cost < 50000:
    discount = 10
elif 20000 <= cost < 30000:
    discount = 5

print(f"Cost: {cost}")
print(f"Discount: {discount}")
amount = cost - (cost*(discount/100))
print(f"Net amount payable after discount: {amount} ")