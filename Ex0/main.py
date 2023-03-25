""" CS 399 - Warmup - Playing around with a larger text file. """

import re
from time import process_time
from collections import Counter



def most_freq_word(list_of_words: [str]) -> (str, int):
    """
    Find the most frequently used word in the given word list
    :param list_of_words: list of words
    :return: most freq word, number of times the word is in the list
    """

    vals = Counter(list_of_words).most_common(1)

    return vals[0]



try:
    with open("treasure.txt") as file:
        text = file.read()
except IOError as err:
    print(err)
    exit(1)

regex = re.compile("[^a-zA-Z]")  # clean up, alt.: ''.join([c for c in text if c.isalpha() or c == " "])
clean_text = regex.sub(" ", text)  # replace all non alpha characters with a space
words = clean_text.lower().split()  # convert all uppercase characters to lower and split on spaces
t0 = process_time()
word, count = most_freq_word(words)
dt = process_time() - t0
print(f"Treasure Island has {len(words)} words.")
print(f"'{word}' is the most frequently used word. It appears {count} times.")
print(f"Processing: {dt} seconds")
