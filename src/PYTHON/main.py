import numpy as np
import os
from read_inputs import *
import sys

def main():
    path=os.getcwd() # get path of ljmd.py
    a=sys.mdsys_t()
    dict = read_inputs('argon_108','../..')
    a.input(dict)

if __name__ == "__main__":
    main()
