import json

from aily_sdk.openapi import OpenAPIClient


class SessionResult:
    def __init__(self, result):
        self.code = result['code']
        self.msg = result['msg']

        self.session_id = None
        if 'data' in result:
            self.session_id = result['data']['session_id']


class SessionClient(OpenAPIClient):
    def create_session(self, app_id, enable_debug=False, channel_context=None):
        # 构建请求的 URL
        if channel_context is None:
            channel_context = {}
        url = f'https://open.feishu.cn/open-apis/aily/v1/apps/{app_id}/sessions'

        data = {
            'enable_debug': enable_debug,
            'channel_context': json.dumps(channel_context)
        }
        # 调用 client 的 post 方法发送请求
        return SessionResult(self.post(url, json=data))
