import random
totalUser=0
totalComputer=0
name=input("Enter you name:")
print(f"----------------Hey {name} Welcome to the game!!-----------------------\n")
print("----------------Aayiye Dekhte hain maja aayega---------------------\n")


def dealCards():  
    cardPoint=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cardPoint)

def sumCards(hand):
    """Calculate the total value of a hand."""
    total = sum(hand)
    # Adjust for Aces
    num_aces = hand.count(11)
    while total > 21 and num_aces:
        total -= 10
        num_aces -= 1
    return total   
        
def game():
    
    play=input("Do you want to play 'y' or 'n' : ")
    if play!='y':
        print("The game is over !")
        return
    userCard=[dealCards(),dealCards()]
    computerChoice=[dealCards(),dealCards()]
    
    totalUser=sumCards(userCard)
    totalComputer=sumCards(computerChoice)
    
    print(f"Dealer in hand is {computerChoice}",totalComputer)
    print(f"Your card in hand is {userCard}", totalUser)
    while totalUser<21:
        choice=input("DO YOU WANT TO TAKE ANOTHER CARD?")
        if choice=='y':
            userCard.append(dealCards())
            totalUser=sumCards(userCard)
            print(f"Your card in hand is {userCard}", totalUser)
            
        elif choice=='n':
            break
        else:
            print("INVALID")
    if totalUser>21:
        print("You busted.The Dealer win!")
    
    
    while totalComputer<17:
        computerChoice.append(dealCards())
        totalComputer=sumCards(computerChoice)
        print(f"Dealer in hand is {computerChoice}",totalComputer)
    if totalComputer >21:
        print(f"Hey {name} !!! You win")
    
if totalComputer==totalUser:
    print("Match Draw\n")
        
    
elif totalUser>totalComputer:
    print(f"Hey {name} You win")
elif totalComputer>totalUser:
    print("Busted...You loose")     
game()