#https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader/
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Document


reader=SimpleDirectoryReader(
 input_dir='data/pdfs'
)

splitter=SentenceSplitter(
    chunk_size=512,
    chunk_overlap=20    
)

docs=Document(text="Hello world. This is a test document. It contains multiple sentences to demonstrate the sentence splitting functionality. Each sentence will be processed accordingly.")
nodes=splitter.get_nodes_from_documents([docs])
print(nodes)

