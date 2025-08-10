import pandas as pd

# def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
#     return activity.groupby('player_id')['event_date'].agg('min').reset_index().rename(columns = {'event_date': 'first_login'})

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.apply(lambda x: x*2 if x.name = 'device_id' else x)
    print(df)
    return activity