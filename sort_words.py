"""
Sort Words
----------

Given a (partial) sentence from the Declaration of Independence, print out
a list of the words in the sentence in alphabetical order. Also print out just
the first two words and the last two words in the sorted list.

::

    speech = '''Four score and seven years ago our fathers brought forth
             on this continent a new nation, conceived in Liberty, and
             dedicated to the proposition that all men are created equal.
             '''


Ignore case and punctuation.

See :ref:`sort-words-solution`.
"""


#%%

speech = '''Four score and seven years ago our fathers brought forth
         on this continent a new nation, conceived in Liberty, and
         dedicated to the proposition that all men are created equal.
         '''

newspeech = speech.split()

newspeech.sort(key=str.lower)

print newspeech

print("\n\nThe first two words : {}".format(newspeech[:2]))

print("\n\nLast two words : {}".format(newspeech[-2:]))
