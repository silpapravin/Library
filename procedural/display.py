import user_file
import see_list_of_books
import login



def print_borrowed_book_list():
    print("Currently onloan books:")
    print("==================================================================================================")
    print(f"Title".ljust(50), "Author".ljust(30), "ID".ljust(30)) 
    print("==================================================================================================")

    for book in see_list_of_books.book_list:
        if book['onloan'] == True:
            print(f"{book['title'].ljust(50)} {book['author'].ljust(30)} {book['ID'].ljust(30)} {str(book['onloan'])}")

