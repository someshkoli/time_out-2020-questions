from subprocess import Popen, PIPE, STDOUT
import subprocess,os
for k in range(18):
    testname="./output/output"+"%02d"%k+".txt"
    if os.path.exists('./'+testname):
            os.remove('./'+testname)
    subprocess.run(["touch",testname])
    f=open(testname,'w')
    inpu=open("./input/input"+"%02d"%k+".txt",'r')
    p = Popen(['python3','marbles_sol.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
    x=inpu.read()
    # print(x)
    grep_stdout = p.communicate(input=x.encode())[0]
    f.write(grep_stdout.decode())
    print("output",k)