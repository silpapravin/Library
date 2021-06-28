
from util import Util
# from datastore import book_list
# from datastore import user_list
from datastore import Datastore

class Search:

    @staticmethod
    def general_search(book_list):
            Util.clear_screen()
            #print(book_list)
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


    def print_user_list (user_list):
        for user in user_list:
            print(user.description())

    def print_borrowed_book_list(book_list):
        for book in book_list:
            if  book.on_loan == True:
                print(book.description())

    def print_book_list(book_list):
        for book in book_list:
            print(book.description())

    def display_users():
        print()

    #general_search(local_book_list) 
    #print(local_book_list)

    #checking access to attibutes
    def checking_attributes():
        for book in book_list:
            print(str(book.title))

    #checking_attributes()