#!/usr/bin/python3
import numpy as np
import os
import tempfile
import cProfile
import pstats

N1 = 500
a = (int)(0.3*N1)
b = (int)(0.7*N1)

print("Data write test using {} values".format(N1 * N1 * N1))
data = np.random.random((N1, N1, N1))
tempfiles = [tempfile.TemporaryFile(dir='.') for i in [1, 2, 3, 4]]
cps = [cProfile.Profile() for i in range(len(tempfiles))]
runs = [np.savez, np.savez_compressed, np.savez_compressed, np.savez_compressed]


for i, r in enumerate(runs):
    if i == 2:
        data[a:b, a:b, a:b] = 0.0
    if i == 3:
        data = np.ones((N1, N1, N1), np.float64)

    cps[i].runcall(r, tempfiles[i], {"array_called_data": data})

print(''' Time spent and file sizes:
        uncompressed random: \t{S_1}    \t{T_1}\n
        compressed random: \t{S_2}    \t{T_2}\n
        compressed semirandom: \t{S_3}    \t{T_3}\n
        compressed nonrandom: \t{S_4}    \t{T_4}'''.format(
            S_1= os.stat(tempfiles[0].name).st_size,
            S_2= os.stat(tempfiles[1].name).st_size,
            S_3= os.stat(tempfiles[2].name).st_size,
            S_4= os.stat(tempfiles[3].name).st_size,
            T_1= pstats.Stats(cps[0]).total_tt,
            T_2= pstats.Stats(cps[1]).total_tt,
            T_3= pstats.Stats(cps[2]).total_tt,
            T_4= pstats.Stats(cps[3]).total_tt,))

