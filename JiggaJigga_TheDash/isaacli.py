def sniper(pos,funds,dist):
    from random import randint

    # main part: sniper is the 3rd (2nd index) runner (bets on 33, 34, 35)

    steady = int(3133+(max(0, min(3*(sum(pos[3:])-sum(3*pos[:2]))/2, 600)))/3) # ...works also for unsustainable paces such as 3400 cpm

    if (33 <= dist[2] <= 36 and dist[2]+pos[2] != 99):
        bid0 = ['short', (steady+randint(-7, 7))*dist[0]]
        bid1 = ['medium', (steady+randint(-7, 7))*dist[1]]
        bid2 = ['long', int((steady+217+randint(-7, 7))*dist[2])]
    elif (30 <= dist[2] <= 33):
        bid0 = ['short', (steady+randint(-7, 7))*dist[0]]
        bid1 = ['long', (steady+randint(-7, 7))*dist[2]]
        bid2 = ['medium', randint(0, 117)]
    elif (36 <= dist[2] <= 39):
        bid0 = ['long', (steady+randint(-7, 7))*dist[2]]
        bid1 = ['medium', (steady+randint(-7, 7))*dist[1]]
        bid2 = ['short', randint(0, 117)]

    # end-of-game part: refinements to spend money optimally at the end
        
    done = [0, 0, 0]
    if (pos[1] == 100):
        bid1[1] = 0
        done[1] = 1
    if (pos[0] == 100):
        bid0[1] = 0
        done[0] = 1
    if (pos[2] == 100):
        bid2[1] = 0
        done[2] = 1
    if (done[2] == 1 and sum(done) == 1) or (sum(done) == 0): # fine-tuning doubles
        score0 = [0, 0, 0]
        score1 = [0, 0, 0]
        for i in range(3):
            p = pos[0] + dist[i]
            score0[i] = pos_worth(p)
            p = pos[1] + dist[i]
            score1[i] = pos_worth(p)
        best = -10000
        bi = [100, 100]
        for i in range(3):
            for j in range(3):
                if 33 <= dist[2] <= 36 and dist[2]+pos[2] != 99 and (i == 2 or j == 2):
                    pass
                elif i == j:
                    p0 = score0[i]+pos_worth(pos[1])
                    p1 = score1[j]+pos_worth(pos[0])
                    if p0 > p1 and p0 > best:
                        best = p0
                        bi = [i, 100]
                    elif p1 > best:
                        best = p1
                        bi = [100, j]
                else:
                    p = score0[i] + score1[j]
                    if (best < p):
                        best = p
                        bi = [i, j]
        lengths = ['short', 'medium', 'long']
        """print("-------")
        if bi[0] == 100:
            print(best, pos[0], pos[1]+dist[bi[1]])
        elif bi[1] == 100:
            print(best, pos[0]+dist[bi[0]], pos[1])
        else:
            print(best, pos[0]+dist[bi[0]], pos[1]+dist[bi[1]])
        print("-------")"""
        if bi[0] == 100:
            bid0 = [lengths[bi[1]], 0]
        else:
            bid0 = [lengths[bi[0]], (steady+randint(-7, 7))*min(dist[bi[0]], 100-pos[0])]
        if bi[1] == 100:
            bid1 = [lengths[bi[0]], 0]
        else:
            bid1 = [lengths[bi[1]], (steady+randint(-7, 7))*min(dist[bi[1]], 100-pos[1])]
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
        elif (pos[u] + dist[1] >= 70):
            bidend = ['medium', int(0.96*dist[1]/(100-pos[u])*funds[0])]
        else:
            bidend = ['long', int(0.96*dist[2]/(100-pos[u])*funds[0])]
        if u == 0:
            bid0 = bidend
        if u == 1:
            bid1 = bidend
        if u == 2:
            bid2 = bidend

    # send bids
    
    bids = [bid0,bid1,bid2]
    return bids

def pos_worth(p):
    if p < 70:
        return p - 70
    elif p < 85:
        return 0
    elif p < 90:
        return -25 * (p - 85)
    elif p < 100:
        return -1000
    else:
        return (110 - p) * 3

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
        if pos[1] + dist[0] < 100 and (not pos[2] + dist[0] < 100):
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
