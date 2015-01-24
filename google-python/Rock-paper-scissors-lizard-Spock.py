# Rock-paper-scissors-lizard-Spock template
import math
import random

# helper functions

def number_to_name(number):
    # Covert numbers to corresponding strings
    if    number == 0: 
        name = 'Rock'
        return name
    elif number == 1: 
        name = 'Spock'
        return name
    elif number == 2: 
        name = 'Paper'
        return name
    elif number == 3: 
        name = 'Lizard'
        return name
    elif number == 4: 
        name = 'Scissors'
        return name
    else: 
        return "Unknown code!"
        
    
def name_to_number(name):
    # Convert strings to equivalent numbers
    if name.capitalize() == 'Rock': 
        number = 0
        return number
    elif name.capitalize() == 'Spock': 
        number = 1
        return number
    elif name.capitalize() == 'Paper': 
        number = 2
        return number
    elif name.capitalize() == 'Lizard': 
        number = 3
        return number
    elif name.capitalize() == 'Scissors': 
        number = 4
        return number
    else: 
        return "Please enter one of Rock |Paper |Spock |Lizard |Scissors"
 
def rpsls(name): 

    # convert name to player_number using name_to_number
    print 'You Guess:', name.capitalize()
    player_number = name_to_number(name)
     
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    print 'Computer Guessed:', number_to_name(comp_number)
    
    # compute difference of player_number and comp_number modulo five
    diff = (player_number - comp_number) % 5
    #print diff
    
    # use if/elif/else to determine winner and print results
    if diff == 0: 
        print "woow, it's a Tie! Play again... \n\n"
    elif diff == 1:
        print "Awesome. You Win! \n\n"
    elif diff == 2:
        print "Now, you're on a Winning Streak! \n\n"
    elif diff == 3:
        print "haha, knock out.... You Lose! \n\n"
    elif diff == 4:
        print "Sorry mate, you've just lost \n\n"
    else:
        print "I don't understand that!"
        
        
# test your code
print "Let the Game Begin!(Bells)\n==========================\n"
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

