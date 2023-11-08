primes = [2,3,5,7]
for i in primes:
    print(i)

for x in range(3,8,2):
    print(x)    

count = 0
while count<5:
    print(count)
    count+=1

count = 0
while True:
    print(count)
    count+=1
    if count==5:
        break

for x in range(10):
    if x%2 == 0:
        continue 
    print(x)