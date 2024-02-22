#Python code for a ScoreBoard class that mainstains an ordered series of scores as GameEntry objects

class GameEntry():
	"""Represents one entry of a list of high scores"""

	def __init__(self, name, score):
		self._name = name
		self._score = score

	def get_name(self):
		return self._name

	def get_score(self):
		return self._score

	def __str__(self):
		return('{0}, {1}').format(self._name, self._score) #example '(Bob, 90)''


oGameEntry1 = GameEntry('Bob', '90')
oGameEntry2 = GameEntry('Jeff', '60')
oGameEntry3 = GameEntry('Charlie', '95')
oGameEntry4 = GameEntry('Patrik', '92')

#print(oGameEntry.get_name())
#print(oGameEntry.get_score())
#print(oGameEntry)


class Scoreboard():
	"""Fixed-length sequence of high scores in nondecreasing order."""

	def __init__(self, capacity=10):
		"""Initialize scoreboard with given maximum capacity
		All entries are initially None."""

		self._board = [None] * capacity  #Reserve space for future scores
		self._n = 0

	def __getitem__(self, k):
		"""Return entry at index k"""
		return self._board[k]

	def __str__(self):
		"""Return string representation of the high score list."""
		return '\n'.join(str(self._board[j]) for j in range(self._n))

	def add(self, entry):
		"""Consider adding entry to high scores."""
		score = entry.get_score()

		#Does new entry qualify as a high score?
		#answer is yes if board not full or score is higher than last entry
		good = self._n < len(self._board) or score > self._board[-1].get_score()

		if good:
			if self._n < len(self._board): #no score drops from list
				self._n += 1 #so overall number increases

			j = self._n - 1
			while j > 0 and self._board[j-1].get_score() < score:
				self._board[j] = self._board[j-1]  #shift entry from j-1 to j
				j -= 1 #decrement j
			self._board[j] = entry  #when done, add new entry



oScoreboard = Scoreboard(3)
print(oScoreboard)
oScoreboard.add(oGameEntry1)
oScoreboard.add(oGameEntry2)
oScoreboard.add(oGameEntry3)
oScoreboard.add(oGameEntry4)

print(oScoreboard)









