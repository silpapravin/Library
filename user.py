class User:
    #constructor
    def __init__(self, username, password, id, name, surname, borrowing, borrowed, is_librarian):
        self._username=username
        self._password=password
        self._id=id
        self._name=name
        self._surname=surname
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
    def password(self):
        return self._password
    
    @password.setter 
    def password(self, new_password):
        self._password = new_password
     
    @property
    def id(self):
        return self._id
    
    @id.setter 
    def id(self, new_id):
        self._id = new_id
        
    @property
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, new_name):
        self._name = new_name
    
    @property
    def surname(self):
        return self._surname
    
    @surname.setter 
    def surname(self, new_surname):
        self._surname = new_surname
        
    @property
    def borrowed(self):
        return self._borrowed
    
    @borrowed.setter 
    def borrowed(self, new_borrowed):
        self._borrowed = new_borrowed
        
    @property
    def borrowing(self):
        return self._borrowing
    
    @borrowing.setter 
    def borrowing(self, new_borrowing):
        self._borrowing = new_borrowing
        
    @property
    def is_librarian(self):
        return self._is_librarian
    
    @is_librarian.setter 
    def is_librarian(self,new_is_librarian):
        self._is_librarian = new_is_librarian


    def description(self):
        return f"Users:  {self._id.ljust(10)} {str(self._name).ljust(20)} {str(self._surname).ljust(20)}{self._borrowing.ljust(10)} {str(self._is_librarian).ljust(10)}"
