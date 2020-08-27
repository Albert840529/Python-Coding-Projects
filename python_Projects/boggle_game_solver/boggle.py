"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
lst = []
enter_lst = []
d = {}                # A dict contain the alphabets in boggle games
ans_lst = []
found_words = 0


def main():
	"""
	TODO:
	# """
	global lst, enter_lst, d
	read_dictionary()
	row_num = 1
	while True:
		if row_num <= 4:
			enter = input(f'{row_num} row of letters: ')
			if enter == '-1':
				break
			enter = enter.lower()      # Case Insensitive
			enter = enter.split(' ')
			if illegal_input(enter):
				print('Illegal input')
				break
			enter_lst += enter
			row_num += 1
		else:
			break
	created_boggle(enter_lst)
	for key in d:
		x = key[0]
		y = key[1]
		play_boggle(x, y, d[(x, y)], [(x, y)])
	print(f'There are {found_words} words in total.')


def play_boggle(x, y, ans, previous_lst):
	global lst, ans_lst, found_words
	if len(ans) >= 4:
		if ans in lst:
			# Base Case
			if ans not in ans_lst:
				print(f'Found: "{ans}"')
				ans_lst.append(ans)
				found_words += 1
				if has_prefix(ans):
					# For ans has prefix e.g room -> roomy
					b_lst = beside_dict(x, y, previous_lst)
					for i in range(len(b_lst)):
						ans += d[b_lst[i]]
						new_x = b_lst[i][0]
						new_y = b_lst[i][1]
						previous_lst.append((new_x, new_y))
						play_boggle(new_x, new_y, ans, previous_lst)
						previous_lst.pop()
						ans = ans[:len(ans) - 1]
				return ans_lst
		else:
			if has_prefix(ans):
				b_lst = beside_dict(x, y, previous_lst)
				for i in range(len(b_lst)):
					ans += d[b_lst[i]]
					new_x = b_lst[i][0]
					new_y = b_lst[i][1]
					previous_lst.append((new_x, new_y))
					play_boggle(new_x, new_y, ans, previous_lst)
					previous_lst.pop()
					ans = ans[:len(ans) - 1]
			return ans_lst

	else:
		if has_prefix(ans):
			b_lst = beside_dict(x, y, previous_lst)
			# chose
			for i in range(len(b_lst)):
				ans += d[b_lst[i]]
				# Update the new x, y position
				new_x = b_lst[i][0]
				new_y = b_lst[i][1]
				previous_lst.append((new_x, new_y))
				# explore
				play_boggle(new_x, new_y, ans, previous_lst)
				# Un-choose
				previous_lst.pop()
				ans = ans[:len(ans) - 1]
		return ans_lst


def beside_dict(x, y, previous_lst):
	"""
	:param x: x position in boggle
	:param y: y position in boggle
	:param previous_lst: to save the alphabet already use
	:return: a list of position need to be explore in boggle game
	"""
	beside_lst = []
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			if i == 0 and j == 0:
				# For the self position
				pass
			else:
				position_x = x + i
				position_y = y + j
				if 0 <= position_x < 4:
					if 0 <= position_y < 4:
						if (position_x, position_y) in previous_lst:
							# To prevent adding the alphabet that already used
							pass
						else:
							beside_lst.append((position_x, position_y))
	return beside_lst


def created_boggle(e_lst):
	"""
	:param e_lst: List which contains the enter 16 alphabets
	:return: A dict contain the alphabets in boggle games and also thew position for each alphabets
	"""
	global d
	for j in range(4):
		for i in range(4):
			d[(i, j)] = e_lst[4*j + i]
	return d


def illegal_input(enter):
	if len(enter) != 4:
		return True
	for ch in enter:
		if len(ch) != 1:
			return True
	return False


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global lst
	with open(FILE, 'r') as f:
		for line in f:
			line = line.split()
			lst += line


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	global lst
	for word in lst:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
