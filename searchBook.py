booklist = []

book = {"title": "Where The Wild Things Are", "author": "Maurice Sendak", "onloan": False}
booklist.append(book)
booklist.append({"title": "The Very Hungry Caterpillar", "author": "Eric Carle", "onloan": False})
booklist.append({"title": "The Giving Tree", "author": "Shel Silverstein", "onloan": False})
booklist.append({"title": "Green Eggs and Ham and Tree", "author": "Dr. Suess", "onloan": False})
booklist.append({"title": "Goodnight Moon", "author": "Margaret Wise Brown", "onloan": False})
booklist.append({"title": "Charlotte's Web", "author": "E.B. White", "onloan": False})

def generalSearch():
    
    searchTerm = input("What would you like to search?\n").capitalize()
    search_list = 0

    for book in booklist:
        if(book['title'].find(searchTerm) != -1):
            print(f"{book['title'].ljust(30)} {book['author'].ljust(20)} {str(book['onloan'])}")
            search_list += 1
        else:
            continue

    if search_list == 0:
        print('No results')

        
