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
    This function wrangles data from a SQL database of Zillow properties, caches it locally, drops null
    values, renames columns, maps county to fips, converts certain columns to integers, and handles
    outliers.
    
    :param user: The username for accessing the MySQL database
    :param password: The password is unique per user saved in env
    :param host: The host parameter is the address of the server where the Zillow database is hosted
    :return: The function `wrangle_zillow` is returning a cleaned and wrangled pandas DataFrame
    containing information on single family residential properties in Los Angeles, Orange, and Ventura
    counties, including the year built, number of bedrooms and bathrooms, square footage, tax value,
    property tax, and county. The DataFrame has been cleaned by dropping null values, renaming columns,
    mapping county codes to county names, converting certain columns
    """
    # name of cached csv
    filename = 'zillow.csv'
    # if cached data exist
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    # wrangle from sql db if not cached
    else:
        # read sql query into df
        # 261 is single family residential id
        df = pd.read_sql('''select yearbuilt
                                    , bedroomcnt
                                    , bathroomcnt
                                    , calculatedfinishedsquarefeet
                                    , taxvaluedollarcnt
                                    , taxamount
                                    , fips 
                            from properties_2017
                            where propertylandusetypeid = 261'''
                            , f'mysql+pymysql://{user}:{password}@{host}/zillow')
        # cache data locally
        df.to_csv(filename, index=False)
    # nulls account for less than 1% so dropping
    df = df.dropna()
    # rename columns
    df = df.rename(columns=({'yearbuilt':'year'
                            ,'bedroomcnt':'beds'
                            ,'bathroomcnt':'baths'
                            ,'calculatedfinishedsquarefeet':'area'
                            ,'taxvaluedollarcnt':'tax_value'
                            ,'taxamount':'prop_tax'
                            ,'fips':'county'}))
    # map county to fips
    df.county = df.county.map({6037:'LA',6059:'Orange',6111:'Ventura'})
    # make int
    ints = ['year','beds','area','tax_value']
    for i in ints:
        df[i] = df[i].astype(int)
    # handle outliers
    df = df[df.area < 25000].copy()
    df = df[df.tax_value < df.tax_value.quantile(.95)].copy()
    return df