from random import random,seed,randint,shuffle
import numpy,os
for k in range(18):
    seed(k+3)    
    testname="./input/input"+"%02d"%k+".txt"
    if os.path.exists(testname):
        os.remove(testname)
    f=open(testname,'+a')
    testcase=randint(1,100)
    f.write(str(testcase))
    f.write('\n')
    for i in range(testcase):
        seed(i+100+k+13)
        n=randint(1,100)
        d=randint(1,n)
        f.write(str(n))
        f.write(str(' '))
        f.write(str(d))
        f.write(str('\n'))
    print("test case",k)