fruits = {'apple', 'banana', 'cherry'}

if 'banana' in fruits:
    print("Banana is in the set of fruits.")
else:
    print("Banana is not in the set of fruits.")

Set1 = {'1', '2', '3'}
numbers_to_check = ['2', '4']

result = any(num in Set1 for num in numbers_to_check)

if result:
    print("At least one number from the list is in Set1.")
else:
    print("No numbers from the list are in Set1.")

people ={'John', 'Jane', 'Doe'}

if 'Jane' in people:
    print("Jane is in the set of people.")
else:
    print("Jane is not in the set of people.")

available_books = {"Echoes of Eternity", "Whispers in the Wind", "Sands of Time"}
input = {"Harry Potter"}