import sys

if __name__ == '__main__':
	n = int(input())
	a, b = 1, 0
	for i in range(n):
		a, b = b, a+b

	print(b)
