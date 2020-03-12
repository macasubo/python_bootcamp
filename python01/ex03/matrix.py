class Matrix:
	def __init__(self, data=[], shape=()):
		if type(data) == type(list()):
			self.data = data
			if len(shape) == 0:
				self.shape = (len(self.data), len(self.data[0]))
			else:
				self.shape = shape
		elif type(data) == type(tuple()):
			self.data = list()
			self.data = [[0 for item in range(data[1])]
							for row in range(data[0])]
			self.shape = data

	def __repr__(self):
		return f'Object: shape: {self.shape}, data: {self.data}'
	
	def __str__(self):
		return ', '.join([f'{key}: {value}' for key, value
							in self.__dict__.items()])

	def __add__(self, other):
		if type(other) == Matrix:
			return [[self.data[y][x] + other.data[y][x]
					for x in range(other.shape[1])]
					for y in range(self.shape[0])]
		elif type(other) == type(list()):
			return [[self.data[y][x] + other[y]
					for x in range(self.shape[1])]
					for y in range(self.shape[0])]
		else:
			print("Error: invalid type")

	def __radd__(self, other):
		return self.__add__(other)

	def __sub__(self, other):
		if type(other) == Matrix:
			return [[self.data[y][x] - other.data[y][x]
					for x in range(other.shape[1])]
					for y in range(self.shape[0])]
		elif type(other) == type(list()):
			return [[self.data[y][x] - other[y]
					for x in range(self.shape[1])]
					for y in range(self.shape[0])]
		else:
			print("Error: invalid type")

	def __rsub__(self, other):
		if type(other) == Matrix:
			return [[other.data[y][x] - self.data[y][x]
					for x in range(other.shape[1])]
					for y in range(self.shape[0])]
		elif type(other) == type(list()):
			return [[other[y] - self.data[y][x]
					for x in range(self.shape[1])]
					for y in range(self.shape[0])]
		else:
			print("Error: invalid type")

	def __mul__(self, other):
		if type(other) == type(list()):
			other = Matrix([other])
		if type(other) == Matrix:
			res = Matrix((self.shape[0], other.shape[1]))
			for y in range(self.shape[0]):
				for x in range(other.shape[1]):
					for z in range(self.shape[1]):
						res.data[y][x] += self.data[y][z] * other.data[z][x]
			return res
#		elif type(other) in [type(int()), type(float())]:
		else:
			print("Error: invalid type")
			


#	def __rmul__(self, other):
#		if type(other) == Matrix:
#			res = Matrix((self.shape[0], other.shape[1]))
#			for y in range(self.shape[0]):
#				for x in range(other.shape[1]):
#					for z in range(self.shape[1]):
#						res.data[y][x] += self.data[y][z] * other.data[z][x]
#		return res
