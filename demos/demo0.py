#https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader/
from llama_index.core import SimpleDirectoryReader, Document, VectorStoreIndex, Settings
from llama_index.llms.gemini import Gemini
from dotenv import load_dotenv
load_dotenv()
reader=SimpleDirectoryReader(
 input_dir='data/pdfs'
)


for docs in reader.iter_data():
    # <do something with the documents per file>
    print(docs,"\n\n")
