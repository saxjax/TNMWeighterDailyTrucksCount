import random

class Enhancer():

    def __init__(self, meta_data):
        self.meta_data = meta_data

    

    def enhance_data_frame(self,df_param):
        df = df_param.drop(columns=['max_axle_load', 'max_height','max_weight', 'max_length', 'recommended_speed', 'mean_speed'])

        # columns = list(df.columns.values)
        # print(columns)

        number_of_edges = df.shape[0]

        # Update the slope values
        for index, row in df.iterrows():
            value = self.meta_data['max_slope'] - self.meta_data['min_slope'] / number_of_edges
            df.loc[index, 'slope'] = int(round(value))

        # Change fuel station values to 0's or 1's
        for index, row in df.iterrows():
            value = None
            if (row['fuel_station'] == False):
                value = 0
            else:
                value = 1
            df.loc[index, 'fuel_station'] = value

        # Replace null values with average for daily_year
        for index, row in df.iterrows():
            value = None
            if (row['daily_year'] is None or row['daily_year'] == -1):
                value = (self.meta_data['max_daily_year'] - self.meta_data['min_daily_year'] / number_of_edges) * (random.random())
            else:
                value = row['daily_year']
            df.loc[index, 'daily_year'] = int(round(value))

        # Replace null values with average for daily_july
        for index, row in df.iterrows():
            value = None
            if (row['daily_july'] == None or row['daily_july'] == -1):
                value = (self.meta_data['max_daily_july'] - self.meta_data['min_daily_july'] / number_of_edges) * (random.random())
            else:
                value = row['daily_july']
            df.loc[index, 'daily_july'] = int(round(value))

        # Replace null values with average for daily_trucks
        for index, row in df.iterrows():
            value = None
            if (row['daily_trucks'] == None or row['daily_trucks'] == -1):
                value = (self.meta_data['max_daily_trucks'] - self.meta_data['min_daily_trucks'] / number_of_edges) * (random.random())
            else:
                value = row['daily_trucks']
            df.loc[index, 'daily_trucks'] = int(round(value))

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
                value = -1
            df.loc[index, 'type'] = value

        # Replace null values with average for type_max_speed
        value1 = (self.meta_data['max_daily_trucks'] - self.meta_data['min_daily_trucks'] / number_of_edges) 
        value2 = (self.meta_data['max_daily_july'] - self.meta_data['min_daily_july'] / number_of_edges)
        for index, row in df.iterrows():
            value = None
            if (row['daily_10_axle'] == None or row['daily_10_axle'] == -1):
                value =  (value1 + value2) * random.random()
            else:
                value = row['daily_10_axle']
            df.loc[index, 'daily_10_axle'] = int(round(value))

        # Set type_max_speed & set_max_speed
        for index, row in df.iterrows():
            value = None
            if (row['type'] == 0):
                value = 80
            elif (row['type'] ==  1):
                value = 60
            elif (row['type'] == 2):
                value = 110
            elif (row['type'] == 3):
                value = 120
            else:
                value = -1
            df.loc[index, 'type_max_speed'] = value
            df.loc[index, 'set_max_speed'] = value
            
        return df

    def remove_column(self,dataframe, columnname):
            df = Enhancer.enhance_data_frame(self,dataframe)
            df = df.drop(columns=[columnname])
            return df
    




