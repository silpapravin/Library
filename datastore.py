from user import User
from book import Book

#create an empty list of users
user_list = []

#create an empty list of books
book_list = []


#dd some sample users
def add_users():
    user_list.append(User("SumayaAlmeida", "1234", "001", "Sumaya", "Almeida", "", "", True ))
    user_list.append(User("AnnaTimoteva", "1234", "002", "Anna", "Timoteva", "", "", False ))
    user_list.append(User("MeganDavitt", "1234", "003", "Megan", "Davitt", "", "", False ))
    user_list.append(User("EstherJoseph", "1234", "004", "Esther", "Joseph", "", "", False ))
    user_list.append(User("FergusDeffely", "1234", "001", "Fergus", "Deffely", "", "", True ))

#add some sample books

def add_books():
    book_list.append(Book("The Very Hungry Caterpillar", "Eric Carle","8008", False, "10/06/2021"))
    book_list.append(Book("The Giving Tree","Shel Silverstein","1002", False, "11/06/2021"))
    #book_list.append({"title": "Green Eggs and Ham", "author": "Dr. Suess", "ID": "1200", "onloan": True})
    #book_list.append({"title": "Goodnight Moon", "author": "Margaret Wise Brown", "ID": "7006", "onloan": True})
    #book_list.append({"title": "Charlotte's Web", "author": "E.B. White", "ID": "2300", "onloan": False})
    #book_list.append({"title": "The Lion, The Witch and The Wardrobe", "author": "C.S. Lewis", "ID": "3005", "onloan": True})
    #book_list.append({"title": "She: A History of Adventure", "author": "H. Rider Haggard", "ID": "6203", "onloan": False})
    #book_list.append({"title": "Charlotte's Web", "author": "E.B. White", "ID": "8877", "onloan": False})
    #book_list.append({"title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll","ID": "6556", "onloan": False})
    #book_list.append({"title": "The Hobbit", "author": "J.R.R. Tolkien", "ID": "4554", "onloan": True})
    #book_list.append({"title": "And Then There Were None", "author": "Agatha Christie", "ID": "6432", "onloan": False})
    #book_list.append({"title": "Harry Potter", "author": "J.K. Rowling", "ID": "3221", "onloan": False})
    #book_list.append({"title": "The Little Prince", "author": " Antoine de Saint-Exupéry", "ID": "1234", "onloan": True})
    #book_list.append({"title": "The Lord of The Rings", "author": " J.R.R. Tolkien", "ID": "8899", "onloan": False})
    #book_list.append({"title": "A Tale of Two Cities", "author": "Charles Dickens", "ID": "3993","onloan": False})
    #book_list.append({"title": "The Little Prince", "author": " Antoine de Saint-Exupéry","ID": "5664", "onloan": True})
    #book_list.append({"title": "Everything I Know About Love", "author": "Dolly Adlerton", "ID": "5536", "onloan": False})





add_users()
add_books()

for user in user_list:
    print(user.description())

for book in book_list:
    print(book.description())