# Search-Engine

# Build Your Own Search Engine

A simple search index using TF-IDF and cosine similarity for text fields and exact matching for keyword fields. It allows you to index documents with text and keyword fields and perform search queries with support for filtering and boosting.


## 1. Preparing the environment

Make sure you have the required dependencies installed:

```bash
pip install pandas scikit-learn
```


## 2. Basics of Text Search

- **Information Retrieval** - The process of obtaining relevant information from large datasets based on user queries.
- **Vector Spaces** - A mathematical representation where text is converted into vectors (points in space) allowing for quantitative comparison.
- **Bag of Words** - A simple text representation model treating each document as a collection of words disregarding grammar and word order but keeping multiplicity.
- **TF-IDF (Term Frequency-Inverse Document Frequency)** - A statistical measure used to evaluate how important a word is to a document in a collection or corpus. It increases with the number of times a word appears in the document but is offset by the frequency of the word in the corpus.


## 3.   Create the Index

Create an instance of the `Index` class, specifying the text and keyword fields.


```python
from minsearch import Index

index = Index(
    text_fields=["question", "text", "section"],
    keyword_fields=["course"]
)
```

Fit the index with your documents

```python
index.fit(docs)
```
