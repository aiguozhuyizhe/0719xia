class A():
    def __init__(self,name=0):
        print("调用了")

    def __call__(self):
        print("bei call le")

    def __str__(self):
        return "haha"
a=A()
print(a)