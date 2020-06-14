import os
import pyrogram

caption = "que nem o do Alisson Cezar"

with pyrogram.Client('bot', os.getenv('API_ID'), os.getenv('API_HASH'), bot_token=os.getenv('BOT_TOKEN')) as client:
    client.send_document(
        chat_id=os.getenv('CHAT_ID'),
        document=os.getenv('FILENAME'),
        caption=caption
    )