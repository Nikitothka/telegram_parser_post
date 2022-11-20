from pyrogram import Client, filters
from mysql import connector
from dotenv import load_dotenv
import os


# print(dir(connector.connect))
class DataBase:

    def __init__(self, user, password, host, port, database):
        self.cnx = connector.connect(host=host, port=int(port), user=user, password=password, database=database)
        self.cursor = self.cnx.cursor(dictionary=True)

    try:
        async def add_photo(self, channel_id: int, username: str, file_id: str, message: str, caption: str,
                            caption_entities: str):
            return self.cursor.execute(
                'INSERT INTO posts(channel_id, username, file_id, text, json, entity)\n'
                'VALUES(%s, %s, %s, %s, %s, %s)',
                (channel_id, username, file_id, caption, message, caption_entities))
    except Exception as ex:
        print(ex)
    try:
        async def add_photo_group(self, channel_id: int, username: str, file_id: str, message: str, caption: str,
                                  caption_entities: str, media_group_id: int):
            return self.cursor.execute(
                'INSERT INTO posts(channel_id, username, file_id, text, json, entity, media_group_id)\n'
                'VALUES(%s, %s, %s, %s, %s, %s, %s)',
                (channel_id, username, file_id, caption, message, caption_entities, media_group_id))
    except Exception as ex:
        print(ex)

    try:
        async def text(self, channel_id: int, username: str, message: str, caption: str,
                       caption_entities: str):
                    return self.cursor.execute(
                        'INSERT INTO posts(channel_id, username, text, json, entity)\n'
                        'VALUES(%s, %s, %s, %s, %s)',
                        (channel_id, username, caption, message, caption_entities))
    except Exception as ex:
        print(ex)
    
    # async def web_app(self, channel_id, username, file_id, message, caption):
    #     return self.cursor.execute("""INSERT INTO posts(`id`, `username`, `file_id`, `message`,'caption')
    #                                VALUES(%s, %s, %s, %s, %s)""", (channel_id, username, file_id, message, caption))
    #
    try:
        async def document(self, channel_id: int, username: str, file_id: str, message: str, caption: str,
                                  caption_entities: str, media_group_id: int):
            return self.cursor.execute(
                'INSERT INTO posts(channel_id, username, file_id, text, json, entity, media_group_id)\n'
                'VALUES(%s, %s, %s, %s, %s, %s, %s)',
                (channel_id, username, file_id, caption, message, caption_entities, media_group_id))
    except Exception as ex:
        print(ex)

    # async def add_interests(self):
    #     pass


load_dotenv()

db = DataBase(user=os.getenv("USER_DB"),
              password=os.getenv("PASSWORD_DB"),
              host=os.getenv("HOST_DB"),
              port=(os.getenv("PORT_DB")),
              database=os.getenv("DATABASE_NAME")
              )
# print(os.getenv("USER"))
