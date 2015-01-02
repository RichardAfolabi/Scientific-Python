"""
Vote String
-----------
Let's assume that you are responsible for analyzing the outcome of a referendum
organized to decide whether or not Texas should secede from the rest of the USA
in your (very small) town. You are being given the data in the form of the
string below, which is a set of "yes/no" votes, where "y" and "Y" both mean
"yes" and "n" and "N" both mean "no".

votes = "y y n N Y Y n n N y Y n Y"

Determine the percentages of "yes" and "no" votes in this small dataset.

Note: There is no need for a "for" loop: by simply exploring the methods
available on any string, you will find enough tools to do this.
"""
# Begin exercise here

#%%
votes = "y y n N Y Y n n N y Y n Y"



def findpercentage(votes, dresponse):
    voting = str(votes).upper().split()
    count_response = voting.count(dresponse.upper())
    findpcent = count_response / float(len(voting)) * 100
    return findpcent
    

positives = findpercentage(votes, 'y')

negatives = findpercentage(votes, 'n')

print positives
print positives + negatives