import json

from loguru import logger
from aily.openapi.card_message import CardMessageClient

config = json.load(open('../../.env.json'))

cmc = CardMessageClient()
cmc.use_tenant_access_token(app_id=config['app_id'], app_secret=config['app_secret'])
r = cmc.send_message(
    template_id='AAqUdngXdszsN',
    template_version_name='1.0.5',
    template_variable={
        "summary": '123',
        "group_data": [{
            "user_count": 123,
            "message_count": 123,
            "neutral_count": 123,
            "positive_count": 123,
            "negative_count": 123,
            "nm_list": 'nm_list',
            "group_name": '123123123'
        }]
    },
    receive_id='ou_697f21450a58570e9afeacc88f2dc33f'
)
logger.info(r.message_id)
r = cmc.reply_message(
    template_id='AAqUdngXdszsN',
    template_version_name='1.0.5',
    template_variable={
        "summary": '123',
        "group_data": [{
            "user_count": 123,
            "message_count": 123,
            "neutral_count": 123,
            "positive_count": 123,
            "negative_count": 123,
            "nm_list": 'nm_list',
            "group_name": '123123123'
        }]
    },
    message_id='om_f5807483c5557c0244d02b3a7be3d219',
)
logger.info(r.message_id)
