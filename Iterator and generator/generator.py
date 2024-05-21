import nltk
from nltk.corpus import words
import random


def my_generator(count_words: int):
    english_words = list(set(words.words()))
    if count_words > 10_000:
        return None
    elif count_words < 0:
        return None
    cache = set()
    while len(cache) < count_words:
        random_number = random.randrange(0, len(english_words))
        if random_number not in cache:
            cache.add(random_number)
            yield english_words[random_number]


some_words = my_generator(10_000)
print(len(list(some_words)))
