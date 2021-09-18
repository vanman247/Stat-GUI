import pandas as pd
import numpy as np
import math
import scipy as spy
from scipy.stats import shapiro
from scipy.stats import normaltest
from scipy.stats import anderson

def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    print()
    Shapiro(url = "adult.csv")
    print()
    K2_test(url = "adult.csv")
    print()
    anderson_darling_test(url = "adult.csv")

def Shapiro(url = "adult.csv"):
    df = pd.read_csv(url)

    df = df.select_dtypes(include=["float64", "int64"])

    for (columnName, columnData) in df.iteritems():
        print('Column Name : ', columnName)
        data = columnData.values
        stat, p = shapiro(data)
        print('stat=%.4f, p=%.4f' % (stat, p))
        if p > 0.05:
            print('Probably Gaussian \n')
        else:
            print('Probably not Gaussian \n')

##Shapiro()

def K2_test(url = "adult.csv"):
    df = pd.read_csv(url)

    df = df.select_dtypes(include=["float64", "int64"])

    for (columnName, columnData) in df.iteritems():
        print('Column Name : ', columnName)
        data = columnData.values
        stat, p = normaltest(data, nan_policy="omit")
        print('stat=%.4f, p=%.4f' % (stat, p))
        if p > 0.05:
            print('Probably Gaussian \n')
        else:
            print('Probably not Gaussian \n')

##K2_test()

def anderson_darling_test(url = "adult.csv"):
    df = pd.read_csv(url)

    df = df.select_dtypes(include=["float64", "int64"])

    for (columnName, columnData) in df.iteritems():
        print('Column Name : ', columnName)
        data = columnData.values
        result = anderson(data, dist="norm") #dist={‘norm’, ‘expon’, ‘logistic’, ‘gumbel’,‘gumbel_r’}
        print('stat=%.3f' % (result.statistic))
        for i in range(len(result.critical_values)):
            sl, cv = result.significance_level[i], result.critical_values[i]
            if result.statistic < cv:
                print('Probably Gaussian at the %.1f%% level' % (sl), "\n")
            else:
                print('Probably not Gaussian at the %.1f%% level' % (sl), "\n")

                
##anderson_darling_test()

if __name__ == "__main__":
    main()
