def jaccard_simialrity(text1,text2):
    words1=set(text1.lower().split())
    words2=set(text2.lower().split())
    intersection=words1.intersection(words2)
    union=words1.union(words2)
    return float(len(intersection)/len(union))
text1="I love machine learning"
text2="I enjoy learning artificial Intelligence"

similarity=jaccard_simialrity(text1,text2)
print(f"Jaccard similarity: {similarity}")