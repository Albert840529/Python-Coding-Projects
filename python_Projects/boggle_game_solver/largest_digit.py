"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	if 0 <= n < 10:
		# for n is one digit number
		return n
	elif -10 < n < 0:
		return -n
	else:
		if n < 0:
			n *= -1
		return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, maximum):
	if n < 10:
		if n > maximum:
			maximum = n
		return maximum
	else:
		if n % 10 > maximum:         # use % to get each digit
			maximum = n % 10		 # compare largest digit
		n = n // 10
		return find_largest_digit_helper(n, maximum)   # Recursion







if __name__ == '__main__':
	main()
