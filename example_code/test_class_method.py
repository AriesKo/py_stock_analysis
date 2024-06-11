class NasdaqStock:
    def __init__(self, symbol, price):
        self.symbol = symbol # instance variable
        self.price = price # instance variable

    def __str__(self):
        return f"{self.symbol}: {self.price}"
    
    def __del__(self):
        print("Destructor called")

    
if __name__ == "__main__":
    stock = NasdaqStock("AAPL", 150.00)
    print(stock)
    del stock