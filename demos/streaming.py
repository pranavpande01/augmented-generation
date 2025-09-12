from llama_index.llms.gemini import Gemini  
from dotenv import load_dotenv
load_dotenv()

llm=Gemini(model_name="models/gemini-2.0-flash-lite")
resp=llm.stream_complete("hvor mye er en maleri i Norge?")

for i in resp:
    print(i.text, end="")