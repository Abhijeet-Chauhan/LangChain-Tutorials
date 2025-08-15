from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(model="llama3-8b-8192")

# template = "Write a {tone} email to {company} expressing interest in the {position} position, mentioning {skill} as a key strength. Keep it to 4 lines max"

# prompt_template = ChatPromptTemplate.from_template(template=template) #--> input_variables=['company', 'position', 'skill', 'tone'] input_types={} partial_variables={} messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['company', 'position', 'skill', 'tone'], input_types={}, partial_variables={}, template='Write a {tone} email to {company} expressing interest in the {position} position, mentioning {skill} as a key strength. Keep it to 4 lines max'), additional_kwargs={})]
# prompt=prompt_template.invoke({
#     "tone":"energetic",
#     "company":"Brainfog",
#     "position":"AI Engineer",
#     "skill":"AI"
# }) #--> messages=[HumanMessage(content='Write a energetic email to Brainfog expressing interest in the AI Engineer position, mentioning AI as a key strength. Keep it to 4 lines max', additional_kwargs={}, response_metadata={})]
# response=llm.invoke(prompt)
# print(response.content)

# prompt_template = ChatPromptTemplate.from_template(template)

# prompt =  prompt_template.invoke({
#     "tone": "energetic", 
#     "company": "samsung", 
#     "position": "AI Engineer", 
#     "skill": "AI"
# })

# Example 2: Prompt with System and Human Messages (Using Tuples)
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
result = llm.invoke(prompt)
print(result)