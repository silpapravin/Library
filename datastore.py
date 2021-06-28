import datetime
from user import User
from book import Book
    
#create an empty list of users
user_list = []

#create an empty list of books
book_list = []

#adding some sample books

def add_books():

    book_list.append(Book("The Very Hungry Caterpillar", "Eric Carle","8008", False, "Available"))
    book_list.append(Book("The Giving Tree", "Shel Silverstein", "1002", False, "Available"))
    book_list.append(Book("Green Eggs and Ham", "Dr. Suess", "1200", True, "04/06/2021"))
    book_list.append(Book("Goodnight Moon", "Margaret Wise Brown", "7006", True, "02/06/2021"))
    book_list.append(Book("Charlotte's Web", "E.B. White", "2300",  False, "Available"))
    book_list.append(Book("The Lion, The Witch and The Wardrobe",  "C.S. Lewis",  "3005", True, "29/05/2021"))
    book_list.append(Book("She: A History of Adventure", "H. Rider Haggard", "6203",  False, "Available"))
    book_list.append(Book("Charlotte's Web", "E.B. White", "8877", False, "Available"))
    book_list.append(Book("Alice's Adventures in Wonderland", "Lewis Carroll", "6556", False, "Available"))
    book_list.append(Book("The Hobbit", "J.R.R. Tolkien", "4554", True, "31/05/2021"))
    book_list.append(Book("And Then There Were None", "Agatha Christie", "6432", False, "Available"))
    book_list.append(Book("Harry Potter", "J.K. Rowling", "3221", False, "Available"))
    book_list.append(Book("The Little Prince", " Antoine de Saint-Exupéry", "1234", True, "01/06/2021"))
    book_list.append(Book("The Lord of The Rings", "J.R.R. Tolkien", "8899", False, "Available"))
    book_list.append(Book("A Tale of Two Cities", "Charles Dickens", "3993", False, "Available"))
    book_list.append(Book("The Little Prince", " Antoine de Saint-Exupéry","5664", True, "24/06/2021"))
    book_list.append(Book("Everything I Know About Love", "Dolly Adlerton", "5536", False, "Available"))

add_books()


def add_users():
    
    user_list.append(User("SumayaAlmeida", "1234", "001", "Sumaya", "Almeida", "", "", True ))
    user_list.append(User("AnnaTimoteva", "1234", "002", "Anna", "Timoteva", [book_list[12], book_list[9]], [book_list[9]], False ))
    user_list.append(User("MeganDavitt", "1234", "003", "Megan", "Davitt", [book_list[2], book_list[3]], [book_list[0], book_list[10]], False ))
    user_list.append(User("EstherJoseph", "1234", "004", "Esther", "Joseph", [], [], False ))
    user_list.append(User("FergusDeffely", "1234", "005", "Fergus", "Deffely", "", "", True ))


add_users()


#for user in user_list:
    #print(user.description())

#for book in book_list:
    #print(book.description())