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
    def username(self):
        return self._username
    
    @username.setter 
    def username(self, new_username):
        self._username = new_username
        
    @property
    def get_password(self):
        return self._password
    
    @password.setter 
    def password(self, new_password):
        self._password = new_password
     
    @property
    def id(self):
        return self._id
    
    @id.setter 
    def id(self, new_id):
        self.__id = new_id
        
    @property
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, new_name):
        self.__name = new_name
        
    @property
    def get_borrowed(self):
        return self._borrowed
    
    @borrowed.setter 
    def borrowed(self, new_borrowed):
        self.__borrowed = new_borrowed
        
    @property
    def borrowing(self):
        return self._borrowing
    
    @borrowing.setter 
    def borrowing(self, new_borrowing):
        self.__borrowing = new_borrowing
        
    @property
    def is_librarian(self):
        return self._is_librarian
    
    @is_librarian.setter 
    def is_librarian(self,new_is_librarian):
        self.__is_librarian = new_is_librarian


    


    def description(self):
        return f"User:       {str(self.__username).ljust(10)} {self.__password.ljust(20)} {self.__id.ljust(10)} {self.__name.ljust(20)} {self.__borrowing.ljust()} {self.__borrowed.ljust()} {self.__is_librarian.ljust()}"
