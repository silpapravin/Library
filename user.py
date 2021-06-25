


class User:
    #constructor
    def __init__(self, username, password, ID, name, surname, borrowing, borrowed, is_librarian):
        borrowing = []
        borrowed = []
        self._username=username
        self._password=password
        self._ID=ID
        self._name=name
        self._surname = surname
        self._borrowing=borrowing #need to come back to boolean values in constructor and lists
        self._borrowed=borrowed
        self._is_librarian = is_librarian

    def description(self):
        return f"User:       {str(self._ID).ljust(4)} {self._name.ljust(20)} {self._surname.ljust(25)}"
