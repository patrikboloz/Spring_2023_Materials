class PriorityQueueBase():
	"""Abstract base class for a priority queue."""

	class _Item():
		"""Lightweight composite to store prority queue items."""
		__slots__ = '_key', '_value'

		def __init__(self, k, v):
			self._key = k
			self._value = v

		def __lt__(self, other):
			return self._key < other._key # compare items based on their keys

	def is_empty(self): #concrete method assuming abstract len
		"""Return True if the priority queue is empty."""
		return len(self) == 0

class UnsortedPriorityQueue(PriorityQueueBase): #base class defines _Item
	""" A min-oriented prioroty queue implemented with an unsorted list."""

	def _find_min(self): #nonpunblic utility
		"""Return Position of item with minimum key"""
		if self.is_empty():
			raise Empty("Priority queue is empty.")

		small = self._data.first()
		walk = self._data.after(small)
		while walk is not None:
			if walk.element() < small.element():
				small = walk
			walk = self._data.after(walk)

		return small

	def __init__(self):
		"""Create a new empty Priority Queue."""
		self._data = PositionalList()


	def __len__(self):
		"""Return the number of items in the priority Queue."""
		return len(self._data)

	def add(self, key, value):
		"""Add a key-value pair."""
		self._data.add_last(self._Item(key, value))

	def min(self):
		"""Return but do not remove (k,v) tuple with minimum key."""
		p = self._find_min()
		item = p.element()
		return (item._key, item._value)

	def remove_min(self):
		""" Remove and return (k,v) tuple with minimum key."""
		p = self._find_min()
		item = self._data.delete(p)
		return (item._key, item._value)
	
