#!/bin/python3

import random, pyfiglet, time, enum

choice_table = ['rock', 'paper', 'scissors']

class Game(IntEnum):
    rock = 1 
    paper = 2
    scissors = 3

def rock_paper_scissors():
    player = input(pyfiglet.figlet_format("Hello there! Pick rock [1] paper [2] or scissors [3]!"))
    choice = int(player)
    action = Game.choice
    computer_choice  = random.choice(choice_table)
    return action      
        


rock_paper_scissors()