def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a whole number.")


menu = {
    "1": ("Pizza",15.00),
    "2": ("Burger", 12.50),
    "3": ("Salad", 9.99),
    "4": ("Pasta", 13.75),
    
}
soda_price = 2.50
tax_rate = 0.08


print("Menu:")
for key, (item, price) in menu.items():
    print(f"{key}. {item} - {price:.2f}")

choice = str(get_valid_int("Please enter your choice (1-4): "))



if choice in menu:
    item, price = menu[choice]
    cost = price
    print(f"Thank you, you got {item} for ${cost:.2f}")
else:
    print("Invalid choice, please try again.")
    exit()

while True:
    soda = input("Would you like to add a soda for $2.50? (yes/no): ").strip().lower()
    if soda in ("yes", "no"):
        break
    else:
        print("Invalid input! Please enter 'yes' or 'no'.")
soda_added = False
if soda == "yes":
    cost += soda_price
    soda_added = True
    print("Soda Added for $2.50")

tax = cost * tax_rate
total = cost + tax
    

print ("======== Order Receipt=========")
print(f"Main Item: {item.capitalize()}")
print(f"Cost: ${cost:.2f}")
if soda_added:
    print(f"Soda: ${soda_price:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total Cost: ${total:.2f}")
print("========= Thank YOU FOR YOUR ORDER! =========")

# print("1.pizza-$15.00 2.burger-$12.50 3.salad-$9.99 4.pasta-$13.75")
# choice = input("Please enter your choice (1-4): ")
# yes = "yes"
# tax = 0.08
# cost=0
# total = 0
# if choice == "1":
#     cost = 15.00
#     print(f"thank you, you got pizza for {cost}")
# elif choice == "2":
#     cost = 12.50
#     print(f"thank you, you got burger for {cost} ")
# elif choice == "3":
#     cost = 9.99
#     print(f"thank you, you got salad for {cost} ")
# elif choice == "4":
#     cost = 13.75
#     print(f"thank you, you got pasta for {cost} ")
# else:
#     print("Invalid choice, please try again.")

# soda = input("Would you like to add a soda for $2.50? (yes/no): ")
# if soda.lower() == "yes":
#     cost += 2.50
#     print(f"Your total cost is now {cost} with soda included.")

# total = cost + (cost * tax)
# print(f"Your total cost is now {total:.2f} with tax included.")

# print(f"Your final total is {total:.2f}")
# print("Thank you for your order!")
