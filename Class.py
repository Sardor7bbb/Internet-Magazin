
from database_db import Database

class Uzum:
    @staticmethod
    def select(tabl):
        query = f"""SELECT * FROM {tabl}"""
        Database.connect(query, "select")


    @staticmethod
    def insert(first_name, last_name, email, password, bio, contact_url):
        query = f"""INSERT INTO student(first_name,last_name,email,password,bio,contact_url) VALUES ('{first_name}','{last_name}','{email}','{password}','{bio}','{contact_url}')"""
        Database.connect(query, "insert")


    @staticmethod
    def insert_seller(name, model, price, color):
        query = f"""INSERT INTO product(product_name, modell, color, price) VALUES ('{name}','{model}','{color}','{price}')"""
        Database.connect(query, "insert")

    @staticmethod
    def update(table, column_name, old_data, new_data):
        query = f"UPDATE {table} SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"
        return Database.connect(query, "update")


    @staticmethod
    def deleted_id(tabl, id, data):
        query = f"""DELETE FROM {tabl} WHERE {id} = {data}"""
        Database.connect(query, "delete")

    @staticmethod
    def delete(table, column_name, data):
        if type(data) == int:
            query = f"DELETE FROM {table} WHERE{column_name} = {data}"
        else:
            query = f"DELETE FROM {table} WHERE{column_name} = '{data}'"
        return Database.connect(query, "delete")

    @staticmethod
    def update_id(table, colum_name, old_data, new_data):
        query = f"UPDATE {table} SET {colum_name} = '{new_data}' WHERE {colum_name} = '{old_data}'"
        return Database.connect(query, "update")
