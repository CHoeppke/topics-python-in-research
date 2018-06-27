#!/usr/bin/env python3

import array
import h5py
import mpi4py
import os
import tempfile
import texttable as tt
from mpi4py import MPI

if(MPI.COMM_WORLD.rank == 0):
    temp = "./files/hdf5_vis_ex.h5"
else:
    temp = ""

KEEP_ME_AROUND = MPI.COMM_WORLD.bcast(temp, root=0)
rank = MPI.COMM_WORLD.rank
f = h5py.File(KEEP_ME_AROUND, "w", driver="mpio", comm=MPI.COMM_WORLD)
dset = f.create_dataset("test", (4, ), dtype="f8")
dset[rank] = rank
