!pip install nltk
import nltk
nltk.download('punkt')

from nltk import CFG
from nltk.parse import ChartParser

def parse_sentence(grammar, sentence):
    # Create a ChartParser with the specified grammar
    parser = ChartParser(grammar)

    # Tokenize the sentence into words
    tokens = nltk.word_tokenize(sentence)

    # Parse the sentence and return the first result
    try:
        parsed_trees = parser.parse(tokens)
        parsed_tree = next(parsed_trees)
        return parsed_tree
    except StopIteration:
        return None

# Example usage
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog'
    V -> 'chased' | 'sat'
    P -> 'on' | 'in'
""")

sentence = "the cat chased a dog"
parsed_tree = parse_sentence(grammar, sentence)

if parsed_tree:
    print("Parse tree:")
    print(parsed_tree)
else:
    print("No parse tree found for the sentence.")
