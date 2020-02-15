from random import random,seed,randint,shuffle,choices
import numpy,os
import string
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
        seed(k+100+i)
        N=randint(1,500)
        K=randint(1,500)
        f.write(str(N))
        f.write(' ')
        f.write(str(K))
        f.write('\n')
        ar=''.join(list(choices(string.ascii_lowercase,k=N)))
        f.write(ar)
        f.write('\n')
    print("test case",k)