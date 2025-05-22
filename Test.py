def is_even(k: int):
	while(k > 1):
		k = k - 2

	return True if k == 0 else False

print(is_even(10))
print(is_even(13))

def is_even_bitwise(k: int):
	assert type(k) == int, 'Your input must be int'
	return k&1 == 0

print(is_even_bitwise(14))
print(is_even_bitwise(15))
