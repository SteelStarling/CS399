"""
    Remove Outliers from a list of words
    Author: Taylor Hancock
    Date:   04/16/2023
    Notes:  Used GitHub Copilot for sentence autocompletion (technically more than 20 lines, but only contain code)
"""
from w2v.wv import Model
from scipy.stats import zscore

model = Model("models/glove_short.txt")
while True:
    words = input("Please enter a comma separated list of words: ").split(",")
    word_list = [model.find_word(word.strip()).normalize() for word in words]  # fill list with words & clear whitespace

    if None in word_list or len(words) < 3:  # break cases
        break

    similarities = [0 for _ in word_list]  # calculate similarities

    for sim, word in similarities, word_list:
        for word_to_compare in word_list:
            sim += (word.similarity(word_to_compare) / len(word_list))  # space saving measure to calculate average

    # remove outliers (using 1 as a threshold (calculating it properly seems like it'd take more than 20 lines))
    fixed_words = [word for word, sim in zip(words, zscore(similarities)) if abs(sim) < 1]
    print("With outliers removed, your list looks like this: ", list(fixed_words))
