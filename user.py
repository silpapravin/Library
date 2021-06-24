import datetime #for date objects
import os


class User:
    #constructor
    def __init(self, username, password, ID, name, borrowing, borrowed):
        self.username=username
        self.password=password
        self.ID=ID
        self.name=name
        self.borrowing=borrowing #need to come back to boolean values in constructor and lists
        self.borrowed=borrowed
