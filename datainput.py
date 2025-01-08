import streamlit as st
from streamlit_lottie import st_lottie
import json
import sqlite3
import pandas as pd
# Connect to an SQLite database (or create it if it doesn't exist)
def datainput():
    conn = sqlite3.connect('example.db')

    # Create a cursor object using the cursor() method
    cursor = conn.cursor()

    # Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS data
                (id integer primary key AUTOINCREMENT, name text, price real)''')


    name=st.text_input(
            "Enter Name here 👇"
        )
    price=st.number_input(
            "Enter price of options here 👇"
        )
    a=(name,price)
    data_person_name = []
    data_person_name.append(a)

    # result data frame
    df=pd.DataFrame({"id":[1] ,"name":["none"],"price":[1]})
    if st.button("Add to Data Base"):
        cursor.executemany('INSERT INTO data(name, price) VALUES (?,?)', data_person_name)
        for row in cursor.execute('SELECT * FROM data'):
                new_row = pd.DataFrame({"id":[row[0]] ,"name":[row[1]],"price":[row[2]]})
                df = pd.concat([df, new_row])
                print(row)
        print(df)
        conn.commit()
        # Close the connection
        conn.close()
    st.title("Your Data-Base :")
    st.dataframe(df)
    # Save (commit) the changes
    # if st.sidebar.button("commit changes"):
    #     conn.commit()
    #     # Close the connection
    #     conn.close()