# 测试类的实例化和输出
from aily_sdk.message.button import Button

test_button = Button(btn_type="primaryFilled", width="200px", action="message", message="新消息是什么", skill="技能名")
print(test_button.to_message())