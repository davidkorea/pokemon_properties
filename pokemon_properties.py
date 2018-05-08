import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pd_utils import utils

DATA_FILE = './data_pd/pokemon.csv'

def collect_data():
    cols = ['Name', 'Type_1', 'Total', 'HP', 'Attack', 'Defense', 'Speed', 'Height_m', 'Weight_kg', 'Catch_Rate']
    data_df = pd.read_csv(DATA_FILE,usecols=cols)
    return data_df

def ananlyse_by_type(data_df,var1):
    sns.boxplot(x='Type_1',y=var1,data=data_df)
    plt.title('Type vs {} box plot'.format(var1))
    plt.tight_layout()
    plt.savefig('./Type_{}_box.png'.format(var1))
    plt.show()


def analyse_dual_vars(data_df,var1,var2):
    sns.jointplot(x=var1,y=var2,data=data_df)
    plt.title('{} vs {}'.format(var1,var2))
    plt.tight_layout()
    plt.savefig('./{}_{}_jointplot.png'.format(var1,var2))
    plt.show()

def ananlyse_vars_relationship(data_df):
    corr_df = data_df.corr()
    sns.heatmap(corr_df,annot=True,cmap='rainbow',fmt='.2f',vmin=-1,vmax=1)
    plt.title('vars relationship heatmap')
    plt.tight_layout()
    plt.savefig('./Vars_relationship_heatmap.png')
    plt.show()

def main():
    data_df = collect_data()
    # utils(data_df)
    ananlyse_by_type(data_df, 'HP')
    analyse_dual_vars(data_df,'HP','Attack')
    ananlyse_vars_relationship(data_df)

main()