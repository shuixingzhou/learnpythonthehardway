class Dog(object):   # 定义class
 
    def __init__(self, name):  # 构造函数，构造方法 == 初始化方法
        self.name = name   # d.name = name  类的属性 / 成员变量
 
    def say_hi(self):   # 类的方法
        print("Hello, I am a dog. My name is", self.name)
 
    def eat(self, food):
        print("%s is eating %s." % (self.name, food))
