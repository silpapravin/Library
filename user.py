class User:
    #constructor
    def __init(self, username, password, ID, name, borrowing, borrowed, is_librarian):
        self.__username=username
        self.__password=password
        self.__ID=ID
        self.__name=name
        self.__borrowing=borrowing #need to come back to boolean values in constructor and lists
        self.__borrowed=borrowed
        self.__is_librarian=is_librarian

    #getters and setters

    def get_username(self):
        return self.__username

    def set_password(self, new_username):
        self.__username = new_username

    def get_password(self):
        return self.__password
    
    def set_password(self, new_password):
        self.__password = new_password

    def get_ID(self):
        return self.__ID
    
    def set_ID(self, new_ID):
        self.__ID = new_ID

    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name
    
    def get_borrowed(self):
        return self.__borrowed
    
    def set_borrowed(self, new_borrowed):
        self.__borrowed = new_borrowed

    def get_borrowing(self):
        return self.__borrowing
    
    def set_borrowing(self, new_borrowing):
        self.__borrowing = new_borrowing
    
    def get_is_librarian(self):
        return self.__is_librarian
    
    def set_is_librarian(self,new_is_librarian):
        self.__is_librarian = new_is_librarian


    


    def description(self):
        return f"User:       {str(self.__username).ljust(10)} {self.__password.ljust(20)} {self.__ID.ljust(10)} {self.__name.ljust(20)} {self.__borrowing.ljust()} {self.__borrowed.ljust()} {self.__is_librarian.ljust()}"
