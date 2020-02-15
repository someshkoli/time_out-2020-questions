from subprocess import Popen, PIPE, STDOUT
import subprocess,os
for k in range(18):
    testname="out"+str(k)
    if os.path.exists('./'+testname):
            os.remove('./'+testname)
    subprocess.run(["touch","out"+str(k)])
    f=open(testname,'w')
    inpu=open("test"+str(k),'r')
    p = Popen(['./a.out'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
    x=inpu.read()
    # print(x)
    grep_stdout = p.communicate(input=x.encode())[0]
    f.write(grep_stdout.decode())