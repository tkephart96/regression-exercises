'''Wrangle Zillow Data'''

### IMPORTS ###

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from env import user,password,host

### ACQUIRE DATA ###

def wrangle_zillow(user=user,password=password,host=host):
    """
    This function wrangles data from a cached CSV or SQL database, drops unneeded columns and null
    values, and returns a cleaned dataframe of Zillow property data.
    
    :param user: The username for accessing the MySQL database
    :param password: Please make sure to keep your password secure and not share it with anyone
    :param host: The host parameter is the address of the server where the MySQL database is hosted
    :return: a pandas DataFrame containing cleaned and wrangled data from the Zillow database for single
    family residential properties. The DataFrame includes columns for bedroom count, bathroom count,
    calculated finished square footage, tax value in dollars, year built, tax amount, and FIPS code. The
    function drops unneeded columns and null values before returning the DataFrame.
    """
    # name of cached csv
    filename = 'zillow2017.csv'
    # wrangle from cached data
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
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
    # drop unneeded columns
    df = df.drop(columns=['propertylandusetypeid','propertylandusedesc'])
    # nulls account for less than 1% so dropping
    df = df.dropna()
    return df