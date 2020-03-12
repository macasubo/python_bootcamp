class Vector:
	def __init__(self, coord):
		if type(coord) == type(list()):
			self.values = coord
			self.size = len(coord)
		elif type(coord) == type(int):
			self.size = coord
			self.values = list()
			for i in coord:
				self.values.append(float(i))
		elif type(coord) == type(tuple):
			self.size = coord[1] - coord[0]
			self.values = list()
			for i in coord:
				self.values.append(float(i))

	def __repr__(self):
		return f'Object: size: {self.size}, values: {self.values}'

	def __str__(self):
		return ', '.join([f'{key}: {value}' for key, value
											in self.__dict__.items()])

	def __add__(v1, other):
		if type(other) == Vector:
			return [v1.values[i] + other.values[i] for i in range(v1.size)]
		elif type(other) in [type(int()), type(float())]:
			return [v1.values[i] + other for i in range(v1.size)]
		else:
			print("Error: invalid type")

	def __radd__(v1, other):
		return v1.__add__(other)

	def __sub__(v1, other):
		if type(other) == Vector:
			return [v1.values[i] - other.values[i] for i in range(v1.size)]
		elif type(other) in [type(int()), type(float())]:
			return [v1.values[i] - other for i in range(v1.size)]
		else:
			print("Error: invalid type")
	
	def __rsub__(v1, other):
		if type(other) == Vector:
			return [other.values[i] - v1.values[i] for i in range(v1.size)]
		elif type(other) in [type(int()), type(float())]:
			return [other - v1.values[i] for i in range(v1.size)]
		else:
			print("Error: invalid type")

	def __mul__(v1, other):
		if type(other) == Vector:
			res = 0
			for i in range(v1.size):
				res += v1.values[i] * other.values[i]
			return res
		elif type(other) in [type(int()), type(float())]:
			return [v1.values[i] * other for i in range(v1.size)]
		else:
			print("Error: invalid type")

	def __rmul__(v1, other):
		return v1.__mul__(other)

	def __truediv__(v1, other):
		if type(other) in [type(int()), type(float())] and other != 0:
			return v1.__mul__(1 / other)
		else:
			print("Error: invalid type")

	def __rtruediv__(v1, other):
		if type(other) in [type(int()), type(float())]:
			try:
				return [other / v1.values[i] for i in range(v1.size)]
			except ZeroDivisionError as e:
				print(f'ZeroDivisionError: {e}')
		else:
			print("Error: invalid type")
