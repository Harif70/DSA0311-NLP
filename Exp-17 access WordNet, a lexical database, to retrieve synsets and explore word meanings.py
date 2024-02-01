!pip install nltk
import nltk
nltk.download('wordnet')
nltk.download('punkt')

from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize

def lesk(word, sentence):
    best_sense = None
    max_overlap = 0

    # Tokenize the sentence into words
    context = word_tokenize(sentence)

    # Iterate over the synsets of the target word
    for sense in wn.synsets(word):
        signature = word_tokenize(sense.definition())

        # Add examples to the signature
        for example in sense.examples():
            signature += word_tokenize(example)

        # Calculate the overlap between the signature and the context
        overlap = len(set(signature) & set(context))

        # Update the best sense if the overlap is greater
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense

# Example usage
word = "bank"
sentence = "I went to the bank to deposit some money."
sense = lesk(word, sentence)

if sense:
    print("Word:", word)
    print("Sense:", sense)
    print("Definition:", sense.definition())
else:
    print("No sense found for the word.")
