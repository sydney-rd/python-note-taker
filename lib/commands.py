from model import *


def create(title, content):
    note = Notes(title = title, content = content)
    note.save()


