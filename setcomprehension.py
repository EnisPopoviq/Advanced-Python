# {expression for item in iterable}

# {expression for x in {1, 2, 3, 4}}

print({i * i for i in {1, 2, 3, 4}})

squares = set()
for i in {1, 2, 3, 4}:
	squares.add(i * i)
print(squares)

word = "hello"
unique_chars = {char for char in word}
print(unique_chars)