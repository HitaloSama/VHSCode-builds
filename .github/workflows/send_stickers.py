import os

import pyrogram

with pyrogram.Client(
    "bot", os.getenv("API_ID"), os.getenv("API_HASH"), bot_token=os.getenv("BOT_TOKEN")
) as client:
    client.send_sticker(
        chat_id=os.getenv("CHAT_ID"),
        sticker="https://raw.githubusercontent.com/Project-WKF/Nekogram-Builds/master/.github/workflows/separator.webp",
        disable_notification=True,
    )
