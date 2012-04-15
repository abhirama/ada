import pprint

def addToMap(mp, tail, head):
    if tail in mp: 
        mp[tail].append((tail, head))
    else:
        mp[tail] = [(tail, head)]

fh = open('small.txt')

lines = fh.readlines()

fMap = {}

rMap = {}

mxVert = 0

for line in lines:
    line = line.strip()
    vertices = line.split()

    v0 = long(vertices[0])
    v1 = long(vertices[1])

    addToMap(fMap, v0, v1)
    addToMap(rMap, v1, v0)

    mxVert = max(mxVert, v0, v1)


_timer = 0
def dfs(vert, seen, timeMap):
    if vert in seen:
        return False 
        
    seen.add(vert)

    global _timer
    if vert in fMap:
        edges = fMap[vert] 
        for edge in edges:
            if not dfs(edge[1], seen, timeMap):
                _timer = _timer + 1
                timeMap[vert] = _timer

        if not vert in timeMap:
            _timer = _timer + 1
            timeMap[vert] = _timer
        return True
    else:
        return False 



seen = set()
timeMap = {}

for vert in reversed(xrange(1, mxVert + 1)):
   if not dfs(vert, seen, timeMap):
        if not vert in timeMap:
            _timer = _timer + 1
            timeMap[vert] = _timer


pprint.pprint(timeMap)
