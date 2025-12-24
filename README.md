# Intelligent Document Similarity Checker

A Streamlit-based application for analyzing document similarity and clustering documents by topics using advanced NLP embeddings.

## Features

- **Document Loading**: Supports PDF and TXT files from the `data/docs/` folder
- **Similarity Detection**: Identifies duplicate or highly similar documents based on cosine similarity
- **Topic Clustering**: Groups documents into topics using K-Means clustering on sentence embeddings
- **Interactive Interface**: Adjust similarity thresholds and number of clusters via sliders

## Setup

1. **Clone or download the project** to your local machine.

2. **Create a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare documents**: Place your PDF or TXT files in the `data/docs/` folder.

2. **Run the application**:
   ```bash
   streamlit run app.py
   ```

3. **Interact with the app**:
   - Adjust the "Duplicate similarity threshold" to set the minimum similarity score for duplicate detection.
   - Adjust the "Number of topic clusters" to specify how many topic groups to create.
   - View similarity pairs and cluster assignments in the tables.
   - Inspect individual document content by selecting from the dropdown.

## Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`

## Project Structure

- `app.py`: Main Streamlit application
- `src/`: Source code modules
  - `loader.py`: Document loading utilities
  - `embeddings.py`: Text embedding generation
  - `similarity.py`: Similarity computation
  - `clustering.py`: Document clustering
- `data/docs/`: Folder for input documents
- `requirements.txt`: Python dependencies
