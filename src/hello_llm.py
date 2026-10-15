'''
1.获取base_url、api_key
2.创建DS客户端
'''
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = os.getenv("DEEPSEEK_BASE_URL")

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

# 获取模型列表
# print(client.models.list())
# 
response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role":"system","content":"你是一个有用的助手"},
        {"role":"user","content":"你是谁？"}
    ],
    max_tokens=1024*384,
    stream=False,
    temperature=1
)

print(response.choices[0].message.content)


