import json
import time
from loguru import logger
from aily.openapi.assistant.beta import AssistantClient

app_id = "spring_9e840c7201__c"
content = '飞书文档怎么用'
logger.remove()
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
run = client.runs.create(session_id=session.id, app_id=app_id, skill_id='skill_2512705ef9da')

# 轮询判断运行状态
start_time = time.time()
timeout = 60
poll_interval = 1


def load_stream_message(run_id, session_id):
    while True:
        run = client.runs.retrieve(session_id=session_id, run_id=run_id)
        if run.status in ["COMPLETED", "FAILED", "CANCELLED", "EXPIRED"]:
            messages = client.messages.list(session_id=session_id, run_id=run_id, with_partial_message=True)
            for message in messages:
                if message.sender.sender_type == 'ASSISTANT':
                    yield message
            break

        if run.status == 'IN_PROGRESS':
            messages = client.messages.list(session_id=session_id, run_id=run_id, with_partial_message=True)
            for message in messages:
                if message.sender.sender_type == 'ASSISTANT':
                    yield message

        elapsed_time = time.time() - start_time
        if elapsed_time >= timeout:
            logger.warning(f"Run {run.id} timed out after {timeout} seconds.")
            break
        time.sleep(poll_interval)


for msg in load_stream_message(session_id=session.id, run_id=run.id):
    print(msg.content)
