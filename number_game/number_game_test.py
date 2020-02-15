from random import random,seed,randint,shuffle
import numpy,os
colors=['R','G','Y','B']
for k in range(18):
    seed(k+3)    
    m=randint(1,100000)
    testname="./input/input"+"%02d"%k+".txt"
    numbers=[]
    for i in range(m):
        seed(i+100+13)
        numbers.append(str(randint(0,10000)))
    if os.path.exists(testname):
        os.remove(testname)
    f=open(testname,'+a')
    f.write(str(m))
    f.write('\n')
    f.write(' '.join(numbers))
    f.write('\n')