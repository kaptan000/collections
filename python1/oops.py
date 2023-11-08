class Myclass:
    var = 'blah'
    def func(self):
        print('inside class')

x = Myclass()
y = Myclass()

y.var = 'hello'

print(x.var)
print(y.var)
print(x.func())

class NumberHolder:
    def __init__(self,n):
        self.number = n 

z = NumberHolder(5)
print(z.number)        