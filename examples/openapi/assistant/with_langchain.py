import asyncio
from aily.openapi.assistant.langchain_llm import AilyLLM
from langchain_core.prompts import ChatPromptTemplate

# 创建AilyLLM实例
llm = AilyLLM(app_id='spring_ec9b314b50__c', user_access_token='')
# 打印批量查询结果
print(llm.batch(['aPaaS的产品负责人是谁', 'aPaaS的技术负责人是谁']))

# 创建聊天提示模板
prompt = ChatPromptTemplate.from_messages(
    [("system", "you are a bot"), ("human", "{input}")]
)

# 将提示模板与语言模型链接
chain = prompt | llm


# 定义一个异步函数，用于处理语言链的事件
async def process_input():
    idx = 0
    async for event in chain.astream_events({"input": "hello there!"}, version="v1"):
        print(event)
        idx += 1
        if idx > 7:
            break


# 在主块中启动异步事件循环
if __name__ == '__main__':
    asyncio.run(process_input())
    from langchain_core.output_parsers import JsonOutputParser
