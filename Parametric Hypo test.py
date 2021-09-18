import pandas as pd
import numpy as np
import math
from scipy.stats import ttest_ind
from scipy.stats import ttest_rel
from scipy.stats import f_oneway

def main(url = "adult.csv",  data1="age", data2="y", data3="hoursperweek"):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    df = pd.read_csv(url)
    df = df.select_dtypes(include=["float64", "int64"])
    print(df.info())
    
    data1 = str(input("Please Enter 1st Feature from Dataframe:"))
    data2 = str(input("Please Enter 2nd Feature from Dataframe:"))
    data3 = str(input("Please Enter 3rd Feature from Dataframe:"))
    print(" \n \n \n \n \n \n \n \n \n \n")

    print("-------------------------------------------------------------------------------")
    print("Student’s t-test \n \n \n")
    print("                           _____ASSUMPTIONS______                       \n")
    print("    1. Observations in each sample are independent and identically distributed")
    print("    2. Observations in each sample are normally distributed")
    print("    3. Observations in each sample have the same variance \n")
    t_test(url = url, data1=data1, data2=data2)
    print("-------------------------------------------------------------------------------")

    print("-------------------------------------------------------------------------------")
    print("Paired Student’s t-test \n \n \n")
    print("                           _____ASSUMPTIONS______                       \n")
    print("    1. Observations in each sample are independent and identically distributed")
    print("    2. Observations in each sample are normally distributed")
    print("    3. Observations in each sample have the same variance")
    print("    4. Observations across each sample are paired. \n")
    paired_t_test(url = url, data1=data1, data2=data2)
    print("-------------------------------------------------------------------------------")


    print("-------------------------------------------------------------------------------")
    print("Analysis of Variance Test (ANOVA) \n")
    print("                           _____ASSUMPTIONS______                       \n")
    print("    1. Observations in each sample are independent and identically distributed")
    print("    2. Observations in each sample are normally distributed")
    print("    3. Observations in each sample have the same variance \n")
    ANOVA(url = url, data1=data1, data2=data2, data3=data3)
    print("-------------------------------------------------------------------------------")


    
##    print("Chi-Squared Test \n")
##    print("_____ASSUMPTIONS______")
##    print("    1. Observations used in the calculation of the contingency table are independent")
##    print("    2. 25 or more examples in each cell of the contingency table \n")
##    CHI2(url = url, data1=data1, data2=data2)
    return



def t_test(url = "adult.csv", data1="age", data2="y"):
    df = pd.read_csv(url)
    df = df.select_dtypes(include=["float64", "int64"])

    stat, p = ttest_ind(df["{}".format(data1)],
                        df["{}".format(data2)],
                        permutations = 1000,
                        random_state = 42,
                        alternative = "two-sided",
                        trim = 0.0)
    print('stat=%.4f, p=%.4f' % (stat, p), "\n")
    if p > 0.05:
        print('H0: the means of the samples are equal. \n \n \n')
    else:
        print('H1: the means of the samples are unequal. \n \n \n')
    return

def paired_t_test(url = "adult.csv", data1="age", data2="y"):
    df = pd.read_csv(url)
    df = df.select_dtypes(include=["float64", "int64"])

    stat, p = ttest_rel(df["{}".format(data1)],
                        df["{}".format(data2)],
                        nan_policy="omit")
    print('stat=%.4f, p=%.4f' % (stat, p), "\n")
    if p > 0.05:
        print('H0: the means of the samples are equal (same distribution)\n \n \n')
    else:
        print('H1: the means of the samples are unequal (different distribution) \n \n \n')
    return

def ANOVA(url = "adult.csv", data1="age", data2="y", data3="hoursperweek"):
    df = pd.read_csv(url)
    df = df.select_dtypes(include=["float64", "int64"])

    stat, p = f_oneway(df["{}".format(data1)], df["{}".format(data2)], df["{}".format(data3)])
    print('stat=%.4f, p=%.4f' % (stat, p), "\n")
    if p > 0.05:
        print('H0: the means of the samples are equal (same distribution)\n \n \n')
    else:
        print('H1: One or More of the means of the samples are unequal (different distribution) \n \n \n')
    return


if __name__=="__main__":
    main()
