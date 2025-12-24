# app.py
import streamlit as st
import pandas as pd

from src.loader import load_documents
from src.embeddings import embed_documents
from src.similarity import compute_similarity
from src.clustering import cluster_documents

st.set_page_config(layout="wide")
st.title("📄 Intelligent Document Similarity Checker")

st.sidebar.header("Settings")
similarity_threshold = st.sidebar.slider("Duplicate similarity threshold", 0.7, 0.95, 0.85)
n_clusters = st.sidebar.slider("Number of topic clusters", 2, 10, 3)

st.markdown("### 📂 Upload documents")
st.info("Place PDF or TXT files inside `data/docs/` folder.")

docs = load_documents()

if len(docs) < 2:
    st.warning("Upload at least 2 documents to analyze similarity.")
    st.stop()

st.success(f"{len(docs)} documents loaded.")

texts = [d["text"] for d in docs]

with st.spinner("Generating embeddings..."):
    embeddings = embed_documents(texts)

# ---------------- SIMILARITY ----------------
st.header("🔁 Duplicate / Similar Documents")
pairs_df, sim_matrix = compute_similarity(docs, embeddings, similarity_threshold)

if pairs_df.empty:
    st.info("No duplicates found above threshold.")
else:
    st.dataframe(pairs_df)

# ---------------- CLUSTERING ----------------
st.header("🧩 Topic Clustering")
cluster_df = cluster_documents(docs, embeddings, n_clusters)
st.dataframe(cluster_df)

# ---------------- INSPECT DOCUMENT ----------------
st.header("🔍 Inspect Document Content")
doc_names = [d["name"] for d in docs]
selected = st.selectbox("Select document", doc_names)

doc_text = next(d["text"] for d in docs if d["name"] == selected)
st.text_area("Document Text", doc_text[:5000], height=300)
