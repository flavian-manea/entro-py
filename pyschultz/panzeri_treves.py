import numpy as np

"""
panzeri_treves.py

This script is part of pyschultz library. It is calculating the entropy and
mutual information of a binary 3D matrix [stimuli x word_length x # of trials]
using the panzeri-treves method. The first argument of all the functions is the binary
matrix. The second argument is the number of stimul(the first dimension of X,
default to 1). The third argument is the time bin which has to be a divident of
the time window(i.e. number of trials, also default to 1).
We assume the numpy package is installed and the input matrix is binary.

"""

def entropy_all(X, s = 1, dt = 1):
    xl,T = X[0,:,:].shape
    Hx = np.zeros(T//dt)
    PT = np.zeros(T//dt)
    R = 2^xl
    for i in range(np.int(T/dt)):
        for yy in range(s):
            if yy==0:
                XX = X[yy,:,:dt*(i+1)].astype(int)
            else:
                XX = np.hstack((XX, X[yy,:,:dt*(i+1)].astype(int)))
        uniqueColumns, occurCount = np.unique(XX, axis=1, return_counts=True)
        p = occurCount/sum(occurCount)
        Hx[i] = -sum(p*np.log2(p))
        N = dt*(i+1)
        bias = -1/(2*N*np.log(2))*(R-1)
        PT = Hx - bias
    return PT

def entropy(X, s = 1, dt = 1):
    xl,T = X[0,:,:].shape
    Hxs = np.zeros((s,T//dt))
    PTs = np.zeros((s,T//dt))
    R = 2^xl
    for yy in range(s):
        for i in range(T//dt):
            XX =  X[yy,:,:dt*(i+1)].astype(int)
            uniqueColumns, occurCount = np.unique(XX, axis=1, return_counts=True)
            p = occurCount/sum(occurCount)
            Hxs[yy,i] = -sum(p*np.log2(p))
            N = dt*(i+1)
            bias = -1/(2*N*np.log(2))*(R-1)
            PTs[yy,i] = Hxs[yy,i] - bias
    return PTs

def mutual_information(X, s = 1, dt = 1):
    PTs_all = np.sum(entropy(X,s,dt)*1/s,0)
    I_PT = entropy_all(X,s,dt)-PTs_all
    return I_PT
