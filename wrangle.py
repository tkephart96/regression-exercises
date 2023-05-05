'''Wrangle Zillow Data'''

### IMPORTS ###

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from env import user,password,host

### ACQUIRE DATA ###

def get_zillow(user=user,password=password,host=host):
    """
    This function retrieves data from a MySQL database containing information about single family
    residential properties and saves it to a CSV file or returns it as a pandas dataframe.
    
    :param user: The username for the MySQL database connection
    :param password: The password is unique per person pulled from personal env
    :param host: The host parameter is the address of the server where the MySQL database is hosted
    :return: a pandas DataFrame containing information about single family residential properties in
    2017 from the Zillow database. If the data has already been saved to a CSV file, the function reads
    the data from the file. Otherwise, it reads the data from the database, saves it to a CSV file, and
    returns the DataFrame.
    """
    # name of cached csv
    filename = 'zillow2017.csv'
    # wrangle from cached data
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    # wrangle from sql db if not cached
    else:
        # read sql query into df
        # 261 is single family residential id
        df = pd.read_sql('''select bedroomcnt
                                    , bathroomcnt
                                    , calculatedfinishedsquarefeet
                                    , taxvaluedollarcnt
                                    , yearbuilt
                                    , taxamount
                                    , fips 
                                    , propertylandusetypeid
                                    , propertylandusedesc
                            from properties_2017
                            join propertylandusetype using(propertylandusetypeid)
                            where propertylandusetypeid = 261'''
                            , f'mysql+pymysql://{user}:{password}@{host}/zillow')
        # cache data locally
        df.to_csv(filename, index=False)
        return df

def wrangle_zillow():
    """
    The function drops null values from a Zillow dataset and returns the cleaned dataframe.
    :return: The function `wrangle_zillow()` is returning a cleaned and preprocessed dataframe obtained
    from the `get_zillow()` function. The null values in the dataframe have been dropped as they account
    for less than 1% of the data.
    """
    df = get_zillow()
    # drop unneeded columns
    df = df.drop(columns=['propertylandusetypeid','propertylandusedesc'])
    # nulls account for less than 1% so dropping
    df = df.dropna()
    return df