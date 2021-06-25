class User:
    #constructor
    def __init__(self, username, password, id, name, borrowing, borrowed, is_librarian):
        self._username=username
        self._password=password
        self._id=id
        self._name=name
        self._borrowing=borrowing #need to come back to boolean values in constructor and lists
        self._borrowed=borrowed
        self._is_librarian=is_librarian

    #getters and setters
    @property
    def get_username(self):
        return self._username
    
    @username.setter 
    def set_username(self, new_username):
        self._username = new_username
        
    @property
    def get_password(self):
        return self._password
    
    @password.setter 
    def set_password(self, new_password):
        self._password = new_password
     
    @property
    def get_id(self):
        return self._id
    
    @id.setter 
    def set_id(self, new_id):
        self.__id = new_id
        
    @property
    def get_name(self):
        return self._name
    
    @name.setter 
    def set_name(self, new_name):
        self.__name = new_name
        
    @property
    def get_borrowed(self):
        return self._borrowed
    
    @borrowed.setter 
    def set_borrowed(self, new_borrowed):
        self.__borrowed = new_borrowed
        
    @property
    def get_borrowing(self):
        return self._borrowing
    
    @borrowing.setter 
    def set_borrowing(self, new_borrowing):
        self.__borrowing = new_borrowing
        
    @property
    def get_is_librarian(self):
        return self._is_librarian
    
    @is_librarian.setter 
    def set_is_librarian(self,new_is_librarian):
        self.__is_librarian = new_is_librarian


    


    def description(self):
        return f"User:       {str(self.__username).ljust(10)} {self.__password.ljust(20)} {self.__id.ljust(10)} {self.__name.ljust(20)} {self.__borrowing.ljust()} {self.__borrowed.ljust()} {self.__is_librarian.ljust()}"
