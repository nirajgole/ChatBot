from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from intents import INTENT_REGISTRY

llm = ChatOllama(
    model="gemma3",
    temperature=0
)

intent_list = ", ".join(INTENT_REGISTRY.keys())

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an intent classifier.\n"
     "Choose ONE intent from this list ONLY:\n"
     f"{intent_list}\n\n"
     "Return JSON with keys:\n"
     "- intent (string)\n"
     "- fields (object)\n\n"
     "If unsure, set intent to 'unknown'.\n"
     "Do not add extra text."),
    ("human", "{input}")
])

parser = JsonOutputParser()
intent_chain = prompt | llm | parser
