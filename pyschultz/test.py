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
    f = 10

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

true_value = np.mean([I[-1],I_PT[-1],I_NSB[-1],I_CDM[-1]])
asym = true_value*np.ones(I.size)

plg_var = np.zeros_like(I)
pt_var = np.zeros_like(I)
nsb_var = np.zeros_like(I)
cdm_var = np.zeros_like(I)


rmse_plg = np.zeros_like(I)
rmse_pt = np.zeros_like(I)
rmse_nsb = np.zeros_like(I)
rmse_cdm = np.zeros_like(I)

plg_mean = np.zeros_like(I)
pt_mean = np.zeros_like(I)
nsb_mean = np.zeros_like(I)
cdm_mean = np.zeros_like(I)

bias_plg = np.zeros_like(I)
bias_pt = np.zeros_like(I)
bias_nsb = np.zeros_like(I)
bias_cdm = np.zeros_like(I)

yerr_plg = np.zeros_like(I)
yerr_pt = np.zeros_like(I)
yerr_nsb = np.zeros_like(I)
yerr_cdm = np.zeros_like(I)

for i in range(I.size):
    plg_mean[i] = np.mean(I[:i+1])
    pt_mean[i] = np.mean(I_PT[:i+1])
    nsb_mean[i] = np.mean(I_NSB[:i+1])
    cdm_mean[i] = np.mean(I_CDM[:i+1])

    plg_var[i] = np.std(I[:i+1])**2
    pt_var[i] = np.std(I_PT[:i+1])**2
    nsb_var[i] = np.std(I_NSB[:i+1])**2
    cdm_var[i] = np.std(I_CDM[:i+1])**2

    if( i == 0 or ((i+1)%f)==0):
        yerr_plg[i] = plg_var[i]
        yerr_pt[i] = pt_var[i]
        yerr_nsb[i] = nsb_var[i]
        yerr_cdm[i] = cdm_var[i]



bias_plg = asym - plg_mean
bias_pt = asym - pt_mean
bias_nsb = asym - nsb_mean
bias_cdm = asym - cdm_mean

rmse_plg = (plg_var + bias_plg**2)**(1/2)
rmse_pt = (pt_var + bias_pt**2)**(1/2)
rmse_nsb = (nsb_var + bias_nsb**2)**(1/2)
rmse_cdm = (cdm_var + bias_cdm**2)**(1/2)

plt.rcParams['figure.figsize'] = [10, 10]
plt.figure(1)

plt.subplot(311)
plt.errorbar(np.arange(I.size),plg_mean, yerr = yerr_plg , color = 'blue', label = 'Plugin')
plt.errorbar(np.arange(I.size),pt_mean, yerr = yerr_pt, color = 'red' ,label = 'Panzeri-treves')
plt.errorbar(np.arange(I.size),nsb_mean, yerr = yerr_nsb, color = 'orange', label = 'NSB')
plt.errorbar(np.arange(I.size),cdm_mean, yerr = yerr_cdm ,color = 'green', label = 'CDM')
plt.plot(np.arange(I.size),asym,'--')
plt.xscale('log')
plt.legend(loc='upper right', frameon = False)
plt.ylabel('Mutual information', fontsize = 12)
plt.tick_params (labelsize = 12)


plt.subplot(312)
plt.plot(np.arange(I.size),plg_var,'blue', label = 'Plugin')
plt.plot(np.arange(I.size),pt_var,'red', label = 'Panzeri-treves')
plt.plot(np.arange(I.size),nsb_var,'orange', label = 'NSB')
plt.plot(np.arange(I.size),cdm_var, 'green', label = 'CDM')
plt.xscale('log')
plt.legend(loc='upper right', frameon = False)
plt.ylabel('Variance', fontsize = 12)
plt.tick_params (labelsize = 12)


plt.subplot(313)
plt.plot(np.arange(I.size),rmse_plg, 'blue', label = 'Plugin')
plt.plot(np.arange(I.size),rmse_pt,'red', label = 'Panzeri-treves')
plt.plot(np.arange(I.size),rmse_nsb,'orange', label = 'NSB')
plt.plot(np.arange(I.size),rmse_cdm, 'green', label = 'CDM')
plt.xscale('log')
plt.legend(loc='upper right', frameon = False)
plt.ylabel('Root mean squared error', fontsize = 12)
plt.xlabel('Number of trials',fontsize = 12)
plt.tick_params (labelsize = 12)

plt.tight_layout()
plt.savefig('test.png')
plt.show()
np.logspace()
