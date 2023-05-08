'''Wrangle Zillow Data'''

### IMPORTS ###

import numpy as np
import pandas as pd
import sklearn.preprocessing

### SCALERS ###

def robs_zillow(train,validate,test):
    """
    The function applies the RobustScaler method to scale the numerical features of the train, validate,
    and test datasets.
    
    :param train: a pandas DataFrame containing the training data
    :param validate: The validation dataset, which is used to evaluate the performance of the model
    during training and to tune hyperparameters
    :param test: The "test" parameter is a dataset that is used to evaluate the performance of a machine
    learning model that has been trained on the "train" dataset and validated on the "validate" dataset.
    The "test" dataset is typically used to simulate real-world scenarios and to ensure that the model
    is able
    :return: three dataframes: Xtr (scaled training data), Xv (scaled validation data), and Xt (scaled
    test data).
    """
    rob_scale = sklearn.preprocessing.RobustScaler()
    Xtr,Xv,Xt = train,validate,test
    scale = train.columns[:-1].to_list()
    Xtr[scale] = rob_scale.fit_transform(Xtr[scale])
    Xv[scale] = rob_scale.transform(Xv[scale])
    Xt[scale] = rob_scale.transform(Xt[scale])
    return Xtr, Xv, Xt


def qtf_zillow(train,validate,test,out_dist='normal'):
    """
    The function qtf_zillow applies quantile transformation to the numerical features of the input
    dataframes train, validate, and test.
    
    :param train: This is the training dataset that will be used to fit the quantile transformer and
    transform the data
    :param validate: The validation dataset used for scaling the data
    :param test: The test parameter is a pandas DataFrame containing the test data
    :param out_dist: The `out_dist` parameter is used to specify the output distribution of the quantile
    transformer. It can take two values: "normal" or "uniform". If "normal" is specified, the
    transformed data will have a normal distribution. If "uniform" is specified, the transformed data
    will have, defaults to normal (optional)
    :return: three dataframes: Xtr (transformed training data), Xv (transformed validation data), and Xt
    (transformed test data).
    """
    qt = sklearn.preprocessing.QuantileTransformer(output_distribution=out_dist)
    Xtr,Xv,Xt = train,validate,test
    scale = train.columns[:-1].to_list()
    Xtr[scale] = qt.fit_transform(Xtr[scale])
    Xv[scale] = qt.transform(Xv[scale])
    Xt[scale] = qt.transform(Xt[scale])
    return Xtr, Xv, Xt