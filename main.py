#https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader/
from llama_index.core import SimpleDirectoryReader, Document, VectorStoreIndex, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from dotenv import load_dotenv
load_dotenv()
reader=SimpleDirectoryReader(
 input_dir='data/pdfs'
)

splitter=SentenceSplitter(
    chunk_size=512,
    chunk_overlap=20    
)

embeddings = GeminiEmbedding(model_name="models/text-embedding-004")

nodes=splitter.get_nodes_from_documents(reader.load_data())

Settings.embed_model=embeddings
Settings.llm=Gemini(model_name="models/gemini-2.0-flash-lite")  
for i in nodes:
    #print(type(i),"\n\n")
    break

print(Settings.llm.complete("yeki lotfa tarikh emruz ro bacpam begeh?"))