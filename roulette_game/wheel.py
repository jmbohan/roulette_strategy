import random

def spin_wheel():
    """Simulates spinning the roulette wheel."""
    number = random.randint(0, 37)
    color = 'green' if number == 0 or number == 37 else 'red' if number % 2 == 1 else 'black'
    return number if number != 37 else '00', color
