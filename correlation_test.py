import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import kendalltau
from scipy.stats import chi2_contingency


def main(url = "adult.csv",  data1="age", data2="y"):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    df = pd.read_csv(url)
    df = df.select_dtypes(include=["float64", "int64"])
    print(df.info())
    
    data1 = str(input("Please Enter 1st Feature from Dataframe:"))
    data2 = str(input("Please Enter 2nd Feature from Dataframe:"))
    print(" \n \n \n \n \n \n \n \n \n \n")

    try:
        print("Pearson’s Correlation Coefficient \n \n \n")
        print("_____ASSUMPTIONS______")
        print("    1. Observations in each sample are independent and identically distributed")
        print("    2. Observations in each sample are normally distributed")
        print("    3. Observations in each sample have the same variance \n")
        pearson(url = url, data1=data1, data2=data2)
    except:
        print("Passed")

    try:
        print("Spearman’s Rank Correlation \n \n \n")
        print("_____ASSUMPTIONS______")
        print("    1. Observations in each sample are independent and identically distributed")
        print("    2. Observations in each sample can be ranked \n")
        spearman(url = url, data1=data1, data2=data2)
    except:
        print("Passed")


    try:
        print("Kendall’s Rank Correlation \n")
        print("_____ASSUMPTIONS______")
        print("    1. Observations in each sample are independent and identically distributed")
        print("    2. Observations in each sample can be ranked \n")
        Kendalltau(url = url, data1=data1, data2=data2)
    except:
        print("Passed")


    try:
        print("Chi-Squared Test \n")
        print("_____ASSUMPTIONS______")
        print("    1. Observations used in the calculation of the contingency table are independent")
        print("    2. 25 or more examples in each cell of the contingency table \n")
        CHI2(url = url, data1=data1, data2=data2)
    except:
        print("Passed")

    return



def pearson(url = "adult.csv", data1="age", data2="y"):
    df = pd.read_csv(url)
    df = df.select_dtypes(include=["float64", "int64"])

    stat, p = pearsonr(df["{}".format(data1)], df["{}".format(data2)])
    print('stat=%.4f, p=%.4f' % (stat, p), "\n")
    if p > 0.05:
        print('H0: the two samples are probably independent. \n \n \n')
    else:
        print('H1: there is probably a dependency between the samples \n \n \n')

def spearman(url = "adult.csv", data1="age", data2="y"):
    df = pd.read_csv(url)
    df = df.select_dtypes(include=["float64", "int64"])
    
    stat, p = spearmanr(df["{}".format(data1)], df["{}".format(data2)], nan_policy="omit", alternative="two-sided") #alternative = {‘two-sided’, ‘less’, ‘greater’}
    print('stat=%.4f, p=%.4f' % (stat, p), "\n")
    if p > 0.05:
        print('H0: the two samples are probably independent. \n \n \n')
    else:
        print('H1: there is probably a dependency between the samples \n \n \n')

def Kendalltau(url = "adult.csv", data1="age", data2="y"):
    df = pd.read_csv(url)
    df = df.select_dtypes(include=["float64", "int64"])
    
    stat, p = kendalltau(df["{}".format(data1)], df["{}".format(data2)], nan_policy="omit", method="auto", variant="b") #variant=[b,c]
    print('stat=%.4f, p=%.4f' % (stat, p), "\n")
    if p > 0.05:
        print('H0: the two samples are probably independent. \n \n \n')
    else:
        print('H1: there is probably a dependency between the samples \n \n \n')

def CHI2(url = "adult.csv", data1="age", data2="y"):
    df = pd.read_csv(url)
    df = df.select_dtypes(include=["float64", "int64"])
    table = [df["{}".format(data1)], df["{}".format(data2)]]
    
    stat, p, dof, expected = chi2_contingency(table)
    print('stat=%.4f, p=%.4f' % (stat, p), "\n")
    if p > 0.05:
        print('H0: the two samples are probably independent. \n \n \n')
    else:
        print('H1: there is probably a dependency between the samples \n \n \n')


if __name__ == "__main__":
    main()



