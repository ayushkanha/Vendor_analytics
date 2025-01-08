import streamlit as st
from streamlit_lottie import st_lottie
import json
import sqlite3
import pandas as pd
import dataprocessing as dp
import matplotlib.pyplot as plt
import seaborn as sns
# Connect to an SQLite database (or create it if it doesn't exist)
df=pd.DataFrame({"id":[1] ,"name":["none"],"price":[1]})
def analytics():
    df=pd.DataFrame({"id":[1] ,"name":["none"],"price":[1]})
    conn = sqlite3.connect('example.db')

    # Create a cursor object using the cursor() method
    cursor = conn.cursor()
 

    # result data frame
    
    if st.button("show analytics"):
        for row in cursor.execute('SELECT * FROM data'):
                new_row = pd.DataFrame({"id":[row[0]] ,"name":[row[1]],"price":[row[2]]})
                df = pd.concat([df, new_row])
                print(row)
        print(df)
        df=df[1:]
        st.title("Your Data-Base :")
        st.dataframe(df)

        """------------------------------------------------------------------------------------"""
        sales,sales_amount = dp.fetch_stats(df)
        col1,col2=st.columns(2)
        with col1:
            st.header("Total Number of Sales : ")
            st.title(sales)
        with col2:
            st.header("Total Sales Amount : ")
            st.title(sales_amount)
        
        st.title("Chart Comarasion : ")
        st.bar_chart(df.iloc[:, 1:])

        st.title("Chat for Sales of medicines : ")
        fig, ax = plt.subplots()
        ax.hist(df["name"], bins=20)
        st.pyplot(fig)


        st.title("Chat for ratio of sales amount of every medicine : ")
        # Grouping data by 'name' and summing up prices
        grouped_data = df.groupby('name')['price'].sum()
        print(grouped_data)
        fig, ax = plt.subplots()
        

        grouped_data.plot(kind='pie', autopct='%0.0f%%', startangle=90, colors=plt.cm.Paired.colors)
        st.pyplot(fig)
        st.title("Price Distribution by Medicine: ")
        fig, ax = plt.subplots()
        sns.boxplot(x='name', y='price', data=df)
        plt.title('Price Distribution by Medicine')
        plt.xlabel('Medicine Name')
        plt.ylabel('Price')
        st.pyplot(fig)




    # Save (commit) the changes
    if st.sidebar.button("commit changes"):
        conn.commit()
        # Close the connection
        conn.close()
        


