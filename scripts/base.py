import pandas as pd
import os

class Base:
    def __init__(self, filename="bus_routes.csv", data_folder="./data/output_tables"):
        self.filename = os.path.join(data_folder, filename)
        self.df = pd.read_csv(self.filename)
    
    def get_dataframe(self):
        return self.df
    
    def get_rows(self, start, end):
        return self.df.iloc[start:end]
    
    def get_columns(self, columns):
        return self.df[columns]
    
    def filter_by_column_value(self, column, value):
        return self.df[self.df[column] == value]
    
    def filter_by_list_in_column(self, df2, column, value):
        return df2[self.df2[column].isin([value])]
    
    def filter_by_value_in_column(self, column, value):
        return self.df[self.df[column].str.contains(value, case=False)]