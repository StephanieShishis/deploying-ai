import os
import pandas as pd
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from dotenv import load_dotenv

load_dotenv(".env")
load_dotenv(".secrets")
 
DATA_PATH = "data/whc-sites-2021.csv"
CHROMA_PATH = "./chroma_store"
COLLECTION_NAME = "city_guides"

df = pd.read_csv(DATA_PATH)
 
documents = df["short_description_en"].tolist()
ids = [f"site{i}" for i in range(len(df))]
 
embedding_function = OpenAIEmbeddingFunction(
    api_key="any value",
    api_base="https://k7uffyg03f.execute-api.us-east-1.amazonaws.com/prod/openai/v1",
    api_type="openai",
    model_name="text-embedding-3-small",
    default_headers={"x-api-key": os.getenv("API_GATEWAY_KEY")},
)
 
chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
 
existing_names = [c.name for c in chroma_client.list_collections()]
if COLLECTION_NAME in existing_names:
    chroma_client.delete_collection(COLLECTION_NAME)
 
collection = chroma_client.create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_function,
)
 
collection.add(
    ids=ids,
    documents=documents,
)
 