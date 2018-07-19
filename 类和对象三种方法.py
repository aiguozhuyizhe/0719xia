class Person():
    #实例方法
    def eat(self):
        print(self)
        print("eating")
    # 类方法
    # 类方法的第一个参数，一般命名为cls,区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("playing")

    #静态方法
    #不需要第一个参数表示自身或者类
    @staticmethod
    def say():
        print("saying")


yueyue=Person()

#实例方法
yueyue.eat()

#类方法
Person.play()#这两种都可以
yueyue.play()#实例当做类方法

#静态方法
Person.say()#这两种也都可以
yueyue.say()#实例当做静态方法