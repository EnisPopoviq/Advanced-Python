def my_generator(x):
	for i in range(x):
		yield i

gen_set = {num for num in my_generator(10) if num % 2 == 0}
print(gen_set)

def fibonacci():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b

fib = fibonacci()

for _ in range(10):
	print(next(fib))