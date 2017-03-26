class Poly:
	def __init__(self):
		pass

	def Strip(a):
		try:
			while (a[0] == 0):
				a.pop(0)
		except(IndexError):
			a = [0]

	def Addition(a, b):
		temp = None
		dif = abs(len(a) - len(b))

		if (len(a) > len(b)):
			temp = a
			for i in range(0, len(b)):
				temp[i+dif] += b[i]

		else:
			temp = b
			for i in range(0, len(a)):
				temp[i+dif] += a[i]

		return temp

	def Subtraction(a, b):
		temp = None
		dif = abs(len(a) - len(b))

		if (len(a) > len(b)):
			temp = a
			for i in range(0, len(b)):
				temp[i+dif] -= b[i]

		else:
			temp = [-x for x in b]
			for i in range(0, len(a)):
				temp[i+dif] += a[i]

		Poly.Strip(temp)
		return temp



	def Multiplication(a, b):
		res = [0] * (len(a) + len(b) - 1)
		for i in range(0, len(a)):
			for j in range(0, len(b)):
				res[i+j] = (res[i+j] + a[i] * b[j])

		return res

	def Division(a, b):
		if (len(a) < len(b)):
			return (0, a)

		temp = a
		dif = len(a) - len(b)
		to_subtract = None
		quotient = [0] * (dif + 1)

		for i in range(0, dif + 1):
			quotient[i] = temp[0] / b[0]
			to_subtract = Poly.Multiplication(b, [quotient[i]]) + ([0] * (dif - i))
			temp = Poly.Subtraction(temp, to_subtract)

		return (quotient, temp)


def main():
	a = [1, 0, 0, 0, 0]
	b = [1, -29, 110, 1]

	poly = Poly()


	quotient, remainder = Poly.Division(a, b)
	remainder = [x % 157 for x in remainder]
	print(remainder)

if __name__ == '__main__':
	main()
	