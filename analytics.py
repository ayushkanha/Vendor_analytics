import streamlit as st
import sqlite3
import seaborn as sns
from visuals import fetch_sales_data
from visuals import analyze_sales

def analytics():

    conn = sqlite3.connect('example.db')
    if st.button("show analytics"):
        sales_df,df = fetch_sales_data(conn)

        # Analyze sales data
        daily_sales, weekly_sales, monthly_sales, best_selling, total_revenue = analyze_sales(sales_df,df)

        # Display total revenue
        st.title(f"**Total Revenue:** :blue[₹{total_revenue:.2f}]")

        # Display best-selling products
        st.title("**Best-Selling :blue[Products]:**")
        st.bar_chart(best_selling, x="product_name", y="quantity_sold")

        # Display sales trends
        st.title("**Sales :blue[Trends]:**")
        st.subheader("Daly Sales :blue[Trends]", divider=True)
        st.line_chart(daily_sales)
        st.subheader("Weekly Sales :blue[Trends]", divider=True)
        st.line_chart(weekly_sales)
        st.subheader("Monthly Sales :blue[Trends]", divider=True)
        st.line_chart(monthly_sales)
        plot = sns.pairplot(df)
 
        # Display the plot in Streamlit
        st.title("**Revenue Contribution by :blue[Product]**")
        fig, ax = plt.subplots()
        ax.pie(product_revenue["total_price"], labels=product_revenue["product_name"], autopct="%1.1f%%")
        st.pyplot(fig)
        conn.close()












































        # for row in cursor.execute('SELECT * FROM data'):
        #         new_row = pd.DataFrame({"id":[row[0]] ,"name":[row[1]],"price":[row[2]]})
        #         df = pd.concat([df, new_row])
        #         print(row)
        # print(df)
        # df=df[1:]
        # st.title("Your Data-Base :")
        # st.dataframe(df)

        # """------------------------------------------------------------------------------------"""
        # sales,sales_amount = dp.fetch_stats(df)
        # col1,col2=st.columns(2)
        # with col1:
        #     st.header("Total Number of Sales : ")
        #     st.title(sales)
        # with col2:
        #     st.header("Total Sales Amount : ")
        #     st.title(sales_amount)
        
        # st.title("Chart Comarasion : ")
        # st.bar_chart(df.iloc[:, 1:])

        # st.title("Chat for Sales of medicines : ")
        # fig, ax = plt.subplots()
        # ax.hist(df["name"], bins=20)
        # st.pyplot(fig)


        # st.title("Chat for ratio of sales amount of every medicine : ")
        # # Grouping data by 'name' and summing up prices
        # grouped_data = df.groupby('name')['price'].sum()
        # print(grouped_data)
        # fig, ax = plt.subplots()
        

        # grouped_data.plot(kind='pie', autopct='%0.0f%%', startangle=90, colors=plt.cm.Paired.colors)
        # st.pyplot(fig)

        # fig, ax = plt.subplots()
        # sns.boxplot(x='name', y='price', data=df)
        # plt.title('Price Distribution by Medicine')
        # st.pyplot(fig)




    # Save (commit) the changes
    if st.sidebar.button("commit changes"):
        conn.commit()
        # Close the connection
        conn.close()
        


