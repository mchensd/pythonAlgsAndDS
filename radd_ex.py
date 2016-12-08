class MyNum:
    def __init__(self,num):
        self.num=num
    def __add__(self,other):
        return MyNum(self.num+other.num)
    def __radd__(self, other):
        return MyNum(self.num + other)
    def __str__(self):
        return str(self.num)


t = MyNum(23)
print(3 + t)
