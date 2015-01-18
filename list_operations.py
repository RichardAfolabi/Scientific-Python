
# List Operations
# ===============
# 
# This exercise provides the opportunity to experiment some more with list creation and the use of their methods. Feel free to skip.
# 
# Create a list 'a' with the elements 10,21,23,11 and 24 in this order

#%%
# your code goes here


# Modify the first element and the last element to be 0.


# your code goes here


# The following questions can all be answered using the appropriate methods attached to the list a.
# 
# Add the element 11 at the end of the list a.

# Hint: To explore the available methods, type a.< TAB > in  ipython.


# your code goes here


import numpy as np

a = np.array([10, 21, 23, 11, 24])

a[0] = 0
a[-1] = 0

print a

b = [10, 21, 23, 11, 24]
b.insert(len(b),11)

b.extend([11])
print b

print b.count(11)

b.extend(['foo', 4])

print b
#%%


# What is the location of the first occurrence of 11?


b.index(11)

# Insert the value 100 as the third element. Hint: All python sequences start at index 0. 

b.insert(2,100)
print b

#%%

# Remove the forth element.
b.remove(b[3])
print b


# Remove the first occurrence of 11
b.remove(11)

print b
#%%

b.sort()

print b

b.reverse()
print b



#%%

11 in b

# Test if 11 is in the list anymore and if 99 is *not* in the list

99 not in b
# your code goes here

