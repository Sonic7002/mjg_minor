# This class contains utility functions for ui use
import os

def clear_screen():
    """Clears the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    """pauses the program"""
    input("Press enter to continue")
