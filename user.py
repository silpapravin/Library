class User:
    #constructor
    def __init(self, username, password, id, name, borrowing, borrowed, is_librarian):
        self.__username=username
        self.__password=password
        self.__id=id
        self.__name=name
        self.__borrowing=borrowing #need to come back to boolean values in constructor and lists
        self.__borrowed=borrowed
        self.__is_librarian=is_librarian

    #getters and setters
    @property
    def get_username(self):
        return self.__username
    
    @username.setter 
    def set_username(self, new_username):
        self.__username = new_username
        
    @property
    def get_password(self):
        return self.__password
    
    @password.setter 
    def set_password(self, new_password):
        self.__password = new_password
     
    @property
    def get_ID(self):
        return self.__ID
    
    @id.setter 
    def set_id(self, new_id):
        self.__id = new_id
        
    @property
    def get_name(self):
        return self.__name
    
    @name.setter 
    def set_name(self, new_name):
        self.__name = new_name
        
    @property
    def get_borrowed(self):
        return self.__borrowed
    
    @borrowed.setter 
    def set_borrowed(self, new_borrowed):
        self.__borrowed = new_borrowed
        
    @property
    def get_borrowing(self):
        return self.__borrowing
    
    @borrowing.setter 
    def set_borrowing(self, new_borrowing):
        self.__borrowing = new_borrowing
        
    @property
    def get_is_librarian(self):
        return self.__is_librarian
    
    @is_librarian.setter 
    def set_is_librarian(self,new_is_librarian):
        self.__is_librarian = new_is_librarian


    


    def description(self):
        return f"User:       {str(self.__username).ljust(10)} {self.__password.ljust(20)} {self.__id.ljust(10)} {self.__name.ljust(20)} {self.__borrowing.ljust()} {self.__borrowed.ljust()} {self.__is_librarian.ljust()}"
