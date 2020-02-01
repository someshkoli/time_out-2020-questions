from random import random,seed,randint,shuffle
import numpy,os
for k in range(18):
    seed(k)    
    testname="test"+str(k)
    if os.path.exists('./'+testname):
        os.remove('./'+testname)
    f=open(testname,'+a')
    T=randint(1,10)
    f.write(str(T))
    f.write('\n')
    for i in range(T):
        seed(k+i)
        n=randint(1,20)
        f.write(str(n))
        f.write("\n")
        # for j in range(1,n+1):
        numbers=list(range(1,n+1))
        for x in range(1,n+1):
            f.write(str(x))
            f.write(' ')
            seed(k+i+x)
            numpy.random.shuffle(numbers)
            la=[]
            for a in numbers:
                la.append(str(a))
            f.write(' '.join(la))
            f.write('\n')
        for x in range(1,n+1):
            f.write(str(x))
            f.write(' ')
            seed(k+i+x+100)
            numpy.random.shuffle(numbers)
            la=[]
            for a in numbers:
                la.append(str(a))
            f.write(' '.join(la))
            f.write('\n')

    print(testname)