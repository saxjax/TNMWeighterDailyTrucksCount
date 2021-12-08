import random
import pandas as pd

class TrainingRealDataEnhancer():

    def __init__(self, meta_data):
        self.meta_data = meta_data

    def  enhance_data_frame(self,df_param):
        df = df_param.drop(columns=['max_axle_load', 'max_height','max_weight', 'max_length', 'recommended_speed', 'mean_speed'])

        # Drop rows with null values
        for index, row in df.iterrows():
            if (pd.isnull(row['daily_year']) or pd.isnull(row['daily_july']) or pd.isnull(row['daily_trucks']) or pd.isnull(row['type'])
            or pd.isnull(row['daily_10_axle'] or pd.isnull(row['type_max_speed']) or pd.isnull(row['type_max_speed']) or pd.isnull(row['set_max_speed']) or pd.isnull(row['slope']))):
                df.drop(index, inplace=True)

        # Update the slope values
        for index, row in df.iterrows():
            value = None
            if pd.isnull(row['slope']):
                df.loc[index, 'slope'] = 0
            else:
                value = float(row['slope'])
                df.loc[index, 'slope'] = int(round(value))

        # Change fuel station values to 0's or 1's
        for index, row in df.iterrows():
            value = None
            if (row['fuel_station'] == False):
                value = 0
            else:
                value = 1
            df.loc[index, 'fuel_station'] = value

        # Replace road types with numerical values
        for index, row in df.iterrows():
            value = None
            if (str(row['type']).__contains__('Lokalvej, tertiær by')):
                value = 0
            elif (str(row['type']).__contains__('Lokalsti, By')):
                value = 1
            elif (str(row['type']).__contains__('Lokalvej, tertiær land')):
                value = 2
            elif (str(row['type']).__contains__('Hovedsti, By')):
                value = 3
            else:
                value = 0
            df.loc[index, 'type'] = value
        
        # Round daily_year
        for index, row in df.iterrows():
            value = None
            value = row['daily_year']
            df.loc[index, 'daily_year'] = int(round(value))

        # Round daily_july
        for index, row in df.iterrows():
            value = None
            value = row['daily_july']
            df.loc[index, 'daily_july'] = int(round(value))

        # Round daily_trucks
        for index, row in df.iterrows():
            value = None
            value = row['daily_trucks']
            df.loc[index, 'daily_trucks'] = int(round(value))
        
        # Round daily_10_axle
        for index, row in df.iterrows():
            value = None
            value = row['daily_10_axle']
            df.loc[index, 'daily_10_axle'] = int(round(value))

        return df

    def remove_column(self,dataframe, columnname):
            df = TrainingRealDataEnhancer.enhance_data_frame(self,dataframe)
            df = df.drop(columns=[columnname])
            return df
    




