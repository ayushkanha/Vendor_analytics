import matplotlib.pyplot as plt
import pandas as pd

def fetch_sales_data(conn):
    
    cursor = conn.cursor()
    cursor.execute("SELECT sale_date, product_id, quantity_sold, total_price FROM Sales")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=['sale_date', 'product_id', 'quantity_sold', 'total_price'])
    print(df)
    df['sale_date'] = pd.to_datetime(df['sale_date'], format='%Y-%m-%d')

    cursor.execute("SELECT product_id,product_name FROM Product")
    rows = cursor.fetchall()
    df1 = pd.DataFrame(rows, columns=['product_id','product_name'])
    print(df1)
    return df,df1
# """-----------------------------------------------------------------------------------------------------------------------------------------"""
def analyze_sales(df,df1):
    

    # Track sales trends
    df['date'] = df['sale_date'].dt.date
    daily_sales = df.groupby('date')['total_price'].sum()
    weekly_sales = df.resample('W', on='sale_date')['total_price'].sum()
    monthly_sales = df.resample('M', on='sale_date')['total_price'].sum()
    print("daily", daily_sales)
    print("weekly",weekly_sales)
    # Identify best-selling products
    best_selling = df.groupby('product_id')['quantity_sold'].sum()
    merged_df = pd.merge(best_selling, df1, on='product_id', how='inner')

# Remove the 'product_id' column
    merged_df = merged_df.drop(columns='product_id')

    # Display the final DataFrame
    print(merged_df)
    print(best_selling)
    # Calculate total revenue
    total_revenue = df['total_price'].sum()

    return daily_sales, weekly_sales, monthly_sales, merged_df, total_revenue
