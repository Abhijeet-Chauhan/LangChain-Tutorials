from cmd import PROMPT
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model="llama3-8b-8192")

prompt_template = ChatPromptTemplate.from_messages([
    ("system","You are a facts expert who knows facts about {animal}"),
    ("human","Tell me {fact_counts} facts")
])

chain = prompt_template | model | StrOutputParser()

result = chain.invoke({"animal":"elephant","fact_counts":"4"})

print(result)