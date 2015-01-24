#%%

f_open = open('readme.txt', 'rU')
indat = f_open.read().split()


print '''****************** '''
from collections import Counter
countdat = Counter(indat)
print (countdat)

# %%
