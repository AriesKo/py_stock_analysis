import pandas as pd
import matplotlib.pyplot as plt
if __name__ == "__main__":
    df = pd.DataFrame([[1915,542],[1961,584],[1811,557],[1761,536],[1812,570]], index=[2018,2019,2020,2021,2022], columns=['KOSPI','KOSDAQ'])
    
    df = pd.DataFrame({'KOSPI':[1915,1961,1811,1761,1812],
                       'KOSDAQ':[542,584,557,536,570]},
                       index=[2018,2019,2020,2021,2022])
    print(df)
    print(df.info())
    print(df.describe())
    print(df.columns)
    print(df.index)
    
    kospi = pd.Series([1915,1961,1811,1761,1812], index=[2018,2019,2020,2021,2022], name='KOSPI')
    kosdaq = pd.Series([542,584,557,536,570], index=[2018,2019,2020,2021,2022], name='KOSDAQ')
    
    df = pd.DataFrame({
        kospi.name: kospi,
        kosdaq.name: kosdaq
    })
    print(df)

    columns = ['KOSPI','KOSDAQ']
    index = [2018,2019,2020,2021,2022]
    rows = []
    rows.append([1915,542])
    rows.append([1961,584])
    rows.append([1811,557])
    rows.append([1761,536])
    rows.append([1812,570])
    df = pd.DataFrame(rows, index=index, columns=columns)
    print(df)
    
    for i in df.index:
        print(i,df['KOSPI'][i],df.loc[i]['KOSPI'])
        
    for row in df.itertuples(name='KRX'):
        print(row)
        
    for row in df.itertuples():
        print(row[0],row[1],row[2])
        
    for idx,row in df.iterrows():
        print(idx,row[0],row[1])
    
