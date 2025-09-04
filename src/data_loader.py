import pandas as pd

class RecommederDataLoader:
    def __init__(self, original_csv:str, processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        # skip bad lines and drop null values
        df = pd.read_csv(self.original_csv, encoding='utf-8', on_bad_lines='skip').dropna()
        
        required_columns = {'Name', 'Genres', 'sypnopsis'}

        # perform a check to see if any of the required columns exists 
        # in the set of columns in the df
        missing = required_columns - set(df.columns)
        print(missing)
        
        if missing:
            raise ValueError("Missing column in csv file")
        
        # Create a new column called combined info shich combines Name, synopsis and genres into one new column
        df['combined_info'] = (
            "Title: " + df["Name"] + " Overview: " + df["sypnopsis"] + "Genres : " + df["Genres"]
        )

        #create a new csv
        df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8')

        return self.processed_csv