class A():
    name = "NoName"
    age = 18
    def __getattr__(self, item):
        print("没找到")
        print(item)

a=A()
print(a.name)
print(a.addr)

#作业：为什么会打印None？

#因为 默认返回值是None