#My first program

"""var1 = 2

def add2(var1):
    var2 = var1 +2
    return var2

var2 = add2()

print(var2)

print(__name__)"""
"""name is assigned file name when imported as a module. when run
as a script name is set by Python to __main__"""

"""if __name__ == '__main__':"""



"""def add2(num):
    
    y = num + 2
    return y

x = add2(x)"""

class MyClass:
    
    def __init__(self, x = 2, y = 3):
        self.a = x
        self.b = y
        
    def add_nums(self):
       return self.a + self.b
       

class NewClass1(MyClass):
    
    def add_nums(self):
        return self.a + self.b*2
    
    def sub_nums(self):
        return self.a - self.b
        
if __name__ == '__main__':
    
    c = MyClass()
    print(c.a)
    print(c.b)
    z = c.add_nums()
    print(z)

    
"""if __name__ == '__main__':
    x = 3
    y = 3"""

    