class Player:
	def __init__(self, name, colour, tokens, score = 0):
		self.name = name
		self.colour = colour
		self.tokens = tokens
		self.score = score

	def __str__(self):
		return "Name: {}, Tokens: {}, Score: {}".format(
				self.name, self.tokens, self.score)

	def __repr__(self):
		return self.__str__()