from model import *
from playhouse.shortcuts import model_to_dict

def create(title, content):
    note = Notes(title = title, content = content)
    note.save()

def view():
    for note in Notes.select():
        print(model_to_dict(note))

def delete(note_id):
    note = Notes.get_or_none(id=note_id)
    if note:
        title = note.title
        note.delete_instance()
        print(f"Note '{title}' deleted successfully.")
    else:
        print(f"Note with ID '{note_id}' does not exist.")

