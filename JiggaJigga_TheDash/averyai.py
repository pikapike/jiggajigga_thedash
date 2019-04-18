def averyai(pos, funds, dist):
    runnerpos = [pos[0], pos[1], pos[2]]
    runnersdone = sum(100 == i for i in runnerpos)
    valuepermeter = (funds[0] - 150000) / (333 - pos[0] - pos[1] - pos[2])
    if runnersdone == 2:
        valuepermeter = funds[0] / (300 - pos[0] - pos[1] - pos[2])
    '''
    valuepermeter0 = (funds[0]/3)/(111-pos[0])
    valuepermeter1 = (funds[0]/3)/(111-pos[1])
    valuepermeter2 = (funds[0]/3)/(111-pos[2])
    '''
    # to counter steadyfreddy?
    '''
    print(valuepermeter0)
    print(valuepermeter1)
    print(valuepermeter2)
    '''
    '''
    if valuepermeter <= 3000 and (pos[0] < 50 or pos[1] < 50 or pos[2] < 50):
        valuepermeter = 3001
    '''

    smallbid = valuepermeter * dist[0]
    midbid = valuepermeter * dist[1]
    bigbid = valuepermeter * dist[2]

    if runnersdone == 1:
        smallchunk = valuepermeter * dist[0] / 2
        smallbid = 0
        midbid = valuepermeter * dist[1] + smallchunk
        bigbid = valuepermeter * dist[2] + smallchunk
    elif runnersdone == 2:
        midbid = valuepermeter * dist[1] + smallbid + bigbid
        smallbid = 0
        bigbid = 0

    bigRun = 0
    smallRun = 1

    if not (pos[0]+pos[1]+pos[2])//3 <= 75:
        '''
        smallbid = valuepermeter0*dist[0]+7500
        midbid = valuepermeter0*ist[1]+7500
        bigbid = valuepermeter0*dist[2]+7500
        '''
        smallbid += 7500
        midbid += 7500
        bigbid += 7500
        
    else:
        smallbid = valuepermeter*dist[0]
        midbid = valuepermeter*dist[1]
        bigbid = valuepermeter*dist[2]

    for i in range(3):
        if runnerpos[i] > runnerpos[bigRun]:
            bigRun = i
        elif runnerpos[i] < runnerpos[smallRun]:
            smallRun = i
    
    midRun = [0, 1, 2]
    midRun.remove(bigRun)
    midRun.remove(smallRun)
    midRun = midRun[0]
    
    bids = [[], [], []]
    
    bids[smallRun] = ["long", bigbid]
    bids[bigRun] = ["short", smallbid]
    bids[midRun] = ["medium", midbid]
    
    return bids
