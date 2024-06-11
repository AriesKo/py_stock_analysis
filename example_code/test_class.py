class A:
    def methodA(self):
        print("Calling A's methodA")
    def method(self):
        print("Calling A's method")

class B:
    def methodB(self):
        print("Calling B's methodB")

class C(A,B):
    def methodC(self):
        print("Calling C's methodC")
        
    def method(self):
        print("Calling C's overridden method")
        super().method()

if __name__ == "__main__":
    d = C()
    d.methodA()
    d.methodB()
    d.methodC()
    d.method()