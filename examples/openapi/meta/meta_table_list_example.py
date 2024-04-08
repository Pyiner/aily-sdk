import json

from aily.openapi.meta import MetaClient

meta_api = MetaClient(json.load(open('../../.env.json'))['user_access_token'])

# 准备查询参数
query_params = {
    'app_id': 'spring_a3ff04b1f6__c',
    "table_type": "datatable",
    "access_item": "readable",  # readable\writable
    "page_size": 10,
    "page_token": "",
    # "quick_query": "",
    # "api_names": [""],
    "fill_fields": True,
    "need_total_count": True,
}

# 通过 DataAPI 发送请求
response = meta_api.table_list(query_params)
print('code: ', response.code)
print('items: ', response.items)
print('msg', response.msg)
