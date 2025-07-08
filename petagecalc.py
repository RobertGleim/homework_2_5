def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")
pet_menu = {
    "1": "dog",
    "2": "cat",
    "3": "hamster",
    "4": "bird"
}
pet_names = {name: name for name in pet_menu.values()}

print("Select your pet from the menu:")
for key, pet in pet_menu.items():
    print(f"{key}. {pet.capitalize()}")
while True:
    choice = input("Enter the number or type of your pet: ").strip().lower()
    if choice in pet_menu:
        pet = pet_menu[choice]
        break
    elif choice in pet_names:
        pet = pet_names[choice]
        break
    else:
        print("Invalid choice. Please enter a number from the menu.")


age = get_valid_int("How old is your pet? ")


if pet in ["dog", "cat"]:
    if age < 3:
        pet_age = age * 12
    else:
        pet_age = 24 + (age - 2) * 4
elif pet == "bird":
    pet_age = age * 9
elif pet == "hamster":
    pet_age = age * 25
else:
    pet_age = "Unknown (invalid pet type)"


print("\n--- Pet Age Summary ---")
print(f"Pet type        : {pet.capitalize()}")
print(f"Pet age         : {age} years")
print(f"In human years  : {pet_age} years")
print(f"Fun fact        : Your {pet} is {pet_age} years old in human years!")



# pet = input("What kind of pet do you have (dog|cat|hamster|bird)? ")
# age = int(input("How old is your pet? "))
# pet_age = 0
# if pet == "dog" or pet == "cat":
#     if age < 3:
#         pet_age = age * 12
#     else:
#         pet_age = 24 + (age - 2) * 4
# elif pet == "bird":
#     pet_age = age * 9
# elif pet == "hamster":
#     pet_age = age * 25



# print(
#     f'''Your pet is a {pet} and is {age} years old.
# pet type: {pet}
# human years: {age}
# pet age in human years: {pet_age}

# fun fact: your {pet} is {pet_age} years old in human years.
# '''
# )