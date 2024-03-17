from database_db import Database
import Class
import main
from Class import Uzum

def praducts(email, password):
    query = """SELECT * FROM product"""
    data = Database.connect(query, "select")
    for i in data:
        print(f"""
                ID: {i[0]}
                Name: {i[1]}
                Modell: {i[2]}
                Color: {i[3]}
                Price: {i[4]}
            """)
    back = input("""

    1. Maxsulot qo'shish
    2. Maxsulotni olib tashlash
    0. Back 
        >>> """)
    if back == "1":
        name = input("Enter product name: ")
        model = input("Enter madel: ")
        color = input("Enter color: ")
        price = input("Enter your price: ")
        print(Uzum.insert_seller(name, model, price, color))
        return praducts(email, password)

    elif back == "2":
        tabl = "product"
        column_name = input("Enter column name: ")
        data = input("Enter data: ")
        if column_name.lower() == "id":
            id = "product_id"
            print(Uzum.deleted_id(tabl, id, data))
            return praducts(email, password)
        else:
            print(Uzum.delete(tabl, column_name, data))
            return praducts(email, password)

    elif back == "0":
        return seller(email,password)
    else:
        print("Invalid")
        return seller(email, password)



def select_seller(email, password):
    query = """SELECT * FROM seller"""
    data = Database.connect(query, "select")
    for i in data:
        if i[3] == email and i[4] == password:
            print(f"""
                   ID: {i[0]}
                   First Name: {i[1]}
                   Last Name: {i[2]}
                   Email: {i[3]}
                   Password: {i[4]}
                   """)
            back = input("""
        1. Update
        0. Back
            >>> """)

            if back == "1":
                column_name = input("Enter your column name: ")
                old_data = input("Enter your old data: ")
                new_data = input("Enter your new data: ")
                table = 'seller'
                if column_name.lower() == "id":
                    column_name = "seller_id"
                    print(Uzum.update_id(table, column_name, old_data, new_data))
                    return select_seller(email, password)
                elif column_name.lower() != "id":
                    print(Uzum.update(table, column_name, old_data, new_data))
                    print(select_seller(email, password))
                    return select_seller(email, password)
                else:
                    print("Invalid column")
                    return select_seller(email, password)

            if back == "0":
                return seller(email, password)
            else:
                print("Invalid")
                return select_seller(email, password)




def seller(email, password):
    print("<< Seller >>")
    bolimlar = input("""
            1. Profil
            2. Praduct
            0. Log Out
                >>> """)

    if bolimlar == "1":
        return select_seller(email, password)
    if bolimlar == "2":
        return praducts(email, password)
    if bolimlar == "0":
        return main.main()
    else:
        print("Invalid")
        return seller(email, password)
