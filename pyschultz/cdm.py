import numpy as np
import os
import matlab.engine

"""
cdm.py

This script is part of pyschultz library. It is calculating the entropy and
mutual information of a binary 3D matrix [stimuli x word_length x # of trials]
using the cdm method. The first argument of all the functions is the binary
matrix. The second argument is the number of stimul(the first dimension of X,
default to 1). The third argument is the time bin which has to be a divident of
the time window(i.e. number of trials, also default to 1).
We assume the numpy package is installed and the input matrix is binary.
We also assumed MATLAB is installed and CDMentropy is downloaded.
"""

eng = matlab.engine.start_matlab()
cwd = os.getcwd()
str_1 = '/CDMentropy/src'
str_2 = '/CDMentropy/lib/PYMentropy/src'
eng.addpath(cwd+str_1, nargout=0)
eng.addpath(cwd+str_2, nargout=0)

def entropy_all(X, s = 1, dt = 1):
    xl,T = X[0,:,:].shape
    Hx = np.zeros(T//dt)
    for i in range(np.int(T/dt)):
        for yy in range(s):
            if yy==0:
                XX = X[yy,:,:dt*(i+1)].astype(int)
            else:
                XX = np.hstack((XX, X[yy,:,:dt*(i+1)].astype(int)))
        mat_d1 = matlab.double(XX.T.tolist())
        Hx[i] = eng.computeH_CDM(mat_d1)
    return Hx

def entropy(X, s = 1, dt = 1):
    xl,T = X[0,:,:].shape
    Hxs = np.zeros((s,T//dt))
    for yy in range(s):
        for i in range(T//dt):
            XX =  X[yy,:,:dt*(i+1)].astype(int)
            mat_d1 = matlab.double(XX.T.tolist())
            Hxs[yy,i] = eng.computeH_CDM(mat_d1)
    return Hxs

def mutual_information(X, s = 1, dt = 1):
    Hxs_all = np.sum(entropy(X,s,dt)*1/s,0)
    I_CDM = entropy_all(X,s,dt)-Hxs_all
    return I_CDM
