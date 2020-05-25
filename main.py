from register import *
from login import *



choice = input("1. Login 2.Register\n")
if choice == "1":
    login()
elif choice == "2":
    register()