import streamlit as st
import sqlite3
import pandas as pd

def data_first_time():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Product (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        price REAL
    )''')



    cursor.execute(''' CREATE TABLE IF NOT EXISTS Sales (
        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        quantity_sold INTEGER,
        sale_date DATE,
        total_price REAL,
        FOREIGN KEY(product_id) REFERENCES Product(product_id)) ''')


    # Insert data 

    product_data = [
        (1, 'Laptop', 899.99),
        (2, 'Smartphone', 649.00),
        (3, 'Headphones', 149.95),
        (4, 'Smartwatch', 299.00),
        (5, 'Wireless Mouse', 24.99),
        (6, 'External Hard Drive', 119.99),
        (7, 'Gaming Keyboard', 79.99),
        (8, 'Monitor', 249.99),
        (9, 'Digital Camera', 499.00),
        (10, 'Bluetooth Speaker', 59.99)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Product (product_id, product_name, price) VALUES (?, ?, ?)", product_data)

    
    sales_data = [
        (1, 2, '2024-07-05', 1799.98),
        (2, 3, '2024-07-08', 1947.00),
        (3, 5, '2024-07-10', 749.75),
        (4, 1, '2024-07-12', 299.00),
        (5, 2, '2024-07-15', 49.98),
        (6, 1, '2024-07-18', 119.99),
        (7, 3, '2024-07-20', 239.97),
        (8, 1, '2024-07-22', 249.99),
        (9, 1, '2024-07-25', 499.00),
        (10, 2, '2024-07-28', 119.98)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Sales (product_id, quantity_sold, sale_date, total_price) VALUES (?, ?, ?, ?)", sales_data)

    conn.commit()
    conn.close()

# """-----------------------------------------------------------------------------------------------------------------------------------------"""

def datainput():
    conn = sqlite3.connect('example.db')

    # Create a cursor object using the cursor() method
    cursor = conn.cursor()

    c1,c2,c3,c4=st.columns(4)
    product_id=c1.text_input(
            "Enter product_id here 👇"
        )
    quantity_sold=c2.number_input(
            "Enter quantity_sold here 👇"
        )
    sale_date=c3.date_input(
            "Enter sale_date here 👇",format="YYYY-MM-DD"
        )
    total_price=c4.number_input(
            "total_price here 👇"
        )
    a=(product_id,quantity_sold,sale_date,total_price)
    sales_data = []
    sales_data.append(a)

    # result data frame
    df_product=pd.DataFrame({"product_id":[] ,"product_name":[],"price":[]})
    df_Sales=pd.DataFrame({"sale_id":[] ,"product_id":[],"quantity_sold":[],"sale_date":[],"total_price":[]})
    for row in cursor.execute('SELECT * FROM Product'):
            new_row = pd.DataFrame({"product_id":[row[0]] ,"product_name":[row[1]],"price":[row[2]]})
            df_product = pd.concat([df_product, new_row])
            print(row)
    print(df_product)

    for row in cursor.execute('SELECT * FROM Sales'):
            new_row = pd.DataFrame({"sale_id":[row[0]] ,"product_id":[row[1]],"quantity_sold":[row[2]],"sale_date":[row[3]],"total_price":[row[4]]})
            df_Sales = pd.concat([df_Sales, new_row])
            print(row)
    print(df_Sales)
    if st.button("Add to Data Base"):
        cursor.executemany("INSERT OR IGNORE INTO Sales (product_id, quantity_sold, sale_date, total_price) VALUES (?, ?, ?, ?)", sales_data)
        
        
        conn.commit()
        conn.close()

    c1,c2=st.columns(2)
    c1.title("Your Product Table  :")
    c1.dataframe(df_product)
    
    c2.title("Your Sales Table  :")
    c2.dataframe(df_Sales)
























    # Save (commit) the changes
    # if st.sidebar.button("commit changes"):
    #     conn.commit()
    #     # Close the connection
    #     conn.close()