import json
from loguru import logger
from aily.openapi.assistant.beta import AssistantClient
from aily.openapi.assistant.errors import AilyTimeoutError

# 关闭 loguru 的日志输出
# logger.remove()

# 固定的 app_id
app_id = "spring_ec9b314b50__c"

# 通过 input() 函数接收用户输入的 content
content = input("用户: ")

# 初始化 AssistantClient
client = AssistantClient()
client.use_user_access_token(json.load(open('../../.env.json'))['user_access_token'])

# 使用用户输入的 content 和固定的 app_id
try:
    message = client.chat_completions.create(app_id=app_id, content=content)
    print('Assistant:' + message.content)
except AilyTimeoutError as e:
    print(e)
