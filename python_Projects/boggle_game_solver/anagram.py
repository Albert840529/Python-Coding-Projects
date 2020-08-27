"""
File: anagram.py
Name: Albert
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
lst = []
num_run = 0
num_words = 0
d = {}                        # Dict which count each alphabet in a word, e.g : apple ->
                              # d = {'a': 1, 'p':2, 'l':1, 'e':1}


def main():
    global d, num_words, num_run
    read_dictionary()
    print('Welcome to stanCode \"Anagram Generator\"(or -1 to quit)')
    while True:
        search = input('Find anagrams for: ')
        if search == EXIT:
            break
        else:
            search = search.lower()     # case insensitive
            d = duplicate(search)
            test = find_anagrams(search)
            print(f'{num_words} anagrams: {test}')
            print(f'Number of runs: {num_run}')
        num_words = 0     # count how many anagrams
        num_run = 0       # count the recursion times


def read_dictionary():
    global lst
    with open(FILE, 'r') as f:
        for line in f:
            line = line.split()
            lst += line


def find_anagrams(s):
    """
    :param s: search str
    :return: a list of anagrams
    """
    print('Searching...')
    return find_anagrams_helper(s, '', [])


def find_anagrams_helper(s, ans, ans_lst):
    global lst, num_run, num_words, d
    num_run += 1
    if len(s) == len(ans):
        # Base case
        if ans in lst:
            # If ans is a word in lst
            if ans not in ans_lst:
                print(f'Found: {ans}')
                print('Searching...')
                ans_lst.append(ans)
                num_words += 1
        return ans_lst
    else:
        for word in d:
            if d[word] > 0:
                # choose
                ans += word
                d[word] -= 1
                # explore
                if has_prefix(ans):
                    find_anagrams_helper(s, ans, ans_lst)
            # un-choose
                ans = ans[:len(ans)-1]
                d[word] += 1
        return ans_lst


def has_prefix(sub_s):
    """
    :param sub_s: str
    :return: bool
    To check whether sub_sting has prefix in lst (Words-Dictionary)
    """
    global lst
    for word in lst:
        if word.startswith(sub_s):
            return True
    return False


def duplicate(s):
    """
    :param s: search word
    :return: Dict
    This is the fxn to count each alphabet in a word
    """
    d_check = {}
    for i in range(len(s)):
        if s[i] in d_check:
            d_check[s[i]] += 1
        else:
            d_check[s[i]] = 1
    return d_check



if __name__ == '__main__':
    main()
