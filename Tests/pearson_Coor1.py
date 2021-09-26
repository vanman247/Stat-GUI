from scipy.stats import pearsonr
from tkinter import *
from tkinter import filedialog

    
def main(url = "adult.csv",  data1="age", data2="y"):
    direc="C:/Users/Ammon Van/Desktop/Fun Projects/Statistic Analysis/Tests"
    filetypes = (("CSV", "*.CSV"), ("All Files", "*.*"))
    url = filedialog.askopenfilename(initialdir=direc, title="Open File", filetypes=filetypes)
    url = open(url, "r")
    stuff = url.read()
    text1.insert(END, stuff)
    url.close()
##    data1 = 
##    data2 = 
    

    try:
        print("Pearson’s Correlation Coefficient \n \n \n")
        print("_____ASSUMPTIONS______")
        print("    1. Observations in each sample are independent and identically distributed")
        print("    2. Observations in each sample are normally distributed")
        print("    3. Observations in each sample have the same variance \n")
        pearson(url = url, data1=data1, data2=data2)
    except ValueError:
        print(ValueError)
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



if __name__ == "__main__":
    main()
