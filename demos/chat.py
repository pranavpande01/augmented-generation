from llama_index.core.llms import ChatMessage
from llama_index.llms.gemini import Gemini
from dotenv import load_dotenv  
load_dotenv()

llm=Gemini(model_name="models/gemini-2.0-flash-lite")
messages=[
    ChatMessage(role="user", content="Hei! Jeg Heter er Hilder?"),
    ChatMessage(role="assistant", content="Hei Hilder! Hyggelig å møte deg. Hvordan kan jeg hjelpe deg i dag?"),
    ChatMessage(role="user", content="Hva er hovedstaden i Norge?"),
    ]

resp=llm.chat(messages)
print(resp)