from datastore import book_list
from book import Book
from menu import Menu

class Search:

    local_book_list = book_list

    def general_search(book_list):
            
            print(book_list)
            search_term = input("What would you like to search?\n").lower()
            search_list = []
            print("================================================")
            

            for book in book_list:
                if (book.title.lower().count(search_term)) or (book.author.lower().count(search_term)):
                    search_list.append(book)
                         
                else:
                    continue
                
                print(f"Results: {len(search_list)}\n")
                for book in search_list:
                    print(book.description())
        
            if len(search_list) == 0:
                print(f'There are no books with this word')

            input("Return to continue...")


    def print_user_list ():
        print()

    def print_borrowed_book_list():
        print()

    def print_book_list():
        print()

    def display_users():
        print()

    general_search(local_book_list) 
    #print(local_book_list)

    #checking access to attibutes
    def checking_attributes():
        for book in book_list:
            print(str(book.title))

    #checking_attributes()