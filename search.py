from datastore import book_list
from book import Book

class Search:

       
    def general_search(book_list):
        
            print(book_list)
            search_term = input("What would you like to search?\n").lower()
            search_list = 0
            print("================================================")
            print("Results:\n")

            for book in book_list:
                book_title = str(getattr(book,'title')).lower()
                if(book_title.find(search_term) != -1):
                    print(book.description())
                    #print(f"{str(getattr(book,'title')).ljust(30)} {str(getattr(book,'author')).ljust(20)} {str(getattr(book,'on_loan'))}")
                    search_list += 1
                else:
                    continue

            if search_list == 0:
                print(f'There are no books with this word')

            input("Return to continue...")

    general_search(book_list) 


    def print_user_list ():
        print()

    def print_borrowed_book_list():
        print()

    def print_book_list():
        print()

    def display_users():
        print()
