import os

def clear():
    """Clears all console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')