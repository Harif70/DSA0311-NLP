!pip install nltk
import nltk
nltk.download('punkt')

from nltk import CFG
from nltk.parse import RecursiveDescentParser

def generate_parse_tree(grammar, sentence):
    # Create a RecursiveDescentParser with the specified grammar
    parser = RecursiveDescentParser(grammar)

    # Tokenize the sentence into words
    tokens = nltk.word_tokenize(sentence)

    # Generate all possible parse trees for the sentence
    parse_trees = parser.parse(tokens)

    # Return the first parse tree found
    return next(parse_trees, None)

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
parse_tree = generate_parse_tree(grammar, sentence)

if parse_tree:
    print("Parse tree:")
    print(parse_tree)
else:
    print("No parse tree found for the sentence.")
