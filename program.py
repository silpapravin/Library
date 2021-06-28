from datastore import Datastore
from login_methods import LoginMethods

datastore = Datastore()
login_menu = LoginMethods() 

login_menu.login_menu(datastore)





