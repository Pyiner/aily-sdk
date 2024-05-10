import json
from loguru import logger
from aily.openapi.assistant.beta import AssistantClient

# 关闭 loguru 的日志输出
# logger.remove()

# 固定的 app_id
# 通过 input() 函数接收用户输入的 content
app_id = "spring_9e840c7201__c"
content = '飞书文档怎么用'
skill_id = 'skill_2512705ef9da'

# 初始化 AssistantClient
client = AssistantClient()
client.use_user_access_token(json.load(open('../../.env.json'))['user_access_token'])

# 使用用户输入的 content 和固定的 app_id
message = client.chat_completions.create(app_id=app_id, content=content, skill_id=skill_id, unique_user_id='123')

print('Assistant:' + message.content)
