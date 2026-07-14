import os
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from langchain.tools import tool
 
CHROMA_PATH = "./chroma_store"
COLLECTION_NAME = "city_guides"
 
embedding_function = OpenAIEmbeddingFunction(
    api_key="any value",
    api_base="https://k7uffyg03f.execute-api.us-east-1.amazonaws.com/prod/openai/v1",
    api_type="openai",
    model_name="text-embedding-3-small",
    default_headers={"x-api-key": os.getenv("API_GATEWAY_KEY")},
)
 
chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = chroma_client.get_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_function,)

@tool
def search_city_guides(query: str, n_results: int = 3) -> str:
    """
    Using semantic search, this searches a collection of UNESCO World Heritage Site descriptions. 
    Can use this when the user asks about famous places, landmarks, or things to see somewhere.
    """
    results = collection.query(query_texts=[query], n_results=n_results)
    docs = results["documents"][0]
 
    if not docs:
        return "No matching results found."
 
    return "\n".join(docs)