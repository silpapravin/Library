import os
import Users
import usermenu
import librarianmenu

def ClearScreen():
    os.system('cls')
   

def LoginMenu():
    ClearScreen()
    print("Menu Options")
    print(" 1:  User Login")
    print(" 2:  User Registration")
    choice=int(input("Enter your choice:  "))
    if(choice==1):
      UserLogin()
    else:
      print("Contact your library for new registration")

def UserLogin():
    found=False
    user_list=Users.userList
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
           librarianmenu.displayLibrarianMenu()
           print("")
        else:
            usermenu.displayUserMenu()
            print("")
    else:
        print("Login Unsuccessful")
        #UserLogin()
    return

#calling function
        


