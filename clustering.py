# src/clustering.py
from sklearn.cluster import KMeans
import pandas as pd

def cluster_documents(docs, embeddings, n_clusters=3):
    n_clusters = min(n_clusters, len(docs))
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(embeddings)

    return pd.DataFrame({
        "Document": [d["name"] for d in docs],
        "Cluster": labels
    })
