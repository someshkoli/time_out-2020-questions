from random import random,seed,randint,shuffle
import numpy,os
for k in range(18):
    seed(k)    
    T=randint(1,10)
    testname="./input/input"+"%02d"%k+".txt"
    numbers=[]
    for i in range(T):
        seed(i+k)
        numbers.append(str(randint(1,100000)))
    if os.path.exists(testname):
        os.remove(testname)
    f=open(testname,'a')
    f.write(str(T))
    f.write('\n')
    f.write('\n'.join(numbers))
    print(testname)