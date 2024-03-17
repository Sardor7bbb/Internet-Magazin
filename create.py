from database_db import Database


def create_table():


    seller_table = """
    CREATE TABLE seller (
    seller_id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(50),
    password VARCHAR(8),
    birth_date DATE,
    create_date TIMESTAMP DEFAULT now());"""


    country_table = """
    CREATE TABLE country (
    country_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    creat_date TIMESTAMP DEFAULT now());"""



    city_table = """
    CREATE TABLE city (
    city_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    country_id INT REFERENCES country(country_id),
    create_date TIMESTAMP DEFAULT now());"""

    adress_table = """
    CREATE TABLE adress (
    adress_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    city_id INT REFERENCES city(city_id),
    create_date TIMESTAMP DEFAULT now());"""


    store_table = """
    CREATE TABLE store (
    store_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    address_id INT REFERENCES adress(adress_id),
    create_date TIMESTAMP DEFAULT now());"""


    customers_table = """
    CREATE TABLE customer (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(50),
    password VARCHAR(8),
    birth_date DATE,
    balanc INT,
    address_id INT REFERENCES adress(adress_id),
    create_date TIMESTAMP DEFAULT now());"""


    category_table = """
    CREATE TABLE category (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    last_updated DATE DEFAULT now(),
    create_date TIMESTAMP DEFAULT now());"""


    product_table = """
    CREATE TABLE product (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(50),
    modell VARCHAR(20),
    color VARCHAR(20),
    price INT,
    create_date TIMESTAMP DEFAULT now());"""



    payment_tayp_table = """
    CREATE TABLE payment_tayp(
    payment_tayp_id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    create_date TIMESTAMP DEFAULT now());
    """

    payment_status_table = """
    CREATE TABLE payment_status(
    payment_status_id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    create_date TIMESTAMP DEFAULT now());"""


    payment = """
    CREATE TABLE payment(
    payment_id SERIAL PRIMARY KEY,
    amount INT,
    payment_status_id INT REFERENCES payment_status(payment_status_id),
    payment_tayp_id INT REFERENCES payment_tayp(payment_tayp_id),
    create_date TIMESTAMP DEFAULT now());"""


    office_detail_table = """
    CREATE TABLE office_detail(
    office_detail_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES product(product_id),
    customer_id INT REFERENCES customer(customer_id));
    """


    praduct_category_table = """
    CREATE TABLE praduct_category (
    praduct_category_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES product(product_id),
    category_id INT REFERENCES category(category_id),
    seller_id INT REFERENCES seller(seller_id));"""



    data = {
        "seller_table": seller_table,
        "country_table": country_table,
        "city_table": city_table,
        "adress_table": adress_table,
        "store_table": store_table,
        "customers_table": customers_table,
        "category_table": category_table,
        "product_table": product_table,
        "payment_tayp_table": payment_tayp_table,
        "payment_status_table": payment_status_table,
        "payment": payment,
        "office_detail_table": office_detail_table,
        "praduct_category_table": praduct_category_table
    }

    for i in data:
        print(f"{i} => {Database.connect(data[i], 'create')}")


if __name__ == "__main__":
    create_table()






