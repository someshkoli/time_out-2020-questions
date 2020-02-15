from random import random,seed,randint,shuffle,choice
import numpy,os
for k in range(18):
    seed(k+3)    
    testname="./input/input"+"%02d"%k+".txt"
    if os.path.exists(testname):
        os.remove(testname)
    f=open(testname,'+a')
    inp=''
    for _ in range(randint(0,100000)):
        inp=inp+choice(['A','B','C'])
    f.write(inp)
    print("test case",k)