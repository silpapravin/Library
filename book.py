
class Book: 

    def __init__(self, title, author, book_id, on_loan, date_loaned):
        self._title = title
        self._author = author 
        self._book_id = book_id
        self._on_loan = on_loan
        self._date_loaned = date_loaned

#property
    def title(self):
        return self._title

#title.setter
    def title(self, new_title):
        self._title = new_title

    def author(self):
        return self._author
            
    def author(self, new_author):
        self._author = new_author
    
    def book_id(self):
        return self._book_id

    def book_id(self, new_book_id):
        self._book_id = new_book_id

    def on_loan(self):
        return self._on_loan
    
    def on_loan(self, new_on_loan):
        self._on_loan = new_on_loan
    
    def date_loaned(self):
        return self.date_loaned

    def on_loan(self, new_date_loaned):
        self._date_loaned = new_date_loaned


