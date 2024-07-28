import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np

class TextSearch:
    """
    A simple search index using TF-IDF and cosine similarity for text fields and exact matching for keyword fields.

    Attributes:
        text_fields (list): List of text field names to index.
        keyword_fields (list): List of keyword field names to index.
        vectorizers (dict): Dictionary of TfidfVectorizer instances for each text field.
        keyword_df (pd.DataFrame): DataFrame containing keyword field data.
        text_matrices (dict): Dictionary of TF-IDF matrices for each text field.
        docs (list): List of documents indexed.
    """

    def __init__(self, text_fields):
        """
        Initializes the TextSearch with specified text fields.

        Args:
            text_fields (list): List of text field names to index.
        """
        self.text_fields = text_fields
        self.matrices = {}
        self.vectorizers = {}

    def fit(self, records, vectorizer_params={}):
        """
        Fits the index with the provided documents.

        Args:
            records (list of dict): List of documents to index. Each document is a dictionary.
            vectorizer_params (dict): Optional parameters to pass to TfidfVectorizer.
        """
        self.df = pd.DataFrame(records)

        for f in self.text_fields:
            cv = TfidfVectorizer(**vectorizer_params)
            X = cv.fit_transform(self.df[f])
            self.matrices[f] = X
            self.vectorizers[f] = cv

    def search(self, query, n_results=10, boost={}, filters={}):
        """
        Searches the index with the given query, filters, and boost parameters.

        Args:
            query (str): The search query string.
            num_results (int): The number of top results to return. Defaults to 10.
            boost_dict (dict): Dictionary of boost scores for text fields. Keys are field names and values are the boost scores.
            filter_dict (dict): Dictionary of keyword fields to filter by. Keys are field names and values are the values to filter by.

        Returns:
            list of dict: List of documents matching the search criteria, ranked by relevance.
        """
        score = np.zeros(len(self.df))

        for f in self.text_fields:
            b = boost.get(f, 1.0)
            q = self.vectorizers[f].transform([query])
            s = cosine_similarity(self.matrices[f], q).flatten()
            score = score + b * s

        for field, value in filters.items():
            mask = (self.df[field] == value).values
            score = score * mask

        idx = np.argsort(-score)[:n_results]
        results = self.df.iloc[idx]
        return results.to_dict(orient='records')