import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pd_utils import utils

DATA_FILE = './house_data.csv'

def collect_data():
    data_df = pd.read_csv(DATA_FILE)
    data_df.dropna() # no NA in csv
    return data_df

def box_plot(data_df, x, y):
    sns.boxplot(x=x, y=y, data=data_df)
    plt.show()

def joint_plot(data_df,var1,var2):
    sns.jointplot(x=var1,y=var2,data=data_df)
    plt.show()

def heatmap_plot(data_df):
    corr = data_df.corr()
    sns.heatmap(corr,annot=True)
    plt.show()

def main():
    data_df = collect_data()
    utils(data_df)
    box_plot(data_df,'bedrooms','price')
    joint_plot(data_df,'bathrooms','price')
    heatmap_plot(data_df)

main()