import os
import pyrogram

from glob import glob

short_rev=os.getenv('SHORT_REV')
long_rev=os.getenv('LONG_REV')
branch=os.getenv('BRANCH')
time=os.getenv('TIME')

with pyrogram.Client('bot', os.getenv('API_ID'), os.getenv('API_HASH'), bot_token=os.getenv('BOT_TOKEN')) as client:
    for path in glob('**/*.apk', recursive=True):
        client.send_document(
            document=path,
            caption=f"""APK Built with the [{short_rev}](https://github.com/vhqtvn/VHEditor-Android/commit/{long_rev}) commit (Commit made on {time}).""",
        chat_id=os.getenv('CHAT_ID'),
        parse_mode="markdown"
        )