import os
import user_file
import user_menu
import librarian_menu


active_user=""
user_list = user_file.user_list
count=len(user_list)

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
    elif(choice==2):
       newRegistration()
    else:
        print("Invalid Entry..Exiting application")
        exit()


def user_login():
    found=False
    user_name=input("Enter Username:  ")
    for user in user_list:
        if (user['Username']==user_name):
           pass_word=input("Enter password:  ")
           if (user['Password']==pass_word):
              found=True
              status=user['isLibrarian']
              active_user=user
              break
           else:
               found=False
               break
          
    if (found==True):
        print("Login Sucesssful")
        if (status==True): 
           librarian_menu.display_librarian_menu()
           print("")
        else:
            user_menu.display_user_menu()
            print("")
    else:
        print("Login Unsuccessful")
        #user_login()
    return

def newRegistration():
    #user_list=user_file.user_list()
    count=len(user_list)
    count=count+1
    print(" Enter registration details")
    print("ID Number :", count)
    user_name=input("Enter a username :")
    pass_word=input("Enter a password :")
    firstname=input("Enter First Name :")
    surname=input("Enter Surname :")
    books=[]
    user_list.append({"IDNumber": count, "isLibrarian": False, "Username": user_name, "Password": pass_word, "Name":firstname, "Surname": surname, "BorrewedBooks":[]})
    print("Welcome  ",firstname)
    print("Please Login to your account")
    user_login()
    
#calling function
        
#login_menu()

