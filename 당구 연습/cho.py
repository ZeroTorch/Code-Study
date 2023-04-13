def possible_way(m, n, startPos, endPos):
    startX, startY = startPos
    endX, endY = endPos
    
    way = []
    
    # x축상에 같은 위치에 있으면
    if startX == endX:
        if startY > endY:
            way.append((startX, n+(n-startY)))
        else:
            way.append((startX, -startY))
    else:
        way.append((startX, n+(n-startY)))
        way.append((startX, -startY))
    
    # y축상에 같은 위치에 있으면
    if startY == endY:
        if startX > endX:
            way.append((m + (m - startX), startY))
        else:
            way.append((-startX, startY))
    else:
        way.append((m+(m-startX), startY))
        way.append((-startX, startY))
    
    # y=x상에 같은 위치에 있으면
    if startY / startX == endY / endX == n/m:
        if startX < endX:
            way.append((-startX, -endX))
        else:
            way.append((m+(m-startX), n+(n-startY)))
    
    if startY / startX == endY / endX == -n/m:
        if startX < endX:
            way.append((-startX, n+(n-startY)))
        else:
            way.append((m+(m-startX), -startY))
    
    return way

def distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    

def solution(m, n, startX, startY, balls):
    answer = []

    for b in balls:
        ways = possible_way(m, n, [startX, startY], b)
        min_dis = 1e9
        for w in ways:
            min_dis = min(min_dis, distance(b, w))
            
        answer.append(min_dis)
    return answer
