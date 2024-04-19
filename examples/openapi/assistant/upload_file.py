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

files = client.upload_file([open('bps.pdf', 'rb'),open('bps.pdf', 'rb')])
print(files)
