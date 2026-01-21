numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = {num for num in numbers if num % 2 == 0}
print(even_numbers)

fruits = {'apple', 'banana', 'grape', 'orange', 'kiwi'}
fruits_with_letter_a = {fruit.upper() for fruit in fruits if 'a' in fruit}
print(fruits_with_letter_a)
