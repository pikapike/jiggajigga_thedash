def candlestickmaker(pos, funds, dist):
    runnersneeded = [i for i in range(3) if pos[i] != 100]
    bids = [[], [], []]
    import random
    
    vpm1 = 3400
    
    if pos[0] != 100:
        if pos[0] == 0:
            bids[0] = ["long", dist[2] * vpm1]
        elif pos[0] >= 30 and pos[0] <= 39:
            bids[0] = ["long", dist[2] * vpm1]
        elif pos[0] >= 60 and pos[0] <= 70:
            #Case 1
            bids[0] = ["medium", dist[1] * vpm1]
        elif pos[0] >= 71 and pos[0] <= 78:
            #Case 2
            bids[0] = ["small", dist[0] * vpm1]
        else:
            if dist[0] >= 100 - pos[0]:
                bids[0] = ["small", dist[0] * vpm1]
            else:
                bids[0] = ["medium", dist[1] * vpm1]

        valuepermeter = ((funds[0]-pos[0]*3333))//(310-pos[0]-pos[1]-pos[2])
        
        if bids[0][0] == "small":
            if pos[1] >= pos[2]:
                bids[1] = ["long", valuepermeter*pos[1]]
                bids[2] = ["medium", valuepermeter*pos[2]]
            else:
                bids[1] = ["medium", valuepermeter*pos[1]]
                bids[2] = ["long", valuepermeter*pos[2]]
        elif bids[0][0] == "medium":
            if pos[1] >= pos[2]:
                bids[1] = ["long", valuepermeter*pos[1]]
                bids[2] = ["short", valuepermeter*pos[2]]
            else:
                bids[1] = ["short", valuepermeter*pos[1]]
                bids[2] = ["long", valuepermeter*pos[2]]
        else:
            if pos[1] >= pos[2]:
                bids[1] = ["medium", valuepermeter*pos[1]]
                bids[2] = ["short", valuepermeter*pos[2]]
            else:
                bids[1] = ["medium", valuepermeter*pos[1]]
                bids[2] = ["short", valuepermeter*pos[2]]
    elif len(runnersneeded) == 2:
        bids[0] = ["small", 0]
        valuepermeter = (funds[0])//(210+random.randint(-3, 3)-pos[1]-pos[2])

        if pos[1] > pos[2]:
            bids[2] = ["long", valuepermeter*dist[2]]
            bids[1] = ["medium", valuepermeter*dist[1]]
        else:
            bids[1] = ["medium", valuepermeter*dist[1]]
            bids[2] = ["long", valuepermeter*dist[2]]
    else:
        valuepermeter = (funds[0])//(110-pos[runnersneeded[0]])
        rn = runnersneeded[0]
        
        if 100 - pos[rn] <= dist[0]:
            bids[rn] = ["short", dist[0]*valuepermeter]
            bids[(rn+1)%3] = ["medium", 0]
            bids[(rn-1)%3] = ["long", 0]
        elif 100 - pos[rn] <= dist[1]:
            bids[rn] = ["medium", dist[1]*valuepermeter]
            bids[(rn+1)%3] = ["short", 0]
            bids[(rn-1)%3] = ["long", 0]
        else:
            bids[rn] = ["long", dist[2]*valuepermeter]
            bids[(rn+1)%3] = ["medium", 0]
            bids[(rn-1)%3] = ["short", 0]
    return bids

