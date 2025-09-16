import os
from llama_index.core import Settings, SimpleDirectoryReader, KnowledgeGraphIndex, StorageContext
from llama_index.core.graph_stores import SimpleGraphStore
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from dotenv import load_dotenv
load_dotenv()

documents=SimpleDirectoryReader("data",recursive=True).load_data()

Settings.llm=GoogleGenAI(model="gemini-2.5-flash")
Settings.embed_model=GoogleGenAIEmbedding(model="gemini-embedding-001")

graph_store=SimpleGraphStore()
storage_context=StorageContext.from_defaults(graph_store=graph_store)

index=KnowledgeGraphIndex.from_documents(
    documents,
    maxtriples_per_chunk=2,
    storage_context=storage_context,
    include_embeddings=True) 


query_engine=index.as_query_engine(
    include_text=False,
    response_mode="tree_summarize",
)

response=query_engine.query("who led starlight?")
print(response)