from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

def run_llm(prompt: str) -> str:
    response = llm.invoke(prompt)
    return response.text
