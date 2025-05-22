def dot_product(a: list[int], b: list[int], n: int):
	return [a[i] * b[i] for i in range(n)]

print(dot_product([1,2,3,4,5], [6,7,8,9,10], 5))

def dot_product_pythoniac(a: list[int], b: list[int]):
	return [x * y for x, y in zip(a, b)]

print(dot_product_pythoniac([1,2,3,4,5], [6,7,8,9,10]))