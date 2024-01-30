import json

from aily_sdk.openapi.meta import MetaClient

meta_api = MetaClient(json.load(open('.env.json'))['user_access_token'])

# 准备查询参数
query_params = {
    'app_id': 'spring_a3ff04b1f6__c',
    "table_type": "datatable",
    "api_name": '_department',
    "fill_fields": True,
}

# 通过 DataAPI 发送请求
response = meta_api.table_meta(query_params)
print('code: ', response.code)
print('data: ', response.data)
print('msg', response.msg)
