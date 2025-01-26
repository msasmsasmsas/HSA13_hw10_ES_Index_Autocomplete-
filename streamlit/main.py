import streamlit as st
from elasticsearch import Elasticsearch

def create_es_index(es_client):
    mapping = {
        "mappings": {
            "properties": {
                "comment": {
                    "type": "text"
                },
                "suggest": {
                    "type": "completion",
                    "analyzer": "simple",
                    "preserve_separators": True,
                    "preserve_position_increments": True,
                    "max_input_length": 50
                }
            }
        }
    }
    es_client.indices.create(index="comments", body=mapping, ignore=400)

def add_comment(es_client, comment):
    es_client.index(index="comments", body={
        "comment": comment,
        "suggest": {
            "input": comment.split()
        }
    })

def autocomplete(es_client, query):
    response = es_client.search(index="comments", body={
        "suggest": {
            "comment-suggest": {
                "prefix": query,
                "completion": {
                    "field": "suggest",
                    "fuzzy": {
                        "fuzziness": 2
                    }
                }
            }
        }
    })
    return [option["text"] for option in response["suggest"]["comment-suggest"][0]["options"]]

st.title("Коментарі з автодоповненням")

es_client = Elasticsearch(["http://elasticsearch:9200"])
create_es_index(es_client)

comment = st.text_input("Введіть коментар")
if st.button("Додати"):
    add_comment(es_client, comment)
    st.success("Коментар додано")

auto_query = st.text_input("Автодоповнення")
if auto_query:
    suggestions = autocomplete(es_client, auto_query)
    st.write("Рекомендації:", suggestions)
