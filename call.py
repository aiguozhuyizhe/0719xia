class A():
    def __init__(self,name=0):
        print("调用了")

    def __call__(self):
        print("bei call le")
a=A()
a()  #对象当函数使用时，先调用__call__