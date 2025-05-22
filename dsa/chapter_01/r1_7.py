def sum_of_odd_squares(k: int):
	assert type(k) == int, 'Your input must be an Integer'
	assert k > 0, 'Your input must be a positive Integer'

	return sum([x**2 for x in range(k) if x%2 == 1])

print(sum_of_odd_squares(5))