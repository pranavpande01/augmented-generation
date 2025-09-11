from llama_index.llms.gemini import Gemini
from llama_index.core.llms import ChatMessage
from dotenv import load_dotenv
load_dotenv()   
llm=Gemini(
    model="models/gemini-2.0-flash-lite"
)

messages = [
    ChatMessage(role="user", content="Hello friend!"),
    ChatMessage(role="assistant", content="Yarr what is shakin' matey?"),
    ChatMessage(
        role="user", content="Help me decide what to have for dinner."
    ),
]
resp = llm.chat(messages)
print(resp)