import os
import pyrogram

caption = "oi hitalo"

client = pyrogram.Client(':memory:', bot_token=os.getenv('BOT_TOKEN'))
client.send_document(
    chat_id=os.getenv('CHAT_ID'),
    document=os.getenv('FILENAME'),
    caption=caption
)