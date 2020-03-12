from matrix import Matrix

m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
			 [0.0, 2.0, 4.0, 6.0]])

m2 = Matrix([[0.0, 1.0],
			 [2.0, 3.0],
			 [4.0, 5.0],
			 [6.0, 7.0]])

m3 = Matrix((5, 2))

v1 = [10, 100, 1000, 10000]

print(m3.__repr__)
print(m3.__str__)
print(m1 + m1)
print(m1 + v1)
print(v1 - m1)
print(m1 * m2)
