import pandas as pd
import numpy as np
import math
from scipy.stats import mannwhitneyu
from scipy.stats import wilcoxon
from scipy.stats import kruskal
from scipy.stats import friedmanchisquare

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def main(url = "adult.csv"):
    df = pd.read_csv(url)
    df = df.select_dtypes(include=["float64", "int64"])
    print(df.info())
    
    data1 = str(input("Please Enter 1st Feature from Dataframe:"))
    data2 = str(input("Please Enter 2nd Feature from Dataframe:"))
    data3 = str(input("Please Enter 3rd Feature from Dataframe:"))
    print(" \n \n \n \n \n \n \n \n \n \n")

    print("-------------------------------------------------------------------------------")
    print("Mann-Whitney U Test \n \n \n")
    print("                           _____ASSUMPTIONS______                       \n")
    print("    1. Observations in each sample are independent and identically distributed")
    print("    2. Observations in each sample can be Ranked \n")
    Mann_Whitney(url = url, data1=data1, data2=data2)
    print("-------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------")
    print("Wilcoxon Signed-Rank Test \n \n \n")
    print("                           _____ASSUMPTIONS______                       \n")
    print("    1. Observations in each sample are independent and identically distributed")
    print("    2. Observations in each sample can be Ranked")
    print("    3. Observations across each sample are paired. \n")
    Wilcox(url = url, data1=data1, data2=data2)
    print("-------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------")
    print("Kruskal-Wallis H Test \n")
    print("                           _____ASSUMPTIONS______                       \n")
    print("    1. Observations in each sample are independent and identically distributed")
    print("    2. Observations in each sample can be Ranked \n")
    Kruskal_Wallis(url = url, data1=data1, data2=data2)
    print("-------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------")
    print("Friedman Test \n")
    print("                           _____ASSUMPTIONS______                       \n")
    print("    1. Observations in each sample are independent and identically distributed")
    print("    2. Observations in each sample can be Ranked")
    print("    3. Observations across each sample are paired. \n")
    Friedman(url = url, data1=data1, data2=data2, data3=data3)
    return



def Mann_Whitney(url = "adult.csv", data1="age", data2="y"):
    df = pd.read_csv(url)
    df = df.select_dtypes(include=["float64", "int64"])

    stat, p = mannwhitneyu(df["{}".format(data1)],
                           df["{}".format(data2)],
                           method="auto")
    print('stat=%.4f, p=%.4f' % (stat, p), "\n")
    if p > 0.05:
        print('H0: the distributions of both samples are equal. \n \n \n')
    else:
        print('H1: the distributions of both samples are not equal. \n \n \n')
    return

def Wilcox(url = "adult.csv", data1="age", data2="y"):
    df = pd.read_csv(url)
    df = df.select_dtypes(include=["float64", "int64"])

    stat, p = wilcoxon(df["{}".format(data1)],
                       df["{}".format(data2)],
                       zero_method="pratt",
                       correction=True,
                       mode="auto")
    print('stat=%.4f, p=%.4f' % (stat, p), "\n")
    if p > 0.05:
        print('H0: the distributions of both samples are equal. \n \n \n')
    else:
        print('H1: the distributions of both samples are not equal. \n \n \n')
    return

def Kruskal_Wallis(url = "adult.csv", data1="age", data2="y", data3="hoursperweek"):
    df = pd.read_csv(url)
    df = df.select_dtypes(include=["float64", "int64"])

    stat, p = kruskal(df["{}".format(data1)],
                      df["{}".format(data2)],
                      nan_policy="omit")
    print('stat=%.4f, p=%.4f' % (stat, p), "\n")
    if p > 0.05:
        print('H0: the distributions of both samples are equal. \n \n \n')
    else:
        print('H1: the distributions of one or more samples are not equal. \n \n \n')
    return

def Friedman(url = "adult.csv", data1="age", data2="y", data3="hoursperweek"):
    df = pd.read_csv(url)
    df = df.select_dtypes(include=["float64", "int64"])

    stat, p = kruskal(df["{}".format(data1)],
                      df["{}".format(data2)],
                      df["{}".format(data3)],
                      nan_policy="omit")
    print('stat=%.4f, p=%.4f' % (stat, p), "\n")
    if p > 0.05:
        print('H0: the distributions of both samples are equal. \n \n \n')
    else:
        print('H1: the distributions of one or more samples are not equal. \n \n \n')
    return


if __name__=="__main__":
    main()
