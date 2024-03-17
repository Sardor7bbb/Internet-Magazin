from database_db import Database
from Costomer import customer
from Seller import seller

import main


def login():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    query = f"SELECT first_name,email,password FROM customer WHERE email = '{email}' AND password = '{password}'"
    query2 = f"SELECT first_name,email,password FROM seller WHERE email = '{email}' AND password = '{password}' "

    natija = Database.connect(query, "select")

    natija2 = Database.connect(query2, "select")

    if len(natija or natija2) == 0:
        print("Email yoki password xato! ")
        return main.main()
    elif len(natija) != 0:
        print(f"<<<<<<<<<<<<<<<<< Salom {natija[0][0]} >>>>>>>>>>>>>>>>>>")
        return customer(email, password)
    elif len(natija2) != 0:
        print(f"<<<<<<<<<<<<<<<<< Salom {natija2[0][0]} >>>>>>>>>>>>>>>>>>")
        return seller(email, password)
    else:
        print("Invalid email or password")
