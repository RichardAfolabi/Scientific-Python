import numpy as np
import scipy.io as scpy
import matplotlib.pyplot as plt


# Evenly sampled time at 200ms intervals
tme = np.arange(0, 5, 0.2)

plt.figure(2)
plt.clf()
plt.plot(tme,tme**2.5,'-r*', tme, tme**2,'-bs', tme,tme**3,'-g^')
plt.grid()
plt.ylabel('Some numbers')
plt.xlabel('Sampled points')
plt.text(1.25, 60, r'$\mu=100,\ \sigma_i=15$', fontsize=12)
plt.legend(('data', 'model', 'fitter'), loc='best')
plt.savefig('testfig2.pdf', dpi=600)

#%% Using subplots and figure file

def func(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)    
t2 = np.arange(0.0, 5.0, 0.025)


plt.figure(3)
plt.clf()
plt.subplot(3,1,1)
plt.plot(t1,func(t1),'bo',t2,func(t2),'k')
plt.grid()

plt.subplot(3,1,2)
plt.plot(t2,np.cos(2*np.pi*t2),'r--')
plt.grid()

plt.subplot(3,1,3)
plt.semilogy(t1,np.exp(-t1),'r*')
plt.grid()



#%%

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)



plt.figure(4)
plt.clf()
#plot histogram
n, bins, patches = plt.hist(x,50,normed=1, facecolor='g', alpha=0.75)

plt.xlabel('Smart')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.axis([40, 160, 0, 0.03])
plt.text(60, 0.025, r'$\mu=100,\ \sigma_i=15$',fontsize=15)
plt.savefig('test_fig.pdf',dpi=600)
plt.grid(True)


