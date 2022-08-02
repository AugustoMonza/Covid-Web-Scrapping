import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def table():
    covid = pd.read_csv('datos Covid.csv')
    covid_norm = covid.loc[:,['continent', 'location', 'new_cases', 'new_deaths', 'total_cases_per_million', 'total_deaths_per_million', 'reproduction_rate']]
    agrupado = covid_norm.groupby(['continent']).agg({'new_cases': 'sum', 'new_deaths': 'sum'})
    agrupado.plot(kind='bar')
    plt.show()

if __name__ == '__main__':
    table()
