import json
from aily.openapi.assistant.beta import AssistantClient

client = AssistantClient()
client.use_user_access_token(json.load(open('../../.env.json'))['user_access_token'])

files = client.upload_file([open('bps.pdf', 'rb'), open('bps.pdf', 'rb')])
print(files)
