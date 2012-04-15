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

    addToMap(fMap, vertices[0], vertices[1])
    addToMap(rMap, vertices[1], vertices[0])

    mxVert = max(mxVert, vertices[0], vertices[1])

pprint.pprint(fMap)
print "------------------------"
pprint.pprint(rMap)
print "------------------------"
print 'Max is:', mxVert
