from Class import Uzum
import main

from database_db import Database


def category(email, password):
    mahsulot = input("""
    Bolimni tanlang:
    
    1. Telefon
    2. Noutbook
    3. Elektronika
    4. Aksesuar
    0. Back
        >>> """)
    if mahsulot == "1":
        return telefon(email, password)
    elif mahsulot == "2":
        return noutook(email, password)
    elif mahsulot == "3":
        return elektronika(email, password)
    elif mahsulot == "4":
        return aksesuar(email, password)
    elif mahsulot == "0":
        return customer(email, password)
    else:
        print("Invalid")
        category(email, password)



def aksesuar(email, password):
    query = f"""SELECT category.category_id, product.product_id,seller.first_name,seller.last_name,product.product_name,product.modell,product.color,product.price FROM praduct_category
                              INNER JOIN seller 
                                  ON seller.seller_id = praduct_category.seller_id
                              INNER JOIN product
                                  ON product.product_id = praduct_category.product_id
                              INNER JOIN category
                                  ON category.category_id = praduct_category.category_id
                              WHERE category.category_id = 3;"""
    data = Database.connect(query, "select")
    for i in data:
        print(f"""
                  Category:{i[0]}
                  ID: {i[1]}
                  Full name: {i[2]} {i[3]}
                  Name: {i[4]}
                  Madell: {i[5]}
                  Color: {i[6]}
                  Price: {i[7]} 
                  """)
    buying = input("""
              1. Sotib olish
              0. Back
                  >>> """)

    if buying == "1":
        return buy(email, password)
    elif buying == "0":
        return category(email, password)
    else:
        print("Invalid")
        return aksesuar(email, password)

def elektronika(email, password):
    query = f"""SELECT category.category_id, product.product_id,seller.first_name,seller.last_name,product.product_name,product.modell,product.color,product.price FROM praduct_category
                          INNER JOIN seller 
                              ON seller.seller_id = praduct_category.seller_id
                          INNER JOIN product
                              ON product.product_id = praduct_category.product_id
                          INNER JOIN category
                              ON category.category_id = praduct_category.category_id
                          WHERE category.category_id = 4;"""
    data = Database.connect(query, "select")
    for i in data:
        print(f"""
              Category:{i[0]}
              ID: {i[1]}
              Full name: {i[2]} {i[3]}
              Name: {i[4]}
              Madell: {i[5]}
              Color: {i[6]}
              Price: {i[7]} 
              """)
    buying = input("""
          1. Sotib olish
          0. Back
              >>> """)

    if buying == "1":
        return buy(email, password)
    elif buying == "0":
        return category(email, password)
    else:
        print("Invalid")
        return elektronika(email, password)

def noutook(email, password):
    query = f"""SELECT category.category_id, product.product_id,seller.first_name,seller.last_name,product.product_name,product.modell,product.color,product.price FROM praduct_category
                       INNER JOIN seller 
                           ON seller.seller_id = praduct_category.seller_id
                       INNER JOIN product
                           ON product.product_id = praduct_category.product_id
                       INNER JOIN category
                           ON category.category_id = praduct_category.category_id
                       WHERE category.category_id = 2;"""
    data = Database.connect(query, "select")
    for i in data:
        print(f"""
           Category:{i[0]}
           ID: {i[1]}
           Full name: {i[2]} {i[3]}
           Name: {i[4]}
           Madell: {i[5]}
           Color: {i[6]}
           Price: {i[7]} 
           """)
    buying = input("""
       1. Sotib olish
       0. Back
           >>> """)

    if buying == "1":
        return buy(email, password)
    elif buying == "0":
        return category(email, password)
    else:
        print("Invalid")
        return noutook(email, password)


def telefon(email, password):
    query = f"""SELECT category.category_id, product.product_id,seller.first_name,seller.last_name,product.product_name,product.modell,product.color,product.price FROM praduct_category
                    INNER JOIN seller 
                        ON seller.seller_id = praduct_category.seller_id
                    INNER JOIN product
                        ON product.product_id = praduct_category.product_id
                    INNER JOIN category
                        ON category.category_id = praduct_category.category_id
                    WHERE category.category_id = 1;"""
    data = Database.connect(query, "select")
    for i in data:
        print(f"""
        Category:{i[0]}
        ID: {i[1]}
        Full name: {i[2]} {i[3]}
        Name: {i[4]}
        Madell: {i[5]}
        Color: {i[6]}
        Price: {i[7]} 
        """)
    buying = input("""
    1. Sotib olish
    0. Back
        >>> """)

    if buying == "1":
        return buy(email, password)
    elif buying == "0":
        return category(email, password)
    else:
        print("Invalid")
        return telefon(email, password)


def buy(email, password):
    kurs = input("ID raqamini kiriting: ")
    query = f"""SELECT price FROM product WHERE product_id = {kurs}"""
    data = Database.connect(query, "select")
    narx = data[0][0]
    print(narx)


    query2 = f"SELECT * FROM customer"
    data2 = Database.connect(query2, "select")
    for i in data2:
        if i[3] == email and i[4] == password:
            som = i[6]


    narxi = input(f"""
    Maxsulot narxi : {narx}$

    1. Sotib olish
    2. Bekor qilish
        >>> """)

    if narxi == "1":
        if som >= narx:
            qiymat = som - narx
            print(qiymat)
            query = f"""UPDATE customer SET balanc = '{qiymat}' WHERE email = '{email}'"""
            Database.connect(query, "update")
            print(f"""Xizmar muvofaqiyatli tugadi 
    
                    Xozirgi balanc: {qiymat}$""")
            return balanc(email, password)
        else:
            print(f"Sizda mablag yetarli emas")
            return balanc(email, password)
    elif narxi == "2":
        return customer(email, password)
    else:
        print("Invalid")
        return buy(email, password)

def balanc(email, password):
    query = """ SELECT * FROM customer """
    data = Database.connect(query, "select")
    for i in data:
        if i[3] == email and i[4] == password:
            narxi = (f"""
            Your Balancing: {i[6]}""")
            print(narxi)
            buy = input("""
        1. Narsa xaarid qilish
        0. Back
            >>> """)

            if buy == "1":
                return category(email, password)
            elif buy == "0":
                return customer(email, password)
            else:
                print("Invalid")
                return balanc(email, password)



@staticmethod
def select_customer(email, password):
    query = """SELECT * FROM customer """
    natija = Database.connect(query, "select")
    for i in natija:
        if i[3] == email and i[4] == password:
            print(f"""
                    ID: {i[0]}
                    First Name: {i[1]}
                    Last Name: {i[2]}
                    Email: {i[3]}
                    Password: {i[4]}
                    Balancing: {i[6]}
                    """)
            back = input("""
        1. Update
        0. Back
            >>> """)

            if back == "1":
                column_name = input("Column name: ")
                old_data = input("Old data: ")
                new_data = input("New data: ")
                table = "customer"
                if column_name.lower() == "id":
                    column_name = "customer_id"
                    print(Uzum.update_id(table, column_name, old_data, new_data))
                    return select_customer(email, password)
                elif column_name.lower() != "id":
                    print(Uzum.update(table, column_name, old_data, new_data))
                    return select_customer(email, password)
                else:
                    print("Invalid column")
                    return select_customer(email, password)

            if back == "0":
                return customer(email, password)
            else:
                print("Invalid")
                return select_customer(email, password)



def customer(email, password):
    print("<< Customer >>")
    headers = input("""
        1. Profil
        2. Category
        3. Balanc
        0. Log Out
            >>> """)

    if headers == "1":
        return select_customer(email, password)
    if headers == "2":
        return category(email, password)
    if headers == "3":
        return balanc(email, password)
    if headers == "0":
        return main.main()
    else:
        print("Invalid")
        return customer(email, password)
