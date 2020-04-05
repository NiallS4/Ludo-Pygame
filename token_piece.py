class Token:
	def __init__(self, colour, currPos = 0, status = "yard", number = 0):
		self.colour = colour
		self.currPos = currPos
		self.status = status
		self.number = number

	def __str__(self):
		return "Number: {}, Colour: {}, currPos: {}, Status: {}".format(
				self.number, self.colour, self.currPos, self.status)

	def __repr__(self):
		return self.__str__()