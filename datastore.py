import datetime
from user import User
from book import Book

class Datastore:

    def __init__(self):
        #create an empty list of users
        self.user_list = []

        #create an empty list of books
        self.book_list = []

        self.add_books()
        self.add_users()

    #adding some sample books

    def add_books(self):

        self.book_list.append(Book("The Very Hungry Caterpillar", "Eric Carle","8008", False, "Available"))
        self.book_list.append(Book("The Giving Tree", "Shel Silverstein", "1002", False, "Available"))
        self.book_list.append(Book("Green Eggs and Ham", "Dr. Suess", "1200", True, "04/06/2021"))
        self.book_list.append(Book("Goodnight Moon", "Margaret Wise Brown", "7006", True, "02/06/2021"))
        self.book_list.append(Book("Charlotte's Web", "E.B. White", "2300",  False, "Available"))
        self.book_list.append(Book("The Lion, The Witch and The Wardrobe",  "C.S. Lewis",  "3005", True, "29/05/2021"))
        self.book_list.append(Book("She: A History of Adventure", "H. Rider Haggard", "6203",  False, "Available"))
        self.book_list.append(Book("Charlotte's Web", "E.B. White", "8877", False, "Available"))
        self.book_list.append(Book("Alice's Adventures in Wonderland", "Lewis Carroll", "6556", False, "Available"))
        self.book_list.append(Book("The Hobbit", "J.R.R. Tolkien", "4554", True, "31/05/2021"))
        self.book_list.append(Book("And Then There Were None", "Agatha Christie", "6432", False, "Available"))
        self.book_list.append(Book("Harry Potter", "J.K. Rowling", "3221", False, "Available"))
        self.book_list.append(Book("The Little Prince", " Antoine de Saint-Exupéry", "1234", True, "01/06/2021"))
        self.book_list.append(Book("The Lord of The Rings", "J.R.R. Tolkien", "8899", False, "Available"))
        self.book_list.append(Book("A Tale of Two Cities", "Charles Dickens", "3993", False, "Available"))
        self.book_list.append(Book("The Little Prince", " Antoine de Saint-Exupéry","5664", True, "24/06/2021"))
        self.book_list.append(Book("Everything I Know About Love", "Dolly Adlerton", "5536", False, "Available"))

    def add_users(self):
        
        self.user_list.append(User("SumayaAlmeida", "1234", "001", "Sumaya", "Almeida", "", "", True ))
        self.user_list.append(User("AnnaTimoteva", "1234", "002", "Anna", "Timoteva", [self.book_list[12], self.book_list[9]], [self.book_list[9]], False ))
        self.user_list.append(User("MeganDavitt", "1234", "003", "Megan", "Davitt", [self.book_list[2], self.book_list[3]], [self.book_list[0], self.book_list[10]], False ))
        self.user_list.append(User("EstherJoseph", "1234", "004", "Esther", "Joseph", [], [], False ))
        self.user_list.append(User("FergusDeffely", "1234", "005", "Fergus", "Deffely", "", "", True ))


#for user in user_list:
    #print(user.description())

#for book in self.book_list:
    #print(book.description())