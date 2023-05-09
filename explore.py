'''Explore Zillow Data

Functions:
- '''

### IMPORTS ###

import matplotlib.pyplot as plt
import seaborn as sns

### FUNCTIONS ###

def plot_var_pairs(df,target):
    for i in df.drop(columns=target).columns[:-1]:
        sns.lmplot(x=i,y=target,data=df,line_kws={'color':'orange'})
        plt.ylim(0,1_250_000)
        plt.show()

def plot_cat_n_cont_vars(df,cat,cont):
    plt.figure(figsize=(16,6))
    plt.subplot(1,3,1)
    sns.boxenplot(x=cat, y=cont, data=df)
    plt.subplot(1,3,2)
    sns.boxplot(x=cat, y=cont, data=df)
    plt.subplot(1,3,3)
    sns.violinplot(x=cat, y=cont, data=df)
    plt.show()


