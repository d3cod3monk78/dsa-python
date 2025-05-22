def sum_of_squares(k: int):
	assert type(k) == int, 'Your input must be integer'
	assert k > 0, 'Your input must be a positve integer'

	sum = 0
	for x in range(k):
		sum = sum + x ** 2

	return sum

print(sum_of_squares(3))
print(sum_of_squares(5))