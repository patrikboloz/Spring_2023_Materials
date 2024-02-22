def linear_sum(S, n):
	"""Return the sum of the first n numbers of sequence S"""
	if n == 0:
		return 0
	else:
		return linear_sum(S, n-1) + S[n-1]


a_list = [4, 3, 6, 2, 8, 9, 4, 7, 5]
N = 2

print(linear_sum(a_list, N))

def reverse(S, start, stop):
	"""Reverse elements in implicit slice S[start:stop]."""
	if start < stop - 1:
		S[start], S[stop-1] = S[stop-1], S[start]
		reverse(S, start + 1, stop - 1)
	return S

print(reverse(a_list, 0, len(a_list)))