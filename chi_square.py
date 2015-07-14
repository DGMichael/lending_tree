#chi_square.py

import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import collections

def load_runChi():
    """Load data into pandas dataframe, clean and return."""
    loanData = pd.read_csv("https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv")
    loanData.dropna(inplace = True)
    freq = collections.Counter(loanData["Open.CREDIT.Lines"])
    chi, p  = stats.chisquare(freq.values())
    print chi, p

def main():
    load_runChi()

main()

