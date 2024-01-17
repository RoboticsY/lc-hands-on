from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0.9)

# 本当はベクターDBとか PDF などから動的に取得するべき。
knowledge = """
`uたそ` は関西在住のソフトウェアエンジニアです。
"""

# Template
prompt = PromptTemplate(
    input_variables=["knowledge"],
    template="""
{knowledge}

`uたそ` とは誰ですか？
""",
)

res = llm(prompt.format(knowledge=knowledge))
print(res)