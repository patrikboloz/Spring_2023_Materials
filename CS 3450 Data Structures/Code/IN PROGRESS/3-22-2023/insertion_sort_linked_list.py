
def insertion_sort(L):
	"""Sort PositionalList of comparable elements into nondecreasing order."""
	if len(L) > 1:
		marker = L.first()
		while marker != L.last():
			pivot = L.after(marker) #next item to place
			value = pivot.element()
			if value > maker.element(): #pivot is already sorted
				market = pivot
			else: #must relocate pivot
				walk = marker #find the leftmost item greater than value
				while walk != L.first() and L.before(walk).element() > value:
					walk = L.before(walk)
				L.delete(pivot)
				L.add_before(walk, value) #reinsert value before walk