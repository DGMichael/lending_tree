#prob_lending_club.py

import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd

def load_loan_data():
    """Load loan data into pandas dataframe, clean data and return pandas dataframe"""
    loanData = pd.read_csv("https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv")
    loanData.dropna(inplace=True)

    return loanData

def plot_data(input_data):
    """Plot data"""
    #Generate box plot:
    plt.figure()
    input_data.boxplot(column = "Amount.Requested")
    plt.savefig("box_requested.png")
    #Generate histogram:
    plt.figure()
    input_data.hist(column = "Amount.Requested")
    plt.savefig("hist_requested.png")
    #Generate qqplot:
    plt.figure()
    graph = stats.probplot(input_data["Amount.Requested"], dist = "norm", plot = plt)
    plt.savefig("qqplot_requested.png")

def main():
    loans = load_loan_data()
    plot_data(loans)

main()