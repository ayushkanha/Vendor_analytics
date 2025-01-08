import pandas as pd
def fetch_stats(df):
    sales=df.shape[0]
    sales_amount=int(df["price"].sum())
    return sales,sales_amount