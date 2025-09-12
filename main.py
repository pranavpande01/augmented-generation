#https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader/
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter



reader=SimpleDirectoryReader(
 input_dir='data/pdfs'
)

