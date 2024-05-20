import nltk
from nltk.corpus import words
import random

# for i in range(10):
#     print(random.randrange(0,100, 1))

def my_generator(count_words: int):
    english_words = words.words()
    if count_words > 10_000:
        return None
    elif count_words < 0:
        return None
    for i in range(count_words):
        yield english_words[random.randrange(0,200_000, 1)]
print(list(my_generator(20)))
