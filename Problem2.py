import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby('customer_number').count().reset_index().sort_values(by = ['order_number'], ascending = [False])
    return df.head(1)[['customer_number']]