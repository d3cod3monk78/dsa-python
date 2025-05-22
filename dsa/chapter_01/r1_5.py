def sum_of_squares(k: int):
	assert type(k) == int, 'Your input must be integer'
	assert k > 0, 'Your input must be a positive integer'

	return sum([x ** 2 for x in range(k)])

print(sum_of_squares(5))
print(sum_of_squares(10))