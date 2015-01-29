"""
Roman Dictionary
----------------

Mark Antony keeps a list of the people he knows in several dictionaries 
based on their relationship to him::
    
    friends = {'julius': '100 via apian', 'cleopatra': '000 pyramid parkway'}
    romans = dict(brutus='234 via tratorium', cassius='111 aqueduct lane')
    countrymen = dict([('plebius','786 via bunius'), 
                       ('plebia', '786 via bunius')])


1. Print out the names for all of Antony's friends.
2. Now all of their addresses.
3. Now print them as "pairs".
4. Hmmm.  Something unfortunate befell Julius.  Remove him from the 
   friends list.
5. Antony needs to mail everyone for his second-triumvirate party.  Make
   a single dictionary containing everyone.
6. Antony's stopping over in Egypt and wants to swing by Cleopatra's 
   place while he is there. Get her address.
7. The barbarian hordes have invaded and destroyed all of Rome.
   Clear out everyone from the dictionary.
   
See :ref:`roman-dictionary-solution`.   
"""

friends = {'julius': '100 via apian', 'cleopatra': '000 pyramid parkway'}
romans = dict(brutus='234 via tratorium', cassius='111 aqueduct lane')
countrymen = dict([('plebius','786 via bunius'), ('plebia', '786 via bunius')])

# Names of all friends
#print(friends.keys() + romans.keys() + countrymen.keys())

#Addresses of all friends
#print(friends.values() + romans.values() + countrymen.values())

#Pairs of names and addresses
all_friends = friends.items() + romans.items() + countrymen.items()
print(all_friends)

print(all_friends.pop(0) )

#Dictionary of all
friends_dict = dict(all_friends)
print(friends_dict)

#Cleopatra's address
print(friends_dict['cleopatra'])

friends_dict.pop('plebia')
print(friends_dict)

del friends_dict['brutus']

print(friends_dict)

friends_dict.clear()

print(friends_dict)