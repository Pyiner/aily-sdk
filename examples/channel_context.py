from aily.util.channel_context import parse_channel_context


def main(arg1):
    cc = parse_channel_context(arg1, mock_data={
        'sender_id': 'developer_id'
    })
    print(cc.sender_id)


if __name__ == '__main__':
    main('''{
  "chat_id": "oc_XXXX",
  "chat_type": "p2p",
  "message_id": "om_XXXX",
  "sender_id": "ou_XXXX"
}''')
