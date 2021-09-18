import pandas as pd
import numpy as np
import math
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss

def main(csv = "adult.csv"):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    print("Augmented Dickey-Fuller Unit Root Test")
    print("                       _____ASSUMPTIONS______                            ")
    print("    1. Observations in are temporally ordered"         )
    print(" \n \n \n")
    Ad_fuller(url = csv)
    print("Kwiatkowski-Phillips-Schmidt-Shin")
    print("_____ASSUMPTIONS______")
    print("    1. Observations in are temporally ordered \n \n \n")
    KPSS(url = csv)


def Ad_fuller(url = "adult.csv"):
    df = pd.read_csv(url)

    df = df.select_dtypes(include=["float64", "int64", "float32", "int32"])
    

    for (columnName, columnData) in df.iteritems():
        print("---------------------------------------------------------------------------")
        print('Column Name : ', columnName, " \n \n")
        data = columnData.values
        stat, p, lags, obs, crit, t = adfuller(data,
                                               regression="c",
                                               autolag="AIC")
        print('stat=%.4f, p=%.4f' % (stat, p), " \n")
        if p > 0.05:
            print('H0: a unit root is present (series is Probably non-stationary) \n \n')
        else:
            print('H1: a unit root is not present (series is Probably Stationary) \n \n')
    return

def KPSS(url = "adult.csv"):
    df = pd.read_csv(url)

    df = df.select_dtypes(include=["float64", "int64", "float32", "int32"])
    

    for (columnName, columnData) in df.iteritems():
        print("---------------------------------------------------------------------------")
        print('Column Name : ', columnName, " \n \n")
        data = columnData.values
        stat, p, nlags, crit = kpss(data,
                                    nlags="auto",
                                    regression="ct")
        print('stat=%.4f, p=%.4f' % (stat, p), " \n")
        if p >= 0.05:
            print('H0: the time series is not trend-stationary \n \n')
        else:
            print('H1: the time series is trend-stationary) \n \n')
    return

if __name__ == "__main__":
    main()
