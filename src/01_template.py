
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0.9)

# Template
prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Translate English to Japanese

I'm software engineer. => 私はソフトウェアエンジニアです。
{text} =>
""",
)

res = llm(prompt.format(text="I'm web designer."))
print(res)
