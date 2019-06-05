import numpy as np
import matplotlib.pyplot as plt
import plugin as plg
import panzeri_treves as pt
import nsb as nsb
import cdm as cdm



"""
This is a test script that generates a simulation of binary vectors according
to a poisson distribution and plots the performance comparison between different
estimates

"""

if __name__ == '__main__':

    print('This is a Test')

    Ym = 5
    T = 1000
    dt = 10
    xl = 5

    X = np.zeros((Ym,xl,T))
    for sID in range(1,Ym+1):
        l = 0.1*sID**2
        r = np.random.poisson(l,(xl,T))
        r[r>1] = 1
        s = (np.ones((1,T))*sID).astype(int)
        X[sID-1,:] = r.astype(int)

    I = plg.mutual_information(X,Ym,dt)
    I_PT = pt.mutual_information(X,Ym,dt)
    I_NSB = nsb.mutual_information(X,Ym,dt)
    I_CDM = cdm.mutual_information(X,Ym,dt)

    lines = plt.plot(np.log10(np.arange(T/10)+1), I, 'blue', np.log10(np.arange
    (T/10)+1), I_PT, 'red',np.log10(np.arange(T/10)+1), I_NSB, 'yellow',
    np.log10(np.arange(T/10)+1), I_CDM, 'green')
    plt.ylabel('Mutual information')
    plt.xlabel('Number of trials on logarithmic scale')
    plt.title('Performance comparison')
    plt.legend((lines[0], lines[1],lines[2],lines[3]),('Plugin', 'Panzeri-Treves','NSB','CDM' ))
    plt.show()
