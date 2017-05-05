import scrabble

def compare_reverse(word):
    if word == word[::-1]:
        return True
    return False

def compare_opposite(word):
    for num in range(0, int(len(word)/2)):
        if word[num] != word[-num - 1]:
            return False
    return True

palindrome_length = 0
palindrome = ""
for word in scrabble.wordlist:
    if compare_opposite(word) and len(word) > palindrome_length:
        palindrome_length = len(word)
        palindrome = word

print ("The longest palindrome is", palindrome, "with a length of", palindrome_length)