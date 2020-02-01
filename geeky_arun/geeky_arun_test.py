from random import random,seed,randint,shuffle
import numpy,os
for k in range(18):
    seed(k)    
    m=randint(1,100000)
    testname="test"+str(k)
    T=randint(1,100000)
    numbers=[]
    for i in range(T):
        seed(k+i)
        temp=randint(1,29)
        numbers.append(str(2**temp))
    if os.path.exists('./'+testname):
        os.remove('./'+testname)
    f=open(testname,'+a')
    f.write(str(T))
    f.write('\n')
    f.write('\n'.join(numbers))
    print(testname)
    # f.write('\n')