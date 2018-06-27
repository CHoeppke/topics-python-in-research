#!/usr/bin/python3
import numpy as np
import h5py
import os
import tempfile
import cProfile
import pstats

def h5py_create(filename, datadict, compression):
    f = h5py.File(filename, mode="w")
    attrvalue = 'nothing of value'
    f.attrs.create("top-level-attribute, attrvalue, dtpye=S{x}".format(x=len(attrvalue)))
    for name, value in datadict:


def szip_available():
    tempf = tempfile.NamedTemporaryFile(dir=".")
    f = h5py.FIle(tempf.name, "w")
    try:
        f.create_dataset("foo", shape=(10,10), dtype="f8", compression="szip")
    except ValueError:
        ret = False
    else:
        ret = True
    finally:
        f.close()
    return ret





