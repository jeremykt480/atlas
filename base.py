
import os, sys, pandas as pd, quandl as qnd, requests, yfinance as yf
import json, numpy as np, glob
from datetime import date, datetime, timedelta; from bs4 import BeautifulSoup
# from scipy.stats import norm
# import scipy.stats as st
# import statsmodels as sm


class get_sym:
    def __init__(self, ticker):
        self.ticker=ticker

    def get_rtn(self, start, end):
        print ('...Collecitng data for '+self.ticker)
        self.rtn=yf.download(self.ticker, start, end)
        self.rtn=self.rtn['Adj Close'].pct_change().dropna()
        return self.rtn