import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

def rewrite(query: str) -> str:
    """
    Rewrites a user query using the Gemini API, following best practices.
    """
    
    system_instruction = """You are an expert at rephrasing user questions into keyword-rich, information-dense queries
suitable for a vector database search. Your goal is to capture the user's underlying intent
and expand it with relevant technical terms to maximize the chances of finding the right
documents. Do not answer the question. Only rewrite it."""
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-latest",
        system_instruction=system_instruction,
        
    )

    generation_config = genai.GenerationConfig(
        temperature=0.9,
        max_output_tokens=50,
    )

    prompt = f'User\'s conversational query: "{query}"\n\nRewritten query:'

    response = model.generate_content(
        prompt,
        generation_config=generation_config
    )

    rewritten_query = response.text.strip()
    return rewritten_query

user_question = "How do I fix memory leaks in Python?"
rewritten = rewrite(user_question)
print(rewritten)
