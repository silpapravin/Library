import os
import Users
import usermenu
import librarianmenu

def clear_screen():
    os.system('cls')
   

def login_menu():
    clear_screen()
    print("Menu Options")
    print(" 1:  User Login")
    print(" 2:  User Registration")
    choice=int(input("Enter your choice:  "))
    if(choice==1):
      user_login()
    else:
      print("Contact your library for new registration")

def user_login():
    found=False
    user_list=Users.user_list
    user_name=input("Enter Username:  ")
    for user in user_list:
        if (user['Username'].find(user_name)!=-1):
           pass_word=input("Enter password:  ")
           if (user['Password'].find(pass_word)!=-1):
              found=True
              status=user['isLibrarian']
              break
           else:
               found=False
               break
          
    if (found==True):
        print("Login Sucesssful")
        if (status=="True"): 
           librarianmenu.display_librarian_menu()
           print("")
        else:
            usermenu.display_user_menu()
            print("")
    else:
        print("Login Unsuccessful")
        #user_login()
    return

#calling function
        


