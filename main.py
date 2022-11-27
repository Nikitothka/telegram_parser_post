from pyrogram import Client, filters
from dotenv import load_dotenv
import os
from have_attribute import have_entities, have_entities_text
from database import db

load_dotenv()
app = Client("my_account", api_id=(os.getenv("API_ID")), api_hash=(os.getenv("API_HASH")))


@app.on_message(filters=filters.channel & filters.photo & filters.media_group)
async def photo_group(client, message):
    try:
        await app.send_photo(chat_id=int(os.getenv("ID_BOT")), photo=message.photo.file_id,
                             caption=message.photo.file_id)

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

        await db.add_photo(channel_id=int(message.chat.id),
                           username=str(message.chat.username),
                           file_id=str(message.photo.file_id),
                           caption=str(message.caption),
                           message=str(message),
                           caption_entities=have_entities(message)
                           )
        await app.send_photo(chat_id=int(os.getenv("ID_BOT")), photo=message.photo.file_id,
                             caption=message.photo.file_id)

    except Exception as ex:
        print(ex)


@app.on_message(filters=filters.channel & filters.text)
async def text(client, message):
    try:

        await db.text(channel_id=int(message.chat.id),
                      username=str(message.chat.username),
                      caption=str(message.text),
                      message=str(message),
                      caption_entities=have_entities_text(message)
                      )

    except Exception as ex:
        print(ex)


@app.on_message(filters=filters.channel & filters.document)
async def document(client, message):
    try:

        await db.document(channel_id=int(message.chat.id),
                          username=str(message.chat.username),
                          file_id=str(message.document.file_id),
                          caption=str(message.caption),
                          message=str(message),
                          caption_entities=have_entities(message),
                          media_group_id=int(message.media_group_id)
                          )
        await app.send_document(chat_id=int(os.getenv("ID_BOT")), document=message.photo.file_id,
                             caption=message.document.file_id)

    except Exception as ex:
        print(ex)


app.run()
