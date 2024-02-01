!pip install nltk
!pip install numpy
import nltk
import numpy as np
from nltk.tokenize import sent_tokenize
from sklearn.metrics.pairwise import cosine_similarity

def compute_coherence(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize sentences into words
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

    # Compute the sentence embeddings
    embeddings = []
    for sentence in tokenized_sentences:
        sentence_embeddings = np.mean([word_embedding(word) for word in sentence], axis=0)
        embeddings.append(sentence_embeddings)

    # Compute pairwise cosine similarity between sentence embeddings
    similarity_matrix = cosine_similarity(embeddings)

    # Compute coherence score as the average pairwise cosine similarity
    coherence_score = np.mean(similarity_matrix)

    return coherence_score

# Example usage
text = "This is the first sentence. This is the second sentence. These sentences are related."
coherence_score = compute_coherence(text)

print("Coherence score:", coherence_score)
