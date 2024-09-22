from pandas_datareader import data as pdr
import yfinance as yf 

if __name__ == '__main__':
    yf.pdr_override()
    
    sec = pdr.get_data_yahoo('005930.KS',start='2018-05-04')
    msft = pdr.get_data_yahoo('MSFT',start='2018-05-04')
    print(sec.head(10))
    print(msft.tail(10))
