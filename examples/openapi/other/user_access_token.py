from aily.openapi import UserAccessTokenClient

# 方案一:从其他地方获取到token后直接初始化
client = UserAccessTokenClient(
    app_id='cli_***',
    app_secret='ZKPys72B***VFode4XxFyEsUY',
    user_access_token='u-etxh***8YwmKo5lgBxrG0045k02BLM',
    refresh_token='ur-f0uAA5***lgLFPG00l1k02B_R',
    expires_in=1,
    refresh_expires_in=5,
)
print(client.get_user_access_token())

# 方案二:使用code来初始化token
client = UserAccessTokenClient(
    app_id='cli_a5***0ddf100c',
    app_secret='ZKPys72Bd***eVFode4XxFyEsUY',
)
client.init_with_code('775ua6fe***c2b5ef55e1d5ebf')
print(client.get_user_access_token())
