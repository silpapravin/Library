#BOOKLIST ONLY#

booklist = []

book = {"title": "Where The Wild Things Are", "author": "Maurice Sendak", "ID": "9009", "onloan": False}
booklist.append(book)
booklist.append({"title": "The Very Hungry Caterpillar", "author": "Eric Carle","ID": "8008", "onloan": False})
booklist.append({"title": "The Giving Tree", "author": "Shel Silverstein","ID": "1002", "onloan": False})
booklist.append({"title": "Green Eggs and Ham", "author": "Dr. Suess", "ID": "1200", "onloan": True})
booklist.append({"title": "Goodnight Moon", "author": "Margaret Wise Brown", "ID": "7006", "onloan": True})
booklist.append({"title": "Charlotte's Web", "author": "E.B. White", "ID": "2300", "onloan": False})
booklist.append({"title": "The Lion, The Witch and The Wardrobe", "author": "C.S. Lewis", "ID": "3005", "onloan": True})
booklist.append({"title": "She: A History of Adventure", "author": "H. Rider Haggard", "ID": "6203", "onloan": False})
booklist.append({"title": "Charlotte's Web", "author": "E.B. White", "ID": "8877", "onloan": False})
booklist.append({"title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll","ID": "6556", "onloan": False})
booklist.append({"title": "The Hobbit", "author": "J.R.R. Tolkien", "ID": "4554", "onloan": True})
booklist.append({"title": "And Then There Were None", "author": "Agatha Christie", "ID": "6432", "onloan": False})
booklist.append({"title": "Harry Potter", "author": "J.K. Rowling", "ID": "3221", "onloan": False})
booklist.append({"title": "The Little Prince", "author": " Antoine de Saint-Exupéry", "ID": "1234", "onloan": True})
booklist.append({"title": "The Lord of The Rings", "author": " J.R.R. Tolkien", "ID": "8899", "onloan": False})
booklist.append({"title": "A Tale of Two Cities", "author": "Charles Dickens", "ID": "3993","onloan": False})
booklist.append({"title": "The Little Prince", "author": " Antoine de Saint-Exupéry","ID": "5664", "onloan": True})
booklist.append({"title": "Everything I Know About Love", "author": "Dolly Adlerton", "ID": "5536", "onloan": False})

for book in booklist:
    print(f"{book['title'].ljust(30)} {book['author'].ljust(20)} {book['ID']} {str(book['onloan'])}")