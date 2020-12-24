#Rock, paper, scissors, lizard, spock
import random

def getChoice():
    while True: 
        hand = input("Please choose Rock, Paper, Scissors, Lizard, Spock: ")
        if hand  in ["Rock", "Paper", "Scissors", "Lizard", "Spock"]:
            return hand

def cpuChoice():
    chooseFrom = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    cpuHand = random.choice(chooseFrom)
    print(f"CPU chose: {cpuHand}")
    return cpuHand

def checkWinner(hand, cpuHand):
    if hand == cpuHand:
       return None # tie = True
    elif hand == "Rock":
        return cpuHand in ["Paper", "Spock"] #returns true or false, if true, you lose
    elif hand == "Paper": 
        return cpuHand in ["Scissors", "Lizard"]
    elif hand == "Lizard": 
        return cpuHand in ["Scissors", "Rock"]
    elif hand == "Spock": 
        return cpuHand in ["Paper", "Lizard"]
    else: #hand == "Scissors"
        return cpuHand in ["Rock", "Spock"]

def displayResult(outcome):
    if outcome is None:
        print("Its a tie")
    elif not outcome: #not 1 in boolean, i.e false
        print("You Win")
    else:
        print("You Lose")

# MAIN PROGRAM
if __name__ == "__main__":
    while True:
        playerChoice = getChoice()
        compChoice = cpuChoice()
        result = checkWinner(playerChoice, compChoice)
        displayResult(result)
        if result is not None:
            break



