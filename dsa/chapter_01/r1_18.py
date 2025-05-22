def sequence(k):
	return [2 * sum(x for x in range(m)) for m in range(1,k)]

print(sequence(12))