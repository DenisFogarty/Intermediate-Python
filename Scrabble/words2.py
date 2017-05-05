import scrabble
import string

#Print all letters that never appear doubled

for letter in string.ascii_lowercase:
    hasDouble = False;

    for word in scrabble.wordlist:
        if letter * 2 in word:
            hasDouble = True;
            break;

    if not hasDouble:
        print (letter);
