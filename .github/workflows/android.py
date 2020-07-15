import os
import pyrogram

from glob import glob

with pyrogram.Client('bot', os.getenv('API_ID'), os.getenv('API_HASH'), bot_token=os.getenv('BOT_TOKEN')) as client:
    for path in glob('**/*.apk', recursive=True):
        client.send_document(
            chat_id=os.getenv('CHAT_ID'),
            document=path,
            caption=path
        )