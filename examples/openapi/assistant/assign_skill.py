import json
from loguru import logger
from aily.openapi.assistant.beta import AssistantClient

# 关闭 loguru 的日志输出
# logger.remove()

# 固定的 app_id
app_id = "spring_dd58222228__c"
skill_id = "skill_37c515ad6a11"
content = "谁是aPaaS产品负责人"

# 初始化 AssistantClient
client = AssistantClient()
client.use_user_access_token(json.load(open('../../.env.json'))['user_access_token'])

# 指定技能并传入参数
message = client.chat_completions.create(app_id=app_id, content=content, skill_id=skill_id, skill_input={
    'abc': "你好啊"
})

print('Assistant:' + message.content)
