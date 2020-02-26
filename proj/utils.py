import pandas as pd

def load_data(path='IPIP-FFM-data-8Nov2018/data-final.csv'):
    data = pd.read_csv('IPIP-FFM-data-8Nov2018/data-final.csv',delimiter='\t')
    data = data.dropna()
    return data