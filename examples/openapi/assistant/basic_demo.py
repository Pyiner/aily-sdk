import json
import time
from loguru import logger
from aily.openapi.assistant.beta import AssistantClient

app_id = "spring_ec9b314b50__c"
content = 'aPaaS的负责人是谁'

# 初始化 AssistantClient
client = AssistantClient()
client.use_user_access_token(json.load(open('../../.env.json'))['user_access_token'])

# 创建一个session
session = client.sessions.create()

# 创建消息
client.messages.create(
    session_id=session.id,
    content=content
)

# 创建运行
run = client.runs.create(session_id=session.id, app_id=app_id)

# 轮询判断运行状态
start_time = time.time()
timeout = 60
poll_interval = 1
while True:
    run = client.runs.retrieve(session_id=session.id, run_id=run.id)
    if run.status in ["COMPLETED", "FAILED", "CANCELLED", "EXPIRED"]:
        break

    elapsed_time = time.time() - start_time
    if elapsed_time >= timeout:
        logger.warning(f"Run {run.id} timed out after {timeout} seconds.")
        break
    time.sleep(poll_interval)

# 获取消息列表
messages = client.messages.list(session_id=session.id, run_id=run.id)
for msg in messages:
    print(f'{msg.sender.sender_type}:{msg.content}')
