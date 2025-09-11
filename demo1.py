from llama_index.llms.gemini import Gemini
from dotenv import load_dotenv
load_dotenv()   
llm=Gemini(
    model="models/gemini-2.0-flash-lite"
)
resp = llm.complete("Write a poem about a magic backpack")
print(resp)
