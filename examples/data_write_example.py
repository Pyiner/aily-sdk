import json

from aily_sdk.openapi.data import DataClient

data_api = DataClient(json.load(open('.env.json'))['user_access_token'])

# 准备查询参数
data = {
    'app_id': 'spring_a3ff04b1f6__c',
    "table_api_name": "object_doc_url_aadfrqjpdysau",
    "primary_key": "_id",
    "records": [
        {'doc_url_aadfrqjpdy4du': 'xxxx'},
    ],
    "table_type": "datatable",
}

# 通过 DataAPI 发送请求
response = data_api.write(data)
print('code: ', response.code)
print('items: ', response.items)
print('msg: ', response.msg)
