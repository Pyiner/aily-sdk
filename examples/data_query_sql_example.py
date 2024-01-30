import json

from aily_sdk.openapi.data import DataClient

data_api = DataClient(json.load(open('.env.json'))['user_access_token'])

# 准备查询参数
query_params = {
    'app_id': 'spring_a3ff04b1f6__c',
    "query": "SELECT doc_url_aadfrqjpdy4du FROM object_doc_url_aadfrqjpdysau_dataset_aadfvkmolhybgzkb67 LIMIT 10",
    "option": {
        "stringify_number": False,
        "normalize_column_name": False
    },
    "table_type": "dataset"
}

# 通过 DataAPI 发送请求
response = data_api.query_sql(query_params)
print('code: ', response.code)
print('records: ', response.records)
print('msg', response.msg)
