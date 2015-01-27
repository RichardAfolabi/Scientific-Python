'''
Program that reads a file and prints out words that are anagrams of each other
in the file. Key is to sort the words in order. If any two words are anagrams
of each other, they should have exactly same words which will be same number
of words and letters when sorted.
'''

# Function to find the key of each word.
def findkey(inword):
    wordkey = sorted(inword)
    #concatenate the list
    wordkey = ''.join(wordkey)
    return wordkey
    

# Search through the file and store words that are anagrams in dictionary
def find_anagrams(wordfile):
    infile = open(wordfile)
    words_dict = dict()
    for word in infile:
        word = word.strip()
        inword = findkey(word)
        
        if inword not in words_dict:
            words_dict[inword] = [word]
        else:
            words_dict[inword].append(word)
    infile.close()

    return words_dict
            

# Print according to size of the anagram in Descending order down to length 2.
def anagram_size(words_dict, maxsize):
    newlist = []
    for x in words_dict.values():
        if len(x) >= maxsize:
            newlist.append((len(x),x))
        
    sort_list = sorted(newlist,reverse=False)
    return sort_list


# Print anagrams that are exactly 8 letters.
def bingo_anagram(words_dict, bingo_size):
    newlist = []
    for wordky,anag in words_dict.iteritems():
        if len(anag) == bingo_size:
            newlist.append((wordky, len(anag), anag))
    return newlist

        

if __name__ == '__main__':
    anagwords = find_anagrams('words.txt')
    
    for i in anagwords.iteritems(): 
        print i
        
    print "\n\n"
    for i in anagram_size(anagwords,3):
        print i

    print "\n\n"    
    for i in bingo_anagram(anagwords, 8):
        print i
     