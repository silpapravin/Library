import user_file
import see_list_of_books



#Display Currently Borrowing Books:
def all_borrowed_book(): 
    print("\n\n===================================================================================================================")
    print("users with Borrowed Books:")
    print("===================================================================================================================")
    print(f"ID".ljust(8), "Username".ljust(20), "Name".ljust(20), "Surname".ljust(20), "Borrewed Books".ljust(10)) 
    print("===================================================================================================================")

    for user in user_file.user_list:
        if user ['BorrewedBooks']:
            print(f"{user['IDNumber'].ljust(8)} {user['Username'].ljust(20)} {user['Name'].ljust(20)} {user['Surname'].ljust(20)} {str(user['BorrewedBooks']).ljust(10)}") 
            #print("===================================================================================================================")


def print_borrowed_book_list():
    print("Currently onloan books:")
    print("==================================================================================================")
    print(f"Title".ljust(50), "Author".ljust(30), "ID".ljust(30)) 
    print("==================================================================================================")
    
    for book in see_list_of_books.book_list:
        if book['onloan'] == True:
            print(f"{book['title'].ljust(50)} {book['author'].ljust(30)} {book['ID'].ljust(30)} {str(book['onloan'])}")

