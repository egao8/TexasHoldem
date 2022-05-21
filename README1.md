# Texas Hold'em

May 2021
Auth (Eddie Gao, Kenny Smith)

This is a fully open-source Python-based Texas Hold'em game supporting Python 3 on Windows, Mac and Linux. The game plays out exactly like a traditional Texas Hold'em match in a Player v.s Computer form.


Do know you've the liberty to explore the code and the game itself, though a prior understanding of poker and Texas Hold'em is recommended. In the case that you've never learned the rules and strategy of Texas Hold'em,  [here's a quick rundown on the game.](https://www.wikihow.com/Play-Poker)

## Features

- [x] 52 card deck with different suits and random shuffling
- [x] Calling, raising, and folding system
- [x] Chip system
- [x] Basic Poker game progression
- [x] Interactive text-based gameplay
- [x] Hand detection 
- [x] Hand strength calculation/evaluation
- [x] Determination of winning hands
- [x] All-ins, big blinds, small blinds

## Installation

This program requires no external libraries in need of supplementary download. Simply running the program using Python 3 (with terminal or your preferred IDE/Compiler) will work just fine.

## Examples

Simulating a random shuffle out of a deck of 52.
```
How many chips would you like to start with?
(We recommend 500 for a short game, 1000 for a medium game and 1500 for a long one): 
>>>1000
1000 chips sounds great!
----------------------------------------

Player is now shuffling, 
----------------------------------------
.
..
...
Player has: 
6 of Diamonds
5 of Hearts

```
Simulation of AI (Loris) making decisions based off of hand strength calculation of both his hands and the river...(or could he be bluffing)?
```
You have 990 chips while Loris has 980.
Fold, check/call or raise? 
>>>call
You have called.
Loris has gone all in! (his stack is 1000 chips)
Your hand is: 
6 of Diamonds
5 of Hearts
You have 20 chips in your stack while Loris has 1000.
You have 980 chips while Loris has 0.
Would you like to call Loris's all in? (Y/N): 
>>>y
Risky choice!
[Loris says]: You got guts kid! #dialogue
Dealer is now shuffling, 
----------------------------------------
.
..
...
Dealer has: #Dealer chooses random cards and prints them
Queen of Hearts
Ace of Diamonds
9 of Diamonds
2 of Diamonds
Queen of Spades
```

Function to evaluate straights.
```
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
```

## AI Functionality

The goal when making an artificial intelligence for poker was to resemble a human's behavioural traits, either with logical choices or irrationality. Logical decisions came in the form of evaluating Loris' hand strength each round whereas irrational choices came in the form of bluffing, slowly raising, and convincing dialogue.

