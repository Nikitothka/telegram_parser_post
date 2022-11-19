from pyrogram import Client, filters
from dotenv import load_dotenv
import os
from have_attribute import have_entities
from database import db

load_dotenv()
app = Client("my_account", api_id=(os.getenv("API_ID")), api_hash=(os.getenv("API_HASH")))


@app.on_message(filters=filters.channel & filters.photo & filters.media_group)
async def photo_group(client, message):
    try:
        await db.add_photo_group(channel_id=int(message.chat.id),
                                 username=str(message.chat.username),
                                 file_id=str(message.photo.file_id),
                                 caption=str(message.caption),
                                 message=str(message),
                                 caption_entities=have_entities(message),
                                 media_group_id=int(message.media_group_id)
                                 )

    except Exception as ex:
        print(ex)

@app.on_message(filters=filters.channel & filters.photo & ~filters.media_group)
async def photo(client, message):
    try:
        await db.add_photo(channel_id = int(message.chat.id),
                           username=str(message.chat.username),
                           file_id=str(message.photo.file_id),
                           caption=str(message.caption),
                           message=str(message),
                           caption_entities=have_entities(message)
                           )

    except Exception as ex:
        print(ex)

# @app.on_message(filters=filters.channel & filters.text)
# async def photo(client, message):
#     try:
#         await db.add_photo(channel_id = int(message.chat.id),
#                            username=str(message.chat.username),
#                            file_id=str(message.photo.file_id),
#                            caption=str(message.caption),
#                            message=str(message),
#                            caption_entities=str(message.caption_entities.MessageEntity))
#
#     except Exception as ex:
#         print(ex)


# @app.on_message(filters=filters.channel & filters.web_page)
# async def incoming(client, message):
#     try:
#        print(message)
#     except Exception as ex:
#         print(ex)
#
# @app.on_message(filters=filters.channel & filters.document)
# async def incoming(client, message):
#     try:
#        print(message)
#     except Exception as ex:
#         print(ex)

app.run()
