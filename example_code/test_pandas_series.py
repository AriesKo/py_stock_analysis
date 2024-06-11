import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    s = pd.Series([1, 3, 5, 7, 9])
    print(s)
    s.index = pd.Index(['a', 'b', 'c', 'd', 'e'])
    print(s)
    s.name = "Numbers"
    print(s)
    s['e'] = 11
    print(s)
    
    ser = pd.Series([1, 2, 3, 4, 5], index=['f', 'g', 'h', 'i', 'j'])
    s = s._append(ser)
    print(s)

    print(s.values[:])
    print(s.iloc[:])
    
    s.drop(index=['a', 'b', 'c'], inplace=True)
    print(s)
    
    print(s.describe())
    
    s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0, 5.5, 6.7, 4.2], index=['0.0', '1.2', '1.8', '3.0', '3.6', '4.8', '5.9', '6.8', '8.0'])
    s.index.name = 'MY_INDEX'
    s.name = 'MY_SERIES'

    plt.title('ELLIOTT WAVE')
    plt.plot(s,'bs--')
    plt.xticks(s.index)
    plt.yticks(s.values)
    plt.grid(True)
    plt.show()
