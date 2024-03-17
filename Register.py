from database_db import Database
import Login


def register_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    password2 = input("Repeat your password: ")
    while password != password2:
        password = input("Enter your password: ")
        password2 = input("Repeat your password: ")
    birth_date = input("Enter your birth date: ")
    query = f"""INSERT INTO customer (first_name, last_name, email, password, birth_date) VALUES ('{first_name}', '{last_name}', '{email}', '{password}', '{birth_date}')"""
    Database.connect(query, "insert")
    print("Inserted into database")
    return Login.login()

