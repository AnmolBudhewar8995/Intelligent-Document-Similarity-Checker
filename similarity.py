# src/similarity.py
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(docs, embeddings, threshold=0.85):
    sim_matrix = cosine_similarity(embeddings)
    pairs = []

    for i in range(len(docs)):
        for j in range(i+1, len(docs)):
            score = sim_matrix[i, j]
            if score >= threshold:
                pairs.append({
                    "Doc A": docs[i]["name"],
                    "Doc B": docs[j]["name"],
                    "Similarity": round(score, 3)
                })

    return pd.DataFrame(pairs), sim_matrix
