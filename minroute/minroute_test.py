from random import random,seed,randint,shuffle
import numpy,os
colors=['R','G','Y','B']
for k in range(18):
    seed(k)    
    m=randint(1,60)
    n=randint(1,60)
    testname="./input/input"+"%02d"%k+".txt"
    discs=[]
    for i in range(m):
        for j in range(n):
            seed(i+j)
            numpy.random.shuffle(colors)
            x=[]
            for a in colors:
                # print(a,end="")
                x.append(a)
            discs.append(x)
            # print()
    if os.path.exists(testname):
        os.remove(testname)
    f=open(testname,'a')
    f.write(str(m))
    f.write(" ")
    f.write(str(n))
    f.write('\n')
    for a in discs:
        # print(print(*a,sep=" "))
        f.write(' '.join(a))
        f.write('\n')