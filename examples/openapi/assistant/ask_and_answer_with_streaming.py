import json
from loguru import logger
from aily.openapi.assistant.beta import AssistantClient

# 关闭 loguru 的日志输出
logger.remove()

# 固定的 app_id

# 初始化 AssistantClient
client = AssistantClient()
client.use_user_access_token(json.load(open('../../.env.json'))['user_access_token'])

app_id = "spring_9e840c7201__c"
content = '飞书文档怎么用'
skill_id = 'skill_2512705ef9da'

# 使用用户输入的 content 和固定的 app_id
stream = client.chat_completions.create(app_id=app_id, content=content, skill_id=skill_id, stream=True)

for msg in stream:
    print(msg.content)
