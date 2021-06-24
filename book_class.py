
class Book: 
    def __init__(self, title, author, book_id, on_loan, date_loaned):
        self.title = title
        self.author = author 
        self.book_id = book_id
        self.on_loan = on_loan
        self.date_loaned = date_loaned
    
    def print_book(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("ID:", self.book_id)
        print("On Loan:", self.on_loan)
        print("Date Loaned:", self.date_loaned)


book_1 = Book("Where The Wild Things Are", "Maurice Sandak", "9009", False, "01/02/2021" )

book_1.print_book()
