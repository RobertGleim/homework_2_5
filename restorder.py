print("1.pizza-$15.00 2.burger-$12.50 3.salad-$9.99 4.pasta-$13.75")
choice = input("Please enter your choice (1-4): ")
yes = "yes"
tax = 0.08
cost=0
total = 0
if choice == "1":
    cost = 15.00
    print(f"thank you, you got pizza for {cost}")
elif choice == "2":
    cost = 12.50
    print(f"thank you, you got burger for {cost} ")
elif choice == "3":
    cost = 9.99
    print(f"thank you, you got salad for {cost} ")
elif choice == "4":
    cost = 13.75
    print(f"thank you, you got pasta for {cost} ")
else:
    print("Invalid choice, please try again.")

soda = input("Would you like to add a soda for $2.50? (yes/no): ")
if soda.lower() == "yes":
    cost += 2.50
    print(f"Your total cost is now {cost} with soda included.")

total = cost + (cost * tax)
print(f"Your total cost is now {total:.2f} with tax included.")

print(f"Your final total is {total:.2f}")
print("Thank you for your order!")