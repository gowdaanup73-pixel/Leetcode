import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(
        orders,
        left_on = 'id',
        right_on = 'customerId',
        how = 'left'
    )
    res = df[df['customerId'].isna()][['name']]
    res.columns = ['Customers']
    return res