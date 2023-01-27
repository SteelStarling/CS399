""" CS 399 - Warmup - Playing around with a larger text file. """

import re
from time import process_time


def most_freq_word(list_of_words: [str]) -> (str, int):
    """
    Find the most frequently used word in the given word list
    :param list_of_words: list of words
    :return: most freq word, number of times the word is in the list
    """

    tuple_of_words = (*list_of_words, ) # from https://www.geeksforgeeks.org/python-convert-a-list-into-a-tuple/

    freq_word = ""
    occurrence = -1

    for word in tuple_of_words:
        temp_store = list_of_words.count(word) # store word to prevent double lookup
        if temp_store > occurrence:
            occurrence = temp_store
            freq_word = word
    return freq_word, occurrence



try:
    with open("Ex0/treasure.txt") as file:
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
