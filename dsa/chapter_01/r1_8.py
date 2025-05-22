# 0 - (-10) = 10
# j - k = len => j = len + k

def equivalent_positive_index(word, k):
	assert type(k) == int, 'Your k must be an Integer'
	assert k < 0, 'Your k must be negetive Integer'
	assert k * -1 <= len(word), 'Your k has to be valid index'

	return len(word) + k

print(equivalent_positive_index('whatthehellisgoing', -5))