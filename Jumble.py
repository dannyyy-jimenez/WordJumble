import requests as requests
import numpy as np
from bs4 import BeautifulSoup as bs
import enchant

# Endpoint for our dictionary words webscraping

ENDPOINT = 'https://www.thefreedictionary.com/words-that-start-with-{letter}' # where x should be appended

# Set the default dictionary we want enchant to call
american_dictionary = enchant.Dict("en_US");

def FindWords(letters='imysm') -> dict:
    """Webscrapes our ENDPOINT for all possible words in the dictionary that start with letter [x]

    Parameters
    ----------
    letters : string
        The letters we want to look for

    Returns
    -------
    dict
        Returns a dictionary with all possible words indexed at each of our letters

    """
    letter_dictionary = {}

    for letter in set(letters):
        res = requests.get(ENDPOINT.format(letter=letter), timeout=(3, 27))
        soup = bs(res.text, 'html.parser')

        container = soup.find('div', {'class': 'TCont'})
        word_counts = container.find_all('div')

        word_counts = [counts.find('ul') for counts in word_counts]

        words = [str(word.text) for counts in word_counts for word in counts.find_all('li')]

        words = [word for word in words if american_dictionary.check(word)]

        letter_dictionary[letter] = words

    return letter_dictionary


def GetPhrases(order, letter_dictionary, prefix = "", suffix="", n=100, writeOut=False) -> list:
    """Get n amount of phrases from our letter dictionary

    Parameters
    ----------
    letter_dictionary : dict
        Our dictionary of letters
    prefix : string
        string to prepend to the final phrase
    suffix : string
        string to append to the final phrase
    n : int
        amount of phrases to make
    writeOut : boolean
        Whether to save our not

    Returns
    -------
    list
        List of phrases

    """
    phrases = []

    while len(phrases) < n:
        phrase = [np.random.choice(letter_dictionary[letter]) for letter in order]
        phrases.append(' '.join(prefix.split(" ") + phrase + suffix.split(" ")))

    if writeOut:
        with open(f"phrases-{''.join(order)}-{n}.txt", 'w') as file:
            for phrase in phrases:
                file.write("%s\n" % phrase)
    return phrases
