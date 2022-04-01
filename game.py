from math import remainder
import random


decisions = {
    '0' : 'Rock',
    '1' : 'Paper',
    '2' : 'Scissor'
}

while True:
    computer = random.choice(list(decisions.values()))