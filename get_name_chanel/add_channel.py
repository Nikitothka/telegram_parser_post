import time

from pyrogram import Client, filters
from dotenv import load_dotenv
import os
from database import db
import asyncio
from pyrogram.errors import FloodWait

load_dotenv()


async def main():
    load_dotenv()
    cnt = 0
    try:
        async with Client("my_account", api_id=(os.getenv("API_ID")), api_hash=(os.getenv("API_HASH"))) as app:

            username_list = await db.get_names()
            for username_dict in username_list:
                username = username_dict['username']
                chat_info = (await app.get_chat(username))
                try:
                    time.sleep(10)
                    await app.join_chat(username)
                    await db.channels_update_id(channel_id=chat_info.id,
                                                title=chat_info.title,
                                                username=username)
                    print(cnt)
                    cnt += 1
                except FloodWait as e:
                    print(e.value)
                    await asyncio.sleep(e.value)

                except Exception as ex:
                    print(ex, username)



    except FloodWait as e:
        print(e.value)
        await asyncio.sleep(e.value)


asyncio.run(main())
