import random

# Bids for short, medium, and long depending on the current positions
# Bid is proportional to the amount of funds left

def evensteven(pos, funds, dist):
    # Is only one left?  If so, spend all remaining money on long
    if pos[0] == 100 and pos[1] == 100:
        return [['short',0],['medium',0],['long', funds[0]]]
    if pos[0] == 100 and pos[2] == 100:
        return [['short',0],['long',funds[0]],['medium', 0]]
    if pos[1] == 100 and pos[2] == 100:
        return [['long',funds[0]],['medium',0],['short', 0]]

    
    # Determine sum of distances left to go
    distancetogo = 300 - (pos[0] + pos[1] + pos[2])
    
    # Determine ratios (but don't let them be greater than one)
    ratioshort = min(1,(dist[0]/distancetogo))
    ratiomedium = min(1, (dist[1]/distancetogo))
    ratiolong = min(1, (dist[2]/distancetogo))
    
    # Determine amounts to spend
    spendshort = min(funds[0],int(ratioshort * funds[0]))
    spendmedium = min(funds[0],int(ratiomedium * funds[0]))
    spendlong = min(funds[0],int(ratiolong * funds[0]))

    # Multipliers so that we don't spend money on ones that are done
    if pos[0] == 100:
        dz = 0
    else:
        dz = 1
    if pos[1] == 100:
        do = 0
    else:
        do = 1
    if pos[2] == 100:
        dt = 0
    else:
        dt = 1
    
    if pos[0] >= pos[1] and pos[0] >= pos[2]:
        if pos[1] >= pos[2]:    # Order 0 > 1 > 2
            return [['short', spendshort*dz],['medium', spendmedium*do],['long', spendlong*dt]]
        else:                   #  Order 0 > 2 > 1
            return [['short', spendshort*dz],['long', spendlong*do],['medium', spendmedium*dt]]

    elif pos[1] >= pos[0] and pos[1] >= pos[2]:
        if pos[0] >= pos[2]:    # Order 1 > 0 > 2
            return [['medium', spendmedium*dz],['short', spendshort*do],['long', spendlong*dt]]
        else:                   #  Order 1 > 2 > 0
            return [['long', spendlong*dz],['short', spendshort*do],['medium', spendmedium*dt]]

    else:
        if pos[0] >= pos[1]:    # Order 2 > 0 > 1
            return [['medium', spendmedium*dz],['long', spendlong*do],['short', spendshort*dt]]
        else:                   # Order 2 > 1 > 0
            return [['long', spendlong*dz],['medium', spendmedium*do],['short', spendshort*dt]]


        
# Only bids for long 34 or over, and for the runner that is behind
# Bid is proportional to the amount of funds left.

def mrbig(pos, funds, dist):
    # Bid a small amount if the long is less than 33--need to get there in three turns!
    #   (assume we won't get 3 33s!)
    if dist[2] < 33:
        thelist = [['long',1000],['short',0],['medium',0]]
        random.shuffle(thelist)
        return thelist
        
    # Determine amount to spend
    distancetogo = 300 - pos[0] - pos[1] - pos[2]
    ratio = dist[2]/distancetogo
    amounttospend = min(funds[0],int(ratio * funds[0]))

    #  Randomize move if they are all at the start
    if pos[0] == pos[1] and pos[1] == pos[2]:
        thelist = [['long', amounttospend],['short',0],['medium',0]]
        random.shuffle(thelist)
        return thelist
    
    # pos[0] is behind
    if pos[0] <= pos[1] and pos[0] <= pos[2]:
        return [['long', amounttospend],['short',0],['medium',0]]

    # pos[1] is behind
    elif pos[1] <= pos[0] and pos[1] <= pos[2]:
        return [['short',0],['long', amounttospend],['medium',0]]

    # pos[2] is behind
    else:
        return [['short',0],['medium',0],['long', amounttospend]]

# Position 0 only short, position 1 only medium, position 2 only long
# Only purchase if big enough

def SML(pos, funds, dist):
    
    # Determine sum of distances left to go
    distancetogo = 300 - (pos[0] + pos[1] + pos[2])
    
    # Determine ratios (but don't let them be greater than one)
    ratioshort = min(1,(dist[0]/distancetogo))
    ratiomedium = min(1, (dist[1]/distancetogo))
    ratiolong = min(1, (dist[2]/distancetogo))
    
    # Determine amounts to spend
    spendshort = min(funds[0],int(ratioshort * funds[0]))
    spendmedium = min(funds[0],int(ratiomedium * funds[0]))
    spendlong = min(funds[0],int(ratiolong * funds[0]))

    # Create preliminary list
    thelist = [['short', spendshort],['medium', spendmedium],['long', spendlong]]

    # Make a small bid if too small
    if dist[2] < 33 or pos[2] == 100:
        thelist[2][1] = 1000
    if dist[1] < 24 or pos[1] == 100:
        thelist[1][1] = 1000
    if dist[0] < 16 or pos[0] == 100:
        thelist[0][1] = 1000

    return thelist
    
        
    
    
