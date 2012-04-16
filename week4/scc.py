import pprint

def createGraph(mp, tail, head):
    if tail in mp: 
        mp[tail].append((tail, head))
    else:
        mp[tail] = [(tail, head)]

fh = open('small.txt')

lines = fh.readlines()

fGraph = {}

rGraph = {}

mxVert = 0

for line in lines:
    line = line.strip()
    vertices = line.split()

    v0 = long(vertices[0])
    v1 = long(vertices[1])

    createGraph(fGraph, v0, v1)
    createGraph(rGraph, v1, v0)

    mxVert = max(mxVert, v0, v1)


def dfsForTime(vert, seen, timeMap):
    if vert in seen:
        return False 
        
    seen.add(vert)

    global _timer
    if vert in fGraph:
        edges = fGraph[vert] 
        for edge in edges:
            dfsForTime(edge[1], seen, timeMap)

        _timer = _timer + 1
        timeMap[vert] = _timer
        return True
    else:
        return False 



seen = set()
timeMap = {}

_timer = 0
for vert in reversed(xrange(1, mxVert + 1)):
   if not dfsForTime(vert, seen, timeMap):
        if not vert in timeMap:
            _timer = _timer + 1
            timeMap[vert] = _timer


pprint.pprint(timeMap)
