!pip install nltk
import nltk
nltk.download('wordnet')

from nltk.corpus import wordnet as wn

# Retrieve synsets for a word
synsets = wn.synsets('car')

# Print the synsets and their definitions
for synset in synsets:
    print("Synset:", synset.name())
    print("Definition:", synset.definition())
    print()

# Explore hypernyms (more general terms)
car_synset = synsets[0]
hypernyms = car_synset.hypernyms()

print("Hypernyms of", car_synset.name())
for hypernym in hypernyms:
    print(hypernym.name(), "-", hypernym.definition())
print()

# Explore hyponyms (more specific terms)
hyponyms = car_synset.hyponyms()

print("Hyponyms of", car_synset.name())
for hyponym in hyponyms:
    print(hyponym.name(), "-", hyponym.definition())
print()

# Explore holonyms (part-whole relationships)
holonyms = car_synset.part_holonyms()

print("Holonyms of", car_synset.name())
for holonym in holonyms:
    print(holonym.name(), "-", holonym.definition())
print()

# Explore meronyms (part-whole relationships)
meronyms = car_synset.part_meronyms()

print("Meronyms of", car_synset.name())
for meronym in meronyms:
    print(meronym.name(), "-", meronym.definition())
print()
