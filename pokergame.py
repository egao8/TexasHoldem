import random
import time
title = "╔══════════════════════════╗\n\n♧ WELCOME TO TEXAS HOLD'EM ♤\n\n╚══════════════════════════╝"
CARDS = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2] #Used to process hand rankings
HOUSE = ["Spades", "Hearts", "Clubs", "Diamonds"] #Used to process hand rankings
highestCard = [] #Used for only the highcard function
lowestCard = [] #Used only for the highcard function
poker_handVal = [] #A list of a certain player's final best hand
poker_handHouse = [] #A list of the houses for those cards above
handAndRiverVal = [] #A list of the players hand and the dealers cards in one
handAndRiverHouse = [] #above


def waiting():
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)

conversations = [
    "Good luck...you'll need it.", 
    "Hope I don't hurt your feelings too hard.", 
    "I feel lucky today!", 
    "It's second nature at this point, hot damn!", 
    "Let's wrap this one up and head home.",
    "If there weren’t luck involved, I would win every time.",
    "Try me kid. Last person that did lost 10 grand.",
    "You've got potential, just not in this game.",
    "I'll give you the chance to fold right now, c'mon...",
    "Oooh! My cards are looking almost too good!",
    "Wow! My hand's terrible! >:()",
    "I've got so much money!",
    "I'm Loris, baby!",
    "You've fallen right for my trap! >:)",
    "This deck is bustin respectfully."
]

deck_of_52 = [ #Used solely for picking a random card
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
]

deckHouse_of_52 = [ #Used only for picking a random card
    'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 
    'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 
    'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs',
    'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 
] #in hindsight could probably use a for loop instead of this but cant be bothered anymore

def resetdeck(): #Resetting the deck of 52 each round
    global deck_of_52
    global deckHouse_of_52
    deck_of_52 = [
        2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    ]
    deckHouse_of_52 = [
        'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 'Spades', 
        'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 'Hearts', 
        'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs', 'Clubs',
        'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 'Diamonds', 
    ]
    you.handVal = []
    you.handHouse = []
    loris.handVal = []
    loris.handHouse = []
    dealer.handVal = []
    dealer.handHouse = []

CARDSDICT = {14: "Ace", #Used only for printing outputs (specifically playerdraw())
        13: "King",
        12: "Queen",
        11: "Jack",
        10: '10',
        9: '9',
        8: '8',
        7: '7',
        6: '6',
        5: '5',
        4: '4',
        3: '3',
        2: '2',                
} 

class Play: #Class containing hand rankings, draw's, and currency

    def __init__(self, name): #Create variables
        self.name = name
        self.conversation = None
        self.chips = 0
        self.stack = 0
        self.handVal = []
        self.handHouse = []
        self.poker_handVal = []
        self.poker_handHouse = []
        self.handRank = None
        self.handPoints = None

    def setconversation(self): #to set the conversation # will use in future for dialogue to add life to game
        self.conversation = conversations

    def talk(self): #to talk to you adversary #check above
        if self.conversation is not None:
            print("[" + self.name + " says]: " + random.choice(self.conversation))
        else:
            print(self.name + " doesn't want to talk to you")

    def playerdraw(self, numberofcards): #for dealer and player, draws x cards and puts them in a list handVal
        time.sleep(0.8)
        print(self.name + " is now shuffling, \n----------------------------------------")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print("..")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print(self.name + " has: ")
        for i in range(numberofcards): #number of times via parameters
            k = random.randint(0, (len(deck_of_52) - 1)) # setting a variable for the card assigning so we can pop it
            card = (deck_of_52[k]) #Card = A random index value of k in the deck of 52.
            deck_of_52.pop(k) #Remove that value as in a real game
            suit = (deckHouse_of_52[k]) 
            deckHouse_of_52.pop(k)
            self.handVal.append(card) #Put these random draws in a list for safekeeping.
            self.handHouse.append(suit)
        for v in range(len(self.handVal)):
            index = v
            print(str(CARDSDICT[self.handVal[index]]) + ' of ' + str(self.handHouse[index]))
        print("")

    def lorisdraw(self, numberofcards): #exclusive for loris so it doesnt show his cards
        time.sleep(0.8)
        print(self.name + " is now shuffling, \n----------------------------------------")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print("..")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        for i in range(numberofcards):
            k = random.randint(0, (len(deck_of_52) - 1))
            card = (deck_of_52[k]) #listname[]
            deck_of_52.pop(k)
            suit = (deckHouse_of_52[k])
            deckHouse_of_52.pop(k)
            self.handVal.append(card)
            self.handHouse.append(suit)
        print(self.name + " drew their hand.")


    def setchips(self, chips): #sets chips 
        self.chips = chips
    
    def getchips(self): #returns amo. of chips
        return self.chips
    
    def chipsgive(self, number_of_chips): #grants or takes amount of chips
        self.chips += number_of_chips

    #hand rankings
    def is_straightflush(self):
        self.poker_handVal = []
        self.poker_handHouse = []
        if self.is_flush() == True: #check if flush first
            streak = 0
            for i in CARDS:
                if i in self.poker_handVal:
                    streak += 1
                else:
                    streak = 0
                if streak == 5:
                    return(True)
            return(False)
        else:
            return False

    def is_foak(self):
        self.poker_handVal = []
        self.poker_handHouse = []
        handAndRiverVal = self.handVal + dealer.handVal
        handAndRiverHouse = self.handHouse + dealer.handHouse
        for i in CARDS: #for every card,
            if handAndRiverVal.count(i) == 4: #if there are 4 i's/cards that are the same in that list
                for k in range(4): #we run the code 4 times
                    index = handAndRiverVal.index(i) #we find the index of i/card and then,
                    self.poker_handVal.append(handAndRiverVal[index]) #we append the value at that index in the handandriver list to the new list
                    self.poker_handHouse.append(handAndRiverHouse[index]) #same
                    handAndRiverVal.remove(handAndRiverVal[index]) #then we remove that value from the old list
                    handAndRiverHouse.remove(handAndRiverHouse[index])
                for y in range(1):
                    index2 = handAndRiverVal.index(max(handAndRiverVal)) #here we basically add the highest card in that river+hand to make 5 cards
                    self.poker_handVal.append(handAndRiverVal[index2])
                    handAndRiverVal.remove(handAndRiverVal[index2])
                    self.poker_handHouse.append(handAndRiverHouse[index2])
                    handAndRiverHouse.remove(handAndRiverHouse[index2])
                return True
        return False

    def is_fullhouse(self):
        self.poker_handVal = []
        self.poker_handHouse = []
        handAndRiverVal = self.handVal + dealer.handVal
        handAndRiverHouse = self.handHouse + dealer.handHouse
        for i in CARDS:
            if handAndRiverVal.count(i) == 3:
                for g in CARDS:
                    if handAndRiverVal.count(g) == 2 and not g == i:
                        for k in range(3):
                            index = handAndRiverVal.index(i)
                            self.poker_handVal.append(handAndRiverVal[index])
                            self.poker_handHouse.append(handAndRiverHouse[index])
                            handAndRiverVal.remove(handAndRiverVal[index])
                            handAndRiverHouse.remove(handAndRiverHouse[index])
                        for k in range(2):
                            index = handAndRiverVal.index(g)
                            self.poker_handVal.append(handAndRiverVal[index])
                            self.poker_handHouse.append(handAndRiverHouse[index])
                            handAndRiverVal.remove(handAndRiverVal[index])
                            handAndRiverHouse.remove(handAndRiverHouse[index])
                        return True
        return False

    def is_flush(self):
        pLoop = -1 #ploop counts the number of loops in the p loop, nessesary to append the right card to the list
        self.poker_handVal = [] #value of the hand's numerical value
        self.poker_handHouse = [] #whereas handhouse is the value of the hand's house!
        handAndRiverVal = [] #creating empty lists so that variable is init. and defined as a list
        handAndRiverHouse = [] #above
        handAndRiverVal = self.handVal + dealer.handVal #is the player's hand + the dealer as they share for combos
        handAndRiverHouse = self.handHouse + dealer.handHouse #same as above but this is for houses!
        for i in HOUSE: #checks for a flush with every flush
            if handAndRiverHouse.count(i) >= 5:
                for p in handAndRiverHouse:
                    pLoop += 1 #see above
                    if p == i:
                        self.poker_handVal.append(handAndRiverVal[pLoop])
                while len(poker_handVal) > 5:
                    self.poker_handVal.remove(min(self.poker_handVal))
                for o in range(5):
                    self.poker_handHouse.append(i)
                return(True) #return true simply means that it was indeed a flush!
        return(False)
            #check if 5 of the cards are same house

    def is_straight(self):
        self.poker_handVal = []
        self.poker_handHouse = []
        handAndRiverVal = []
        streak = 0
        handAndRiverVal = self.handVal + dealer.handVal
        for i in CARDS:
            if i in handAndRiverVal:
                streak += 1
                self.poker_handVal.append(i)
                self.poker_handHouse.append(i)
            else:
                streak = 0
                self.poker_handVal = []
            if streak == 5:
                return(True)
        self.poker_handVal = []
        self.poker_handHouse = []
        return(False)

    def is_toak(self):
        self.poker_handVal = []
        self.poker_handHouse = []
        handAndRiverVal = self.handVal + dealer.handVal
        handAndRiverHouse = self.handHouse + dealer.handHouse
        for i in CARDS:
            if handAndRiverVal.count(i) == 3:
                for k in range(3):
                    index = handAndRiverVal.index(i)
                    self.poker_handVal.append(handAndRiverVal[index])
                    self.poker_handHouse.append(handAndRiverHouse[index])
                    handAndRiverVal.remove(handAndRiverVal[index])
                    handAndRiverHouse.remove(handAndRiverHouse[index])
                for y in range(2):
                    index2 = handAndRiverVal.index(max(handAndRiverVal))
                    self.poker_handVal.append(handAndRiverVal[index2])
                    handAndRiverVal.remove(handAndRiverVal[index2])
                    self.poker_handHouse.append(handAndRiverHouse[index2])
                    handAndRiverHouse.remove(handAndRiverHouse[index2])
                return True
        return False

    def is_twopair(self):
        self.poker_handVal = []
        self.poker_handHouse = []
        handAndRiverVal = self.handVal + dealer.handVal
        handAndRiverHouse = self.handHouse + dealer.handHouse
        for i in CARDS:
            if handAndRiverVal.count(i) == 2:
                for g in CARDS:
                    if handAndRiverVal.count(g) == 2 and not g == i:
                        for k in range(2):
                            index = handAndRiverVal.index(i)
                            self.poker_handVal.append(handAndRiverVal[index])
                            self.poker_handHouse.append(handAndRiverHouse[index])
                            handAndRiverVal.remove(handAndRiverVal[index])
                            handAndRiverHouse.remove(handAndRiverHouse[index])
                        for k in range(2):
                            index = handAndRiverVal.index(g)
                            self.poker_handVal.append(handAndRiverVal[index])
                            self.poker_handHouse.append(handAndRiverHouse[index])
                            handAndRiverVal.remove(handAndRiverVal[index])
                            handAndRiverHouse.remove(handAndRiverHouse[index])
                        for y in range(1):
                            index2 = handAndRiverVal.index(max(handAndRiverVal))
                            self.poker_handVal.append(handAndRiverVal[index2])
                            handAndRiverVal.remove(handAndRiverVal[index2])
                            self.poker_handHouse.append(handAndRiverHouse[index2])
                            handAndRiverHouse.remove(handAndRiverHouse[index2])
                        return True
        return False

    def is_pair(self):
        self.poker_handVal = []
        self.poker_handHouse = []
        handAndRiverVal = self.handVal + dealer.handVal
        handAndRiverHouse = self.handHouse + dealer.handHouse
        for i in CARDS:
            if handAndRiverVal.count(i) == 2:
                for k in range(2):
                    try:
                        index = handAndRiverVal.index(i)
                        self.poker_handVal.append(handAndRiverVal[index])
                        self.poker_handHouse.append(handAndRiverHouse[index])
                        handAndRiverVal.remove(handAndRiverVal[index])
                        handAndRiverHouse.remove(handAndRiverHouse[index])
                    except:
                        pass
                for y in range(3):
                    try:
                        index2 = handAndRiverVal.index(max(handAndRiverVal))
                        self.poker_handVal.append(handAndRiverVal[index2])
                        handAndRiverVal.remove(handAndRiverVal[index2])
                        self.poker_handHouse.append(handAndRiverHouse[index2])
                        handAndRiverHouse.remove(handAndRiverHouse[index2])
                    except:
                        pass
                return True
        return False

    def handeval(self):
        self.poker_handVal = []
        self.poker_handHouse = []
        handAndRiverVal = []
        handAndRiverHouse = []
        handAndRiverVal = self.handVal + dealer.handVal
        handAndRiverHouse = self.handHouse + dealer.handHouse
        if self.is_straightflush() == True:
            self.handRank = 'straight flush'
            self.handPoints = 800
        elif self.is_foak():
            self.handRank = 'four of a kind'
            self.handPoints = 700
        elif self.is_fullhouse():
            self.handRank = 'full house'
            self.handPoints = 600
        elif self.is_flush():
            self.handRank = 'flush'
            self.handPoints = 500
        elif self.is_straight():
            self.handRank = 'straight'
            self.handPoints = 400
        elif self.is_toak():
            self.handRank = 'three of a kind'
            self.handPoints = 300
        elif self.is_twopair():
            self.handRank = 'two pair'
            self.handPoints = 200
        elif self.is_pair():
            self.handRank = 'pair'
            self.handPoints = 100
        else:
            self.handRank = 'high card'
            self.handPoints = 0
            for i in range(5):
                try:
                    index2 = handAndRiverVal.index(max(handAndRiverVal))
                    self.poker_handVal.append(handAndRiverVal[index2])
                    handAndRiverVal.remove(handAndRiverVal[index2])
                    self.poker_handHouse.append(handAndRiverHouse[index2])
                    handAndRiverHouse.remove(handAndRiverHouse[index2])
                except:
                    pass

    

def winner(): #highcard handranking check
    you.handeval()
    loris.handeval()
    copyyoupoker_handVal = you.poker_handVal #copies are made to keep the value of poker_handval the same but have the
    copylorispoker_handVal = loris.poker_handVal # freedom to edit them knowing it wont poop on other areas
    while you.handPoints == loris.handPoints: #while there is no definitive winner (either by no higher rankings or same h.r)
        if not len(copyyoupoker_handVal) == 0:
            index = copyyoupoker_handVal.index(max(copyyoupoker_handVal))
            index2 = copylorispoker_handVal.index(max(copylorispoker_handVal))
            you.handPoints += copyyoupoker_handVal[index] #add the highest card to the players score
            copyyoupoker_handVal.remove(copyyoupoker_handVal[index]) #then remove that card from the list
            loris.handPoints += copylorispoker_handVal[index2] #same as 360 and 361
            copylorispoker_handVal.remove(copylorispoker_handVal[index2])
        else:
            return('tie')
    if you.handPoints > loris.handPoints: #compare to see whos hand is bigger 
        return('you')
    else:
        return('loris')
        

#just creating the objects
dealer = Play("Dealer")
you = Play("Player")
loris = Play("Loris")
players = [you, loris]
bigBlind = 20


def chask():    
    global prm
    global aiOutput
    while True:
        time.sleep(1)
        print("Your hand is: ")
        for v in range(len(you.handVal)):
            index = v
            print(str(CARDSDICT[you.handVal[index]]) + ' of ' + str(you.handHouse[index])) #Print it so we know what it is.
        time.sleep(1)
        print("You have " + str(you.stack) + " chips in your stack while Loris has " + str(loris.stack) + ".")
        time.sleep(1)
        print("You have " + str(you.chips) + " chips while Loris has " + str(loris.chips) + ".")
        time.sleep(1)
        if aiOutput == 'all in':
            x = input("Would you like to call Loris's all in? (Y/N): ").lower()
            if x == 'y':
                print("Risky choice!")
                time.sleep(1)
                print("[Loris says]: You got guts kid!")
                if you.stack + you.chips > loris.stack:
                    you.chips -= loris.stack
                    you.stack = loris.stack
                else:
                    you.stack += you.chips
                    you.chips = 0
                    
                return "all in"
            elif x == 'n':
                print("[Loris says]: Never pegged ya for a quitter...")
                time.sleep(1)
                return "fold"
                
        else:
            x = input('Fold, check/call or raise? ').lower() #XD LMAO  
            if x == "raise":
                rm = input("How much do you want to raise? ").lower()
                try:
                    rm = int(rm)
                    if rm <= you.chips:
                        if rm <= loris.chips:
                            if rm == you.chips:
                                while True:
                                    time.sleep(0.5)
                                    f = input('You would be going all in. Are you sure? (Y/N): ').lower()
                                    if f == 'y':
                                        print("All in it is!")
                                        you.chips -= loris.stack - you.stack
                                        you.stack = loris.stack
                                        if you.chips > loris.chips:
                                            g = loris.chips - you.stack
                                            you.chips -= g
                                            you.stack += g
                                        else:
                                            you.stack += you.chips
                                            you.chips = 0
                                        time.sleep(1)
                                        return 'all in'
                                    elif f == 'n':
                                        break
                                continue
                            else:
                                if prm <= rm:
                                    you.chips -= loris.stack - you.stack
                                    you.stack = loris.stack
                                    you.chips -= rm
                                    you.stack += rm
                                    prm = rm
                                    break
                                else:
                                    time.sleep(1)
                                    print('Raise amount must be at least the previous raise amount (' + str(prm) + ')')
                                    continue
                        elif input('You can\'t raise to more than what Loris has! Would you like to raise by ' + str(loris.chips - you.stack) + ' chips (all in)? Y/N: ').lower() == 'y':
                            g = loris.chips - you.stack
                            you.chips -= g
                            you.stack += g
                            prm = g
                            print("You've gone all in!")
                            time.sleep(1)
                            
                            return('all in')
                        else:
                            continue
                    else:
                        time.sleep(1)
                        print('Insufficient funds.')
                        continue
                except:
                    if rm == 'all in':
                        time.sleep(1)
                        print("All in it is!")
                        you.chips -= loris.stack - you.stack
                        you.stack = loris.stack
                        if you.chips > loris.chips:
                            g = loris.chips - you.stack
                            you.chips -= g
                            you.stack += g
                        else:
                            you.stack += you.chips
                            you.chips = 0
                        time.sleep(1)
                        return 'all in'
                    else:
                        print("not a int")
                        continue

            elif x == 'fold':
                print("You've folded your cards.")
                return 'fold'
            
            elif x == 'check' or x == 'call' or x == 'check/call':
                if you.stack >= loris.stack:
                    print('You have checked.')
                else:
                    you.chips -= loris.stack - you.stack
                    you.stack = loris.stack
                    print('You have called.')
                break
                
                    
            else:
                print("Not a valid option. Try again!")
                continue

def ai():
    decision = None
    loris.handeval()
    loris.handPoints += max(loris.poker_handVal)
    rng = random.randint(1, 1000)
    #X
    if chaskOutput == 'all in':
        allinrng = random.randint(1, 100)
        chance = 91 #91% chance we fold if its high card only
        if loris.handPoints >= 200: 
            chance = 85
        if loris.handPoints >= 300:
            chance = 72
        if loris.handPoints >= 400:
            chance = 56
        if loris.handPoints >= 500: 
            chance = 39
        if loris.handPoints >= 600:
            chance = 28
        if loris.handPoints >= 700:
            chance = 19
        if loris.handPoints >= 800:
            chance = 1
        
        if allinrng <= chance: #arbitrary number for when loris has only high card
            waiting()
            print("Loris has folded his cards.")
            return 'fold' #fold nothin hapens
        else:
            waiting()
            print("Loris has also gone all in!")
            if loris.stack + loris.chips > you.stack:
                loris.chips -= you.stack
                loris.stack = you.stack
            else:
                loris.stack += loris.chips
                loris.chips = 0
            return 'all in'
    while True:
        if loris.stack == you.stack: #code to check
            if 1 <= loris.handPoints <= 99: #high card
                if 1 <= rng <= 925:
                    decision = 'check'
                    break
                elif 926 <= rng <= 995:
                    decision = 'small raise'
                    break
                elif 996 <= rng <= 1000:
                    decision = 'big raise'
                    break
            if 100 <= loris.handPoints <= 199: #pair
                if 1 <= rng <= 650:
                    decision = 'check'
                    break
                elif 651 <= rng <= 950:
                    decision = 'small raise'
                    break
                elif 951 <= rng <= 1000:
                    decision = 'big raise'
                    break
            if 200 <= loris.handPoints <= 299: #2pair
                if 1 <= rng <= 350:
                    decision = 'check'
                    break
                elif 351 <= rng <= 919:
                    decision = 'small raise'
                    break
                elif 920 <= rng <= 1000:
                    decision = 'big raise'
                    break
            if 300 <= loris.handPoints <= 399:
                if 1 <= rng <= 230:
                    decision = 'check'
                    break
                elif 231 <= rng <= 800:
                    decision = 'small raise'
                    break
                elif 801 <= rng <= 1000:
                    decision = 'big raise'
                    break
            if 400 <= loris.handPoints <= 499:
                if 1 <= rng <= 198:
                    decision = 'check'
                    break
                elif 199 <= rng <= 700:
                    decision = 'small raise'
                    break
                elif 701 <= rng <= 1000:
                    decision = 'big raise'
                    break
            if 500 <= loris.handPoints <= 599:
                if 1 <= rng <= 160:
                    decision = 'check'
                    break
                elif 161 <= rng <= 625:
                    decision = 'small raise'
                    break
                elif 626 <= rng <= 1000:
                    decision = 'big raise'
                    break
            if 600 <= loris.handPoints <= 699:
                if 1 <= rng <= 140:
                    decision = 'check'
                    break
                elif 141 <= rng <= 550:
                    decision = 'small raise'
                    break
                elif 551 <= rng <= 1000:
                    decision = 'big raise'
                    break
            if 700 <= loris.handPoints <= 799:
                if 1 <= rng <= 100:
                    decision = 'check'
                    break
                elif 101 <= rng <= 480:
                    decision = 'small raise'
                    break
                elif 481 <= rng <= 1000:
                    decision = 'big raise'
                    break
            if 800 <= loris.handPoints <= 814:
                if 1 <= rng <= 90:
                    decision = 'check'
                    break
                elif 91 <= rng <= 420:
                    decision = 'small raise'
                    break
                elif 421 <= rng <= 1000:
                    decision = 'big raise'
                    break
        #---------------------------------------------
        if you.stack - loris.stack <= 50: #if difference in stacks is not quite large
            if 1 <= loris.handPoints <= 99: #high card
                if 1 <= rng <= 839:
                    decision = 'check'
                    break
                elif 840 <= rng <= 901:
                    decision = 'small raise'
                    break
                elif 902 <= rng <= 909:
                    decision = 'big raise'
                    break
                elif 910 <= rng <= 1000:
                    decision = 'fold'
                    break
            if 100 <= loris.handPoints <= 199: #pair
                if 1 <= rng <= 700:
                    decision = 'check'
                    break
                elif 701 <= rng <= 950:
                    decision = 'small raise'
                    break
                elif 951 <= rng <= 984:
                    decision = 'big raise'
                    break
                elif 985 <= rng <= 1000:
                    decision = 'fold'
                    break
            if 200 <= loris.handPoints <= 299: #2pair
                if 1 <= rng <= 525:
                    decision = 'check'
                    break
                elif 526 <= rng <= 919:
                    decision = 'small raise'
                    break
                elif 920 <= rng <= 988:
                    decision = 'big raise'
                    break
                elif 989 <= rng <= 1000:
                    decision = 'fold'
                    break
            if 300 <= loris.handPoints <= 399:
                if 1 <= rng <= 250:
                    decision = 'check'
                    break
                elif 251 <= rng <= 800:
                    decision = 'small raise'
                    break
                elif 801 <= rng <= 995:
                    decision = 'big raise'
                    break
                elif 996 <= rng <= 1000:
                    decision = 'fold'
                    break
            if 400 <= loris.handPoints <= 499:
                if 1 <= rng <= 198:
                    decision = 'check'
                    break
                elif 199 <= rng <= 700:
                    decision = 'small raise'
                    break
                elif 701 <= rng <= 1000:
                    decision = 'big raise'
                    break
                elif 1000 <= rng <= 1000: #would a real player ever fold a straight when the stack diff is <50?
                    decision = 'fold'
                    break
            if 500 <= loris.handPoints <= 599:
                if 1 <= rng <= 140:
                    decision = 'check'
                    break
                elif 141 <= rng <= 625:
                    decision = 'small raise'
                    break
                elif 626 <= rng <= 1000:
                    decision = 'big raise'
                    break
                #elif 996 <= rng <= 1000:
                    #decision = 'fold'
            if 600 <= loris.handPoints <= 699:
                if 1 <= rng <= 140:
                    decision = 'check'
                elif 141 <= rng <= 550:
                    decision = 'small raise'
                    break
                elif 551 <= rng <= 1000:
                    decision = 'big raise'
                    break
                #elif 996 <= rng <= 1000:
                    #decision = 'fold'
            if 700 <= loris.handPoints <= 799:
                if 1 <= rng <= 100:
                    decision = 'check'
                    break
                elif 101 <= rng <= 480:
                    decision = 'small raise'
                    break
                elif 481 <= rng <= 1000:
                    decision = 'big raise'
                    break
                #elif 996 <= rng <= 1000:
                    #decision = 'fold'
            if 800 <= loris.handPoints <= 814:
                if 1 <= rng <= 90:
                    decision = 'check'
                    break
                elif 91 <= rng <= 420:
                    decision = 'small raise'
                    break
                elif 421 <= rng <= 1000:
                    decision = 'big raise'
                    break
    #-----------------------------------------------
        if you.stack - loris.stack >= 50: #if difference in stacks is quite large
            if 1 <= loris.handPoints <= 99: #high card
                if 1 <= rng <= 650:
                    decision = 'check'
                    break
                elif 651 <= rng <= 700:
                    decision = 'small raise'
                    break
                elif 701 <= rng <= 720:
                    decision = 'big raise'
                    break
                elif 721 <= rng <= 1000:
                    decision = 'fold'
                    break
            if 100 <= loris.handPoints <= 199: #pair
                if 1 <= rng <= 720:
                    decision = 'check'
                    break
                elif 721 <= rng <= 749:
                    decision = 'small raise'
                    break
                elif 750 <= rng <= 790:
                    decision = 'big raise'
                    break
                elif 791 <= rng <= 1000:
                    decision = 'fold'
                    break
            if 200 <= loris.handPoints <= 299: #2pair
                if 1 <= rng <= 450:
                    decision = 'check'
                    break
                elif 451 <= rng <= 699:
                    decision = 'small raise'
                    break
                elif 700 <= rng <= 849:
                    decision = 'big raise'
                    break
                elif 850 <= rng <= 1000:
                    decision = 'fold'
                    break
            if 300 <= loris.handPoints <= 399:
                if 1 <= rng <= 300:
                    decision = 'check'
                    break
                elif 301 <= rng <= 800:
                    decision = 'small raise'
                    break
                elif 801 <= rng <= 989:
                    decision = 'big raise'
                    break
                elif 990 <= rng <= 1000:
                    decision = 'fold'
                    break
            if 400 <= loris.handPoints <= 499:
                if 1 <= rng <= 275:
                    decision = 'check'
                    break
                elif 199 <= rng <= 700:
                    decision = 'small raise'
                    break
                elif 701 <= rng <= 993:
                    decision = 'big raise'
                    break
                elif 994 <= rng <= 1000:
                    decision = 'fold'
                    break
            if 500 <= loris.handPoints <= 599:
                if 1 <= rng <= 180:
                    decision = 'check'
                    break
                elif 181 <= rng <= 625:
                    decision = 'small raise'
                    break
                elif 626 <= rng <= 998:
                    decision = 'big raise'
                    break
                elif 999 <= rng <= 1000:
                    decision = 'fold'
                    break
            if 600 <= loris.handPoints <= 699:
                if 1 <= rng <= 140:
                    decision = 'check'
                    break
                elif 141 <= rng <= 550:
                    decision = 'small raise'
                    break
                elif 551 <= rng <= 998:
                    decision = 'big raise'
                    break
                elif 999 <= rng <= 1000: #would you really fold on a full house??? maybe???
                    decision = 'fold'
                    break
            if 700 <= loris.handPoints <= 799:
                if 1 <= rng <= 100:
                    decision = 'check'
                    break
                elif 101 <= rng <= 480:
                    decision = 'small raise'
                    break
                elif 481 <= rng <= 1000:
                    decision = 'big raise'
                    break
                #elif 996 <= rng <= 1000: #aint no way you folding a four of a kind youd probably challenge an all in
                    #decision = 'fold'
            if 800 <= loris.handPoints <= 814:
                if 1 <= rng <= 30:
                    decision = 'check'
                    break
                elif 31 <= rng <= 350:
                    decision = 'small raise'
                    break
                elif 351 <= rng <= 1000:
                    decision = 'big raise'
                    break

    #------------------------------------------------    
    while True:
        if decision == None:
            pass
        elif decision == 'check':
            if loris.stack >= you.stack:
                waiting()
                print('Loris has checked.')
                return 'check'
            else:
                loris.chips -= you.stack - loris.stack
                loris.stack = you.stack
                waiting()
                print('Loris has called.')
                return 'check'
        elif decision == 'fold':
            waiting()
            print("Loris has folded his cards.")
            return 'fold'
        elif decision == 'small raise':
            lorisRaiseAmount = prm + (random.randint(1, 5) * 10)
            if not loris.chips - lorisRaiseAmount <= 0:
                '''loris.chips -= you.stack - loris.stack
                loris.stack = you.stack'''
                loris.chips -= lorisRaiseAmount
                loris.stack += lorisRaiseAmount
                waiting()
                print("Loris has raised by {} chips.".format(lorisRaiseAmount))
            else:
                decision = 'check'
                continue
        elif decision == 'big raise':
            if not random.randint(1, 100) <= 5:
                lorisRaiseAmount = prm + (random.randint(6, 10) * 10)
                if not loris.chips - lorisRaiseAmount <= 0:
                    #loris.chips -= you.stack - loris.stack
                    #loris.stack = you.stack
                    loris.chips -= lorisRaiseAmount
                    loris.stack += lorisRaiseAmount
                    waiting()
                    print("Loris has raised by {} chips.".format(lorisRaiseAmount))
                else:
                    decision = 'small raise'
                    continue
            else:
                you.chips -= loris.stack - you.stack
                you.stack = loris.stack
                if loris.chips > you.chips:
                    g = you.chips - loris.stack
                    loris.chips -= g
                    loris.stack += g
                else:
                    loris.stack += loris.chips
                    loris.chips = 0               
                print('Loris has gone all in! (his stack is ' + str(loris.stack) + ' chips)')
                return 'all in'
        else:
            continue
        break
    
def allIn():
    global winneR
    if not len(dealer.handVal) == 5:
        dealer.playerdraw(5 - len(dealer.handVal))
    loris.handeval()
    you.handeval()
    winneR = winner()
    

def turn():
    global prm
    global gone
    global pot
    global turnNumber
    global winneR
    global bigBlind
    prm = bigBlind
    global chaskOutput
    global aiOutput
    chaskOutput = None
    aiOutput =  None
    while not (you.stack == loris.stack and gone == True):
        if (turnNumber % 2) == 0:
            chaskOutput = chask()
            if chaskOutput == 'fold': #runs chask() & if chask() is fold then break
                winneR = 'loris'
                break
            elif chaskOutput == 'all in' and aiOutput == 'all in':
                allIn()
                break
            if you.stack == loris.stack and gone == True:
                break
            aiOutput = ai()
            if aiOutput == 'fold': #runs chask() & if chask() is fold then break
                winneR = 'you'
                break
            elif chaskOutput == 'all in' and aiOutput == 'all in':
                allIn()
                break
            gone = True
        else:
            aiOutput = ai()
            if aiOutput == 'fold': #runs chask() & if chask() is fold then break
                winneR = 'you'
                break
            elif chaskOutput == 'all in' and aiOutput == 'all in':
                allIn()
                break
            if you.stack == loris.stack and gone == True:
                break
            chaskOutput = chask()
            if chaskOutput == 'fold': #runs chask() & if chask() is fold then break
                winneR = 'loris'
                break
            elif chaskOutput == 'all in' and aiOutput == 'all in':
                allIn()
                break
            gone = True
    time.sleep(1)
    print("Your stack was " + str(you.stack) + " while Loris's was " + str(loris.stack) + ".")
    pot += you.stack + loris.stack
    time.sleep(1)
    print("The pot is", pot)
    you.stack = 0
    loris.stack = 0
    gone = False

def game():
    global turnNumber
    global bigBlind
    turnNumber = 0
    while not you.chips <= bigBlind and not loris.chips <= bigBlind:
        global prm
        global winneR
        global gone
        global pot
        pot = 0
        prm = bigBlind
        winneR = None
        if turnNumber % 5 == 0 and not turnNumber == 0:
            bigBlind += 20
        you.playerdraw(2)
        loris.lorisdraw(2) 
        time.sleep(0.6)
        loris.setconversation()
        loris.talk()
        gone = False
        if turnNumber % 2 == 0:
            loris.stack = bigBlind
            loris.chips -= bigBlind
            you.stack = bigBlind//2
            you.chips -= bigBlind//2
        else:
            you.stack = bigBlind
            you.chips -= bigBlind
            loris.stack = bigBlind//2
            loris.chips -= bigBlind//2
        turn()
        if winneR == None:
            dealer.playerdraw(3)
            randomness = random.randint(1,2)
            if randomness == 1:
                time.sleep(1)
                loris.talk()
            turn()
        if winneR == None:
            dealer.playerdraw(1)
            turn()
            randomness = random.randint(1,3)
            if randomness == 2:
                time.sleep(1)
                loris.talk()
        if winneR == None:
            dealer.playerdraw(1)
            randomness = random.randint(1,2)
            if randomness == 2:
                time.sleep(1)
                loris.talk()
            turn()
        time.sleep(1)
        print("Loris' hand:")
        for q in range(len(loris.handVal)):
            index = q
            print(str(CARDSDICT[loris.handVal[index]]) + ' of ' + str(loris.handHouse[index])) #Print it so we know what it is.
        if not winneR == None:
            if winneR == 'you': #add pot to you.chips, clear pot, clear stacks, kaboosh
                print("You've won the hand!")
                you.chips += pot
            elif winneR == 'loris':
                print("Loris has won the hand!")
                time.sleep(0.9)
                loris.chips += pot
            else:
                #tie
                print('A tie... this time.')
                you.chips += pot//2
                loris.chips += pot//2
        else:
            if winner() == 'you': #add pot to you.chips, clear pot, clear stacks
                print("You've won the hand!")
                you.chips += pot
            elif winner() == 'loris':
                print("Loris has won the hand!")
                time.sleep(0.9)
                print("ur trash khed!")
                loris.chips += pot
            else:
                #tie
                print('A tie... this time.')
                you.chips += pot//2
                loris.chips += pot//2
        print("You have " + str(you.chips) + " chips while Loris has " + str(loris.chips) + ".")
        
        resetdeck()
        turnNumber += 1 #next round, other person goes first (person that went 2nd this round)
    if you.chips <= bigBlind:
        print("You've lost this match... Try again next time when you have money!")
        time.sleep(1.2)
        print("[Loris says]: Can't say I wasn't surprised, but hey, you got some fight in ya kid.")
    else:
        print("You've beaten Loris, the poker legend! This should've been impossible!")
        time.sleep(1)
        print("Maybe you're the poker elite!")
    time.sleep(60)
    quit()

   
#if everybodies stack is same and everyone has went, next round
#every 5-10 rounds we increase starting bets by just a tad.

#introductory loop. just to make sure player actually wants to play
def start():
    global ifready
    print(title)
    time.sleep(1)
    print("I hope you're ready as you'll be playing against Loris, a poker elite.")
    time.sleep(1.6)
    print("Just know that Loris has never lost a game, you think you can break that streak?")
    time.sleep(1.8)
    print("Good luck...")
    time.sleep(1.2)
    ifready = input("Are you ready to play? (Y or N): ").lower()
    if ifready == "y":
        print("Alright, let's begin!")
        time.sleep(2)
        while True:
            x = input('How many chips would you like to start with?\n(We recommend 500 for a short game, 1000 for a medium game and 1500 for a long one): ')
            try:
                x = int(x)
                you.chips = x
                loris.chips = x
                print("{} chips sounds great!".format(x))
                break
            except:
                print("Not a number, try again?")
                time.sleep(1)
                continue
        print('----------------------------------------\n')
        game() #Y will trigger the game
    else:
        print("I suppose Loris' streak still stands!")
        time.sleep(10)



def ending():
    while True:
        time.sleep(2)
        ending = input("Thanks for finishing the game! Whether you were victorious or fell triumph to Loris, we hope you had a fun time.\n Do know this was merely a fun project between two friends in an effort to learn more about Python, so the code may (and will) be messy.\nLet us know if you liked the game! (Y/N): ")
        if ending == "Y":
            print("Sweet! Thanks for playing.")
            break
        elif ending == "N":
            print("Aw, thanks for playing ):")
            # reloop the entire program regardless of consent
        else:
            continue



start() # starts the game
if ifready == "y" or ifready == "Y":
    ending() # ending message
    time.sleep(1000) 