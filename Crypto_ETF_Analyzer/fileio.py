"""Functions desgined to load data from Yfinance module,
and analyze performance in comparison to underlying assets (BTC and ETH).
"""

import yfinance as yf

def get_etf(etf_ticker):
    """This function uses YFinance module uses Yahoo Finance API to
    recall historical data"""
    etf_ticker = yf.Ticker(etf_ticker)
    etf_df = etf_ticker.history(period="max")
    etf_df["etf_pct_change"] = etf_df.loc[:, "Close"].pct_change()
    etf_df["etf_cum_returns"] = (etf_df.loc[:, "etf_pct_change"]+1).cumprod()
    return etf_df


def get_crypto(crypto_ticker):
    crypto_ticker = yf.Ticker(crypto_ticker)
    crypto_df = crypto_ticker.history(period="max")
    crypto_df["crypto_pct_change"] = crypto_df.loc[:, "Close"].pct_change()
    crypto_df["crypto_cum_returns"] = (crypto_df.loc[:, "crypto_pct_change"]+1).cumprod()
    return crypto_df

        
def plot_returns(etf_df, crypto_df):
    etf_plot = (etf_df).hvplot(x="Date", y="etf_cum_returns", title="Cumulative Returns", ylabel="Return")
    crypto_plot = (crypto_df).hvplot.line(x="Date", y="crypto_cum_returns", title="Cumulative Returns for BTC", ylabel="Cumulative Returns")
    return_plot = etf_plot * crypto_plot
    return return_plot
    
def plot_investment(etf_df, crypto_df, investment):
    etf_plot = (etf_df*investment).hvplot(x="Date", y="etf_cum_returns", title="Cumulative Returns", ylabel="Return")
    crypto_plot = (crypto_df*investment).hvplot.line(x="Date", y="crypto_cum_returns", title="Cumulative Returns for BTC", ylabel="Cumulative Investment Returns")
    investment_plot = etf_plot * crypto_plot
    return investment_plot