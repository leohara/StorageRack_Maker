import pandas as pd


class Param:
    def __init__(self):
        df = pd.read_csv('csv\parameters.csv')
        for index, value in df.iterrows():
            exec(f'self.{value[0]} = {value[1]}')
