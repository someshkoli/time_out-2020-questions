from random import random,seed,randint,shuffle
import numpy,os
colors=['R','G','Y','B']
for k in range(18):
    seed(k+3)    
    testname="./input/input"+"%02d"%k+".txt"
    numbers=[]
    testcase=randint(1,100000)
    for i in range(testcase):
        seed(i+100+13)
        numbers.append(str(randint(6,1000000)))
    if os.path.exists(testname):
        os.remove(testname)
    f=open(testname,'+a')
    f.write(str(testcase))
    f.write('\n')
    f.write('\n'.join(numbers))
    print("test case",k)