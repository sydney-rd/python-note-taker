from peewee import *

db = PostgresqlDatabase('notes',
                        user='sydneydavid',
                        password='123',
                        host='localhost',
                        port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Notes(BaseModel):
    title = CharField()
    content = CharField()

db.create_tables([Notes])

