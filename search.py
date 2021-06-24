import datastore

class Search:

        
    def general_search():
        

            search_term = input("What would you like to search?\n").capitalize()
            search_list = 0
            print("================================================")
            print("Results:\n")

            for book in datastore.book_list:
                if(book['title'].find(search_term) != -1):
                    print(f"{book['title'].ljust(30)} {book['author'].ljust(20)} {str(book['onloan'])}")
                    search_list += 1
                else:
                    continue

            if search_list == 0:
                print(f'There are no books with this word')

            input("Return to continue...")

    #general_search() 


    def print_user_list ():
        print()

    def print_borrowed_book_list():
        print()

    def print_book_list():
        print()

    def display_users():
        print()
