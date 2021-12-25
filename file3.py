import subprocess
import numpy as np

nparray = np.array([])
n = np.append(nparray,1)
print(n)

with open('subprocesslogs.txt','w') as f:
    out = subprocess.run('dir',shell=True,stdout=f,text=True)




