import random
def name_to_number(name):

    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    else :
        return 4



def number_to_name(number):

    if number==0:
        return "rock"
    elif number==1:
        return "Spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    else:
        return "scissors"

    

def rpsls(player_choice): 
   
    print "Player chooses",player_choice
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    comp_name=number_to_name(comp_number)
    print "Computer chooses",comp_name
    result=(comp_number-player_number)%5
    
    if result==2 or result==1:
        print "Computer wins!"
    elif result==0:
        print "Player and computer tie!"
    else:
        print "Player wins!"
    print ""

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
