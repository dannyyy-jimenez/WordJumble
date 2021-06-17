# Introduction

The point of this project is to test webscraping techniques using the BeautifulSoup and Requests module in order to generate random dictionary words using n amount of letters.

---

### How does it work?

The jumble.py file can be called in to create a letter dictionary, which returns a dictionary with every possible word starting with that letter.

```python:
  import Jumble as jumble

  letter_dictionary = jumble.FindWords('i')

  # Letter dictionary will be:

  letter_dictionary = {
    'i': [
      'impression', 'image', 'im', 'i', 'inset', 'inside'
    ]
  }
```

### Combinations of Phrases

By calling `jumble.GetPhrases('i', letter_dictionary)` you'll receive a list of phrases that can be combined using the words in your `letter_dictionary`


### Sample Usage

```python:

  import Jumble as jumble

  icb_words = jumble.FindWords('icb')
  icb_phrases = jumble.GetPhrases('icb', icb_words, n=10, prefix="i miss", writeOut=True)

  """
    Saved output to phrases-icb-10.text

    i miss info continuation block
    i miss inhumane counterrevolutionary backtrack
    i miss invasion commercial bureaucrat
    i miss indoor corruption brinkmanship
    i miss indebtedness consumer billion
    i miss institutionalizing credibility bonanza
    i miss insufferable condo bandstand
    i miss innovate course bountiful
    i miss informer cc bay
    i miss instance cuff basement
  """
```
