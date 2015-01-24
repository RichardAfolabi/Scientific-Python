
#import sys

def trials():
    """
    Documentations here about this function.
    """
    print("Questions for you...")
    likes = raw_input("Do you like me? ")
    lives = raw_input("where do you live? ")
    pcname = raw_input("Your computer brand : ")
    
    print ("\n")
    print("Do I like you? %s! because you live at %s and you use %s computer" % (likes,lives,pcname))
    


def repeater(sarg, nrep, exclaim):
    """    
        Define a function that takes a string sarg, repeats it nrep times with nrep exclamation marks.
        sarg : string
        nrep : integer
        exclaim: boolean
    """
    
    result = sarg * nrep
    if exclaim:
        result = result + '!'*nrep
    return result



def main():
    pass




if __name__ == '__main__':
    main()