from model import *
from playhouse.shortcuts import model_to_dict

def create(title, content):
    note = Notes(title = title, content = content)
    note.save()

def view():
    for note in Notes.select():
        print(model_to_dict(note))
