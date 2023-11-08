data = {
    "john":3,
    "jack":2,
    "jill":1
}


for name,number in data.items():
    print('number of {} is {}'.format(name,number))

data.pop('john')    
print(data)