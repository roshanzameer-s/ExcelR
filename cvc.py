from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
texts=["I love machine learning", "I enjoy studying artificial intelligence"]
vectorizer=CountVectorizer().fit_transform(texts)
similarity=cosine_similarity(vectorizer[0],vectorizer[1])
print(f"Cosinr Similarity: {similarity[0][0]:.2f}")