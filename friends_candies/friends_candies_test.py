from random import random,seed,randint,shuffle
import numpy,os
for k in range(18):
    seed(k+3)    
    testname="./input/input"+"%02d"%k+".txt"
    if os.path.exists(testname):
        os.remove(testname)
    f=open(testname,'+a')
    numbers=[]
    testcase=randint(1,10000)
    # testcase=1
    f.write(str(testcase))
    f.write('\n')
    
    for i in range(testcase):
        N=randint(1,100000)
        M=randint(1,100000)
        f.write(str(N))
        f.write('\n')
        f.write(str(M))
        f.write('\n')
        seed(i+100+13)
        a=[]
        for j in range(N):
            seed(i+100+13+j)
            a.append(str(randint(1,10000)))
        f.write(' '.join(a))
        f.write('\n')
        sum=randint(0,N)
        for i in range(M):
            l=randint(0,sum)
            r=sum-l
            choice=[str(l),str(r)]
            f.write(' '.join(choice))
            f.write('\n')
    print("test case",k)