def sniper(pos,funds,dist):
    from random import randint

    # main part: sniper is the 3rd (2nd index) runner (bets on 33, 34, 35)
    
    if (33 <= dist[2] <= 35):
        bid0 = ['short', (3100+randint(-7, 7))*dist[0]]
        bid1 = ['medium', (3100+randint(-7, 7))*dist[1]]
        bid2 = ['long', 116655 + randint(-117, 117)] # 119988 for 36
    if (30 <= dist[2] <= 32):
        bid0 = ['short', (3100+randint(-7, 7))*dist[0]]
        bid1 = ['long', (3100+randint(-7, 7))*dist[1]]
        bid2 = ['medium', randint(0, 117)]
    if (36 <= dist[2] <= 39):
        bid0 = ['long', (3100+randint(-7, 7))*dist[0]]
        bid1 = ['medium', (3100+randint(-7, 7))*dist[1]]
        bid2 = ['short', randint(0, 117)]

    # end-of-game part: refinements to spend money optimally at the end
        
    done = [0, 0, 0]
    if (pos[1] == 100):
        bid1[1] = 0
        done[1] = 1
    elif (pos[1] + dist[0] >= 100):
        bid0, bid1 = bid1, bid0
        if bid1[0] != 'short':
            bid1 = ['short', (3100+randint(-5, 7))*dist[0]]
    if (pos[0] == 100):
        bid0[1] = 0
        done[0] = 1
    if (pos[2] == 100):
        bid2[1] = 0
        done[2] = 1
    if sum(done) == 2:
        u = -1
        for i in range(3):
            if done[i] == 0:
                u = i
        if (pos[u] + dist[0] >= 100):
            bidend = ['short', funds[0]]
        elif (pos[u] + dist[1] >= 100):
            bidend = ['medium', funds[0]]
        elif (pos[u] + dist[2] >= 100):
            bidend = ['long', funds[0]]
        elif (pos[u] + dist[2] >= 70):
            bidend = ['long', funds[0]/2]
        elif (pos[u] + dist[2] >= 40):
            bidend = ['long', funds[0]/3]
        if u == 0:
            bid0 = bidend
        if u == 1:
            bid1 = bidend
        if u == 2:
            bid2 = bidend

    # send bids
    
    bids = [bid0,bid1,bid2]
    return bids

def antisniper(pos,funds,dist):

    # end-of-game part: try to get the first runner as high as possible
    
    if pos[1] == 100 and pos[2] == 100:
        if (pos[0] + dist[0] >= 100):
            bid0 = ['short', funds[0]]
        elif (pos[0] + dist[1] >= 100):
            bid0 = ['medium', funds[0]]
        elif (pos[0] + dist[2] >= 100):
            bid0 = ['long', funds[0]]
        elif (pos[0] + dist[2] >= 70):
            bid0 = ['long', funds[0]/2]
        elif (pos[0] + dist[2] >= 40):
            bid0 = ['long', funds[0]/3]
        else:
            bid0 = ['medium', funds[0]/4]
        bid1 = ['short', 0]
        bid2 = ['short', 0]
    else:

        # main part: get 2nd and 3rd runner in 1st-3rd place, hopefully
        
        bid0 = ['short', 1800*dist[0]]
        if pos[1] + dist[0] < 100:
            bid1 = ['medium', 3800*dist[1]]
        else:
            bid1 = ['short', 3800*dist[0]*(pos[1] < 100)]
        if pos[2] + dist[0] < 100:
            bid2 = ['long', 3800*dist[2]]
        else:
            bid2 = ['short', 3800*dist[0]*(pos[2] < 100)]

   # send bids
    
    bids = [bid0,bid1,bid2]
    return bids
