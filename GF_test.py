from __future__ import print_function
from poly_test import Poly


class GF():
	def __init__(self, mod, irreducible_poly):
		self.mod = mod
		self.irreducible_poly = irreducible_poly


	def Addition(self, a, b):
		temp = [x % self.mod for x in Poly.Addition(self, a, b)]
		self.Strip(temp)
		return temp

	def Multiplication(self, a, b):
		temp = [x % self.mod for x in Poly.Multiplication(a, b)]
		quotient, remainder = Poly.Division(temp, self.irreducible_poly)
		remainder = [x % self.mod for x in remainder]
		Poly.Strip(remainder)
		return remainder

	def X_degree(self, degree):
		x_2deg_n = [1, 0]
		result = [0, 1]
		binary_degree = []
		deg = 0

		while (degree != 0):
			if (degree % 2 == 1):
				result = self.Multiplication(x_2deg_n, result)
				binary_degree.append(1)
			else:
				binary_degree.append(0)

			x_2deg_n = self.Multiplication(x_2deg_n, x_2deg_n)
			degree = degree // 2
			deg += 1
			if (degree != 0):
				print('x^%d = ' % 2**deg, end = '')
				self.Print_poly(x_2deg_n)

		return result, binary_degree

	def Print_poly(self, poly):
		Poly.Strip(poly)

		for i in range(0, len(poly)):
			if (poly[i] == 0):
				continue

			if (i != 0):
				print(' + ', end = '')

			if (poly[i] != 1):
				print('%d' % poly[i], end = '')
			elif(i == len(poly) - 1):
				print('%d' % poly[i], end = '')
				

			if (len(poly) - i > 2):
				print('x^%d' % (len(poly) - i - 1) , end = '')
			elif (len(poly) - i == 2):
				print('x', end = '')
				
		print('\n')



def main():
	mod = 157
	irreducible_poly = [1, -29, 110]
	deg = 79


	gf = GF(mod, irreducible_poly)

	ans, binary_degree = gf.X_degree(deg)

	flag = 0
	print('\nx^%d = ' % deg, end = '')
	for i in range(0, len(binary_degree)):
			if (binary_degree[i] == 0):
				continue
			
			if (i != 0 and flag != 0):
				print(' * ', end = '')

			if (i == 0):
				print('x', end = '')
			else:
				print('x^%d' % 2**i, end = '')
			flag = 1

	print('\n\nx^%d = ' % deg, end = '')
	gf.Print_poly(ans)
	

if __name__ == '__main__':
	main()
	