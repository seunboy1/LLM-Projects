# Search-Engine

## Build Your Own Search Engine

A simple search index using TF-IDF and cosine similarity for text fields and exact matching for keyword fields. It allows you to index documents with text and keyword fields and perform search queries with support for filtering and boosting.


### Preparing the environment

Make sure you have the required dependencies installed:

```bash
pip install pandas scikit-learn
```

###  Usage

Here's how you can use the library:


### Define Your Documents

Prepare your documents as a list of dictionaries. Each dictionary should have the text and keyword fields you want to index.

```python
docs = [
    {
        "question": "How do I join the course after it has started?",
        "text": "You can join the course at any time. We have recordings available.",
        "section": "General Information",
        "course": "llm-course"
    },
    {
        "question": "What are the prerequisites for the course?",
        "text": "You need to have basic knowledge of programming.",
        "section": "Course Requirements",
        "course": "data-scinec-course"
    }
]
```

### Create the Index

Create an instance of the `TextSearch` class, specifying the text and keyword fields.


```python
from minsearch import TextSearch

index = TextSearch(text_fields=['section', 'question', 'text'])
)
```

Fit the index with your documents

```python
index.fit(documents)
```

### Perform a Search

Search the index with a query string, optional filter dictionary, and optional boost dictionary.

```python

results = index.search(
    query='I just singned up. Is it too late to join the course?',
    n_results=5,
    boost={'question': 3.0},
    filters={"course": "llm-course"}
)

for result in results:
    print(result)
```
