class Student():
    def __init__(self,name):
        self._name =name

    def __gt__(self, obj):
        print("哈哈，{0}会比{1}打吗".format(self,obj))
        return self._name > obj._name


 #字符串比较规则是什么
 #小写比大写大
 #小写中按字母顺序，顺序靠前比靠后大
stu1=Student("one")
stu2=Student("two")
print(stu1 > stu2)


#作业：
#下面显示结果不太美观，能否改成文字形式