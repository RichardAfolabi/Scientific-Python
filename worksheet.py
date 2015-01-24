import numpy as np
import numpy.random as rand
from scipy.optimize import curve_fit
import scipy.io as scpy
import matplotlib.pyplot as plt


#%%

import random

alplist = ['c','a','t','d','o','g']

random.shuffle(alplist)

alplist.
#%%

def cls(): print "\n" *50          #Function to clear screen.

cls()


# Unlike matlab, list cannot broadcast. That is perform same operation together
# e.g. we have to setup loop to multiply array with scalar.

#print range(3)*1.1

#However, an array can broadcast. Create an array with 10^3 elements - ndarray
arr = np.arange(10)
print arr * 1.1

#Convert array back to list. Will not work
larr = arr.tolist()
#print larr * 1.1        

def list_times(alist,scalar):
    for i, val in enumerate(alist):
        alist[i] = val * scalar
    return alist

# Call the nparray
print '\n\n',list_times(larr, 1.1)


# Given a List, we can perform broadcast operation by converting to Array 1st
print "\n\n", np.array(range(10))*1.1

# Create some special arrays then reshape to n-dimensions
print np.zeros(9)
print np.arange(9).reshape((3,3))
print np.arange(10,19).reshape((3,3))

# Create array from 0 to 1 of 100 steps 
print '\n', np.linspace(0,1,100).reshape((10,10))

# Create array from 1 to 10 in Log10 base of 100 steps 
print "\n", np.logspace(0,1,100, base=10)

# Create a 5x5x5 matrix cube of 1s
print "\n", np.zeros((2,5,5)).astype(int)+1

# Create random number fomr Gaussian Dist. then filter out values > 0.2
arr = rand.randn(10)

data = np.empty((1000,1000))
np.save('test.npy',data)
newdata = np.load('test.npy')
print newdata

#%%
# Solving Linear Algebra with Python
# 3x + 6y - 5z = 12
#  x - 3y + 2z = -2
# 5x - y  + 4z = 10
# We represent the coefficients of x y x as A and the values as B, then x,y,z as X
# so we have AX = B
# and X = A^(-1) * B

# Define matrices A & B using the matrix command
A = np.matrix([[3, 6,-5],
               [1,-3, 2],
               [5,-1, 4]])
                    
B = np.matrix([[12],
               [-2],
               [10]])       


# Define A2 & B2 using the Array command
A2 = np.array([[3, 6,-5],
               [1,-3, 2],
               [5,-1, 4]])
               
B2 = np.array([12,-2,10])                                        

# Solving for the variable X = x,y,z using A & B (Matrices)
X = A**(-1)*B

# Solving for the variable X2 = x,y,z in A2 & B2 (Arrays) 
# using linear algebra inversion and dot multiplication function
X2 = np.linalg.inv(A2).dot(B2)

X3 = np.linalg.solve(A,B)

print "\n\n x = %.3f, y = %.3f, z = %.3f" %(X[0],X[1],X[2])
print "\n\n x = %.3f, y = %.3f, z = %.3f" %(X2[0],X2[1],X2[2])  
print "\n\n x = %.3f, y = %.3f, z = %.3f" %(X3[0],X3[1],X3[2])


#%%

      
finp = open('words.txt','r')
noe = 0
total_words = 0
dict_words = dict()
for line in finp:
    total_words +=1
    if ('e' not in line):
        dict_words[line.strip()] = 1 
        noe +=1
print dict_words        
print "\n%d Out of %d words do not contain letter 'e'" %(noe,total_words) 
print "{0:.2f}% contains letter 'e'".format(float(float(noe)/float(total_words) * 100))
finp.close()    


#%% ==============



# create model function
def func(x,a,b,c):
    return a*np.exp(-(x-b)**2/(2*c**2))
    
# Generate clean data
x = np.linspace(0,10,100)    
y = func(x,1,5,2)

# Generate noisy data
ynoise = y + 0.2 * np.random.normal(size=len(x))

#Execute curve fit
popt,pcov = curve_fit(func,x,ynoise)

#Results
print"\n", popt
print"\n", pcov


#%%====

def func(x, a0, b0, c0, a1, b1,c1):
    return a0*np.exp(-(x - b0) ** 2/(2 * c0 ** 2))\
    + a1 * np.exp(-(x - b1) ** 2/(2 * c1 ** 2))
    
# Generating clean data
x = np.linspace(0, 20, 200)
y = func(x, 1, 3, 1, -2, 15, 0.5)

# Adding noise to the data
yn = y + 0.2 * np.random.normal(size=len(x))

# Since we are fitting a more complex function, providing guesses for the 
# fitting will lead to better results.
guesses = [1, 3, 1, 1, 15, 1]

# Executing curve_fit on noisy data
popt2, pcov = curve_fit(func, x, yn, p0=guesses) 
popt2 = popt2.tolist()    

plt.figure(1)
plt.clf()
plt.plot(x,y,x,yn)
#plt.plot(len(popt),popt)
popt, pcov = curve_fit(func, x, yn) 
popt = popt.tolist()    

plt.plot(x,func(x,popt2[0],popt2[1],popt2[2],popt2[3],popt2[4],popt2[5]))

plt.plot(x,func(x,popt[0],popt[1],popt[2],popt[3],popt[4],popt[5]))

#%%
import re
inplink = "http://www.youtube.com/watch?v=ojvZs06VHsk"

video_id = re.search(r'(?<=v=).+', inplink)

if video_id:
    print 'video ID found', video_id.group(0)
else:
    print 'Not found'

#%%
import urlparse
url = "http://www.youtube.com/watch?v=ojvZs06VHsk"
parsed = urlparse.urlparse(url)
print urlparse.parse_qs(parsed.query)['v']

import urlparse
url = "http://www.youtube.com/?vx=ojvZs06VHsk"
parsed = urlparse.urlparse(url)
print urlparse.parse_qs(parsed.query)['vx']

#%%
import re
inplink = "/?vx=_AzolHV94LU#"

video_id = re.search(r'/?vx.+', inplink)

if video_id:
    print 'http://www.youtube.com/' + video_id.group(0)
else:
    print 'Not found'
    

    
#%%


def sumx():
    total = 0
    try:
        values = input('Enter all values to add >')
        for v in values:
            total += v
    except Exception as excpt:
        print 'Error!', excpt
        
    return ('Total is %d' %total)
    
print sumx()

    
#%%
def sqrtx(x):
    if not isinstance(x,(int, float,str)):
        raise TypeError('Sorry. Input must be numeric')
    elif x < 0:
        raise ValueError('Sorry, input cannot be negative')
    return 'Input is valid!'

print sqrtx(9)

#%%

try:
    fp = open('sample.txt')
except Exception as excpt:
    print'File error.', excpt
    
#%%
k =4
print('False' if k > 2 else 'True')

print divmod(54,4)

a,b,c = 3,4