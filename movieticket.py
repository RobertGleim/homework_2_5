def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a whole number.")


name = input("Enter your name: ")
age = get_valid_int("Enter your age: ")

if age < 13:
    cost = 8
    ticket_info = "Child (8.00)"
elif age <= 64:
    cost = 12
    ticket_info = "Adult (12.00)"
else:
    cost = 9
    ticket_info = "Senior (9.00)"

quant = get_valid_int("How many tickets would you like to purchase?: ")
total = cost * quant

print("========MOVIE TICKET RECEIPT=========")
print(f"Customer Name: {name}")
print(f"Ticket Type: {ticket_info}")
print(f"Number of Tickets: {quant}")
print(f"Total Cost: ${total:.2f}")
print(" THANK YOU FOR YOUR PURCHASE! ")
print("======================================")
