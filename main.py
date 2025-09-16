from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core.agent.workflow import FunctionAgent
from dotenv import load_dotenv
load_dotenv()

def multiply(a:float,b:float)->float:
    """Multiplies two numbers and returns the product"""
    return a*b   
def add(a:float,b:float)->float:
    """Add two numbers and returns the sum"""
    return a+b

def sendmail(a:str)->str:
    """Sends an email to the specified address"""
    print(a)
    return f"Email sent to {a}"

def run_command(a:str)->str:
    """Runs a shell command passed as an argument"""
    import subprocess
    subprocess.run(a,shell=True)
    return f"Command {a} executed"

llm=GoogleGenAI(model_name="gemini-2.0-flash-lite")

workflow=FunctionAgent(
    tools=[multiply,add,sendmail,run_command],
    llm=llm,
    system_prompt="You are an agent that can perform basic calculations, send an email and perform shell commands",
)

async def main():
    response = await workflow.run(user_msg="please remove the folder with the name gacko")
    print(response)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
