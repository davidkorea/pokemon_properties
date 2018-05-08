import pandas as pd
import matplotlib.pyplot as plt
from pd_utils import utils

DATA_FILE = './'

def collect_data():
    data_df = pd.read_csv(DATA_FILE)
    return data_df



def main():
    data_df = collect_data()

main()