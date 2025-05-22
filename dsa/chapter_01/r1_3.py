def minmax(data: list[int]):
	assert all(isinstance(x, int) for x in data), 'All items must be integers'
	data.sort()
	return data[0], data[len(data) - 1]

print(minmax([4,2,6,1,7,3]))
