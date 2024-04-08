import json
import pprint
import time

from aily.openapi.session import Session
from aily.openapi import OpenAPIClient

client = OpenAPIClient(json.load(open('../../.env.json'))['user_access_token'])

# 通过 DataAPI 发送请求
session = Session(client, 'spring_a3ff04b1f6__c').create()

# 发送一条消息
resp = session.send_message(
    content={"content": {"widgets": [{"type": "Markdown", "props": {"content": "asd", "resources": []}}]}},
    skill_id='skill_ede3aba85e99'
)
last_operation_id = None
while True:
    o_resp = session.poll_operation(last_operation_id)
    if o_resp.intent_finished:
        pprint.pprint(o_resp.get_last_system_message())
        break
    last_operation_id = o_resp.last_operation_id
    time.sleep(5)
