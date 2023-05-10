'''Evaluate Linear Regression Models'''

### IMPORTS ###

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression
from sklearn.metrics import mean_squared_error, explained_variance_score, r2_score

from scipy import stats

### FUNCTIONS ###

def plot_res(df,x,y,yhat):
    '''creates a residual plot'''
    # residuals
    df = df.assign(res = (df[yhat] - df[y]))
    # plot
    sns.scatterplot(data=df,x=x,y=df['res'])
    plt.show()

def reg_err(df,y,yhat,result=None):
    '''returns values:
    - SSE
    - ESS
    - TSS
    - MSE
    - RMSE
    
    result:
        if var then returns variables in same order as above,
        if df then returns a dataframe,
        else prints out values'''
    # metrics
    MSE = mean_squared_error(df[y],df[yhat])
    SSE = MSE*len(df)
    RMSE = MSE**.5
    ESS = sum((df[yhat] - df[y].mean())**2)
    TSS = ESS + SSE
    # for variable outputs
    if result == 'var':
        return SSE,ESS,TSS,MSE,RMSE
    # for df outputs
    elif result == 'df':
        return pd.DataFrame({
            'SSE':[SSE],
            'ESS':[ESS],
            'TSS':[TSS],
            'MSE':[MSE],
            'RMSE':[RMSE]
        })
    # just print it out
    else:
        print("SSE = ", SSE)
        print("ESS = ", ESS)
        print("TSS = ", TSS)
        print("MSE = ", MSE)
        print("RMSE = ", RMSE)

def bl_mean_err(df,y,yhat_bl,result=None):
    '''computes SSE, MSE, and RMSE for baseline'''
    # metrics
    MSE_bl = mean_squared_error(df[y],df[yhat_bl])
    SSE_bl = MSE_bl*len(df)
    RMSE_bl = MSE_bl**.5
    # for variable outputs
    if result == 'var':
        return SSE_bl,MSE_bl,RMSE_bl
    # for df outputs
    elif result == 'df':
        return pd.DataFrame({
            'SSE_bl':[SSE_bl],
            'MSE_bl':[MSE_bl],
            'RMSE_bl':[RMSE_bl]
        })
    # just print it out
    else:
        print("SSE_bl = ", SSE_bl)
        print("MSE_bl = ", MSE_bl)
        print("RMSE_bl = ", RMSE_bl)

def better_than_bl(df,y,yhat,yhat_bl,metric=None):
    '''returns true if model better than bl based on metric
    chosen or all 3, otherwise false'''
    # acquire metrics for comparison
    SSE,ESS,TSS,MSE,RMSE = reg_err(df,y,yhat,'var')
    SSE_bl,MSE_bl,RMSE_bl = bl_mean_err(df,y,yhat_bl,'var')
    # choose metric output
    if metric == 'SSE':
        print('Model SSE better: ',SSE - SSE_bl < 0)
    elif metric == 'MSE':
        print('Model MSE better: ',MSE - MSE_bl < 0)
    elif metric == 'RMSE':
        print('Model RMSE better: ',RMSE - RMSE_bl < 0)
    else:
        print('Model SSE better: ',SSE - SSE_bl < 0)
        print('Model MSE better: ',MSE - MSE_bl < 0)
        print('Model RMSE better: ',RMSE - RMSE_bl < 0)
