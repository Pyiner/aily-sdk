import json

from aily_sdk.openapi.data import DataClient

data_api = DataClient(json.load(open('.env.json'))['user_access_token'])

# 准备查询参数
query_params = {
    'app_id': 'spring_a3ff04b1f6__c',
    'table_type': 'datatable',
    'table_api_name': 'object_doc_url_aadfrqjpdysau',
    'selects': [
        "doc_url_aadfrqjpdy4du"
    ],
    'page_size': 10,
    'page_token': "",
    'need_total_count': True,
}

# 通过 DataAPI 发送请求
response = data_api.query(query_params)
print('code: ', response.code)
print('records: ', response.records)
print('total: ', response.total)
print('has_more', response.has_more)



