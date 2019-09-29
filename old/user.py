from account import Account
from note import Note
from passwordholder import PasswordHolder

class User():

    notes = []
    passwordholder = []
    
    def __init__(self, user_id, username, password, mail_id, firstname, lastname):
        self.user_id = user_id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.mail_id = mail_id
        self.account = Account(user_id, username, password)

    def add_note(self, note):
        self.notes.append(note)

    def get_all_notes(self) :
        return self.notes

    def add_password_holder(self, passwordholder):
        self.passwordholder.append(passwordholder)

    def get_all_password_holder(self) :
        return self.passwordholder