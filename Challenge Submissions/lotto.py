import random

def lotto(startnum, stopnum, cnt): 
    return random.sample([*range(startnum,stopnum)],k=cnt)

print(lotto(1,49,6)) 
