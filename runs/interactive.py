import numpy as np
import sys
from subprocess import call
import time
import pandas as pd

tmax = 5.e7
Nruns = int(sys.argv[1])

df = pd.DataFrame(columns=('K','mag','filename'))

datapath = '../data/'
for filename in os.listdir(datapath):
    result = re.search(r"IC(.*)K(.*)mag(.*).bin", filename)
    if result:
        simID = int(result.group(1))
        K = float(result.group(2))
        mag = float(result.group(3))
        filename='IC{0}K{1:.4e}mag{2:.4e}.bin'.format(simID, K, mag)
        df.loc[simID] = [K,mag,filename]
        
df = df.sort_index()

with open("data/runlog.txt", "a+") as f:
    f.seek(0)
    lines = f.readlines()
    if lines:
        lastseed = int(lines[-1])
    else:
        lastseed = -1 
    
    for i in range(lastseed+1, lastseed+Nruns+1):
        run = df.iloc[i]
        f.write("{0}\n".format(i))
        print(i)
        call("python run.py {0} {1} &".format(run['filename'], tmax), shell=True)

