# Import the necessary module
import os
import json
from tqdm.auto import tqdm
from elasticsearch import Elasticsearch

def load_doc(doc_path):
    with open(doc_path, 'rt') as f_in:
        documents_file = json.load(f_in)

    documents = []

    for course in documents_file:
        course_name = course['course']

        for doc in course['documents']:
            doc['course'] = course_name
            documents.append(doc)
            
    return documents

def create_index(documents, es):
    index_settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "text": {"type": "text"},
                "section": {"type": "text"},
                "question": {"type": "text"},
                "course": {"type": "keyword"} 
            }
        }
    }

    index_name = "course-questions"
    es.indices.create(index=index_name, body=index_settings)
    
    for doc in tqdm(documents):
        es.index(index=index_name, document=doc)
        
            
            

if __name__=="__main__": 
    es = Elasticsearch("http://localhost:9200")
    
    doc_path ='./documents.json'
    documents = load_doc(doc_path)
    create_index(documents, es)
           

