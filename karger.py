import pprint
import random

#todo - very sloppily written, lots of refactoring needed.

def contract(graph, vertex0, vertex1):
    adjecents0 = graph[vertex0]
    adjecents1 = graph[vertex1]
    adjecents = adjecents0 + adjecents1
    vertex = "{0}-{1}".format(vertex0, vertex1)
    del graph[vertex0]
    del graph[vertex1]
    graph[vertex] = adjecents

    for adjecentList in graph.values():
        if vertex0 in adjecentList:
            count = adjecentList.count(vertex0)

            while count:
                del adjecentList[adjecentList.index(vertex0)]
                adjecentList.append(vertex)
                count = count - 1

        if vertex1 in adjecentList:
            count = adjecentList.count(vertex1)

            while count:
                del adjecentList[adjecentList.index(vertex1)]
                adjecentList.append(vertex)
                count = count - 1

    for key, value in graph.iteritems():
        if key in value:
            #print "key is:", key
            #pprint.pprint(value)
            count = value.count(key)
            while count:
                del value[value.index(key)]
                count = count - 1

mins = []
count = 100

while count > 0:
    fh = open('kargerAdj.txt')

    lines = fh.readlines()

    graph = {}
    for line in lines:
        vertices = line.split()
        graph[vertices[0]] = vertices[1:]

    #pprint.pprint(graph)

    while len(graph.keys()) > 2:
        randVertex0 = graph.keys()[random.randint(0, len(graph.keys()) - 1)]
        adjecents = graph[randVertex0]
        randVertex1 = adjecents[random.randint(0, len(adjecents) - 1)]

        #print "Contraction candidates: {0} - {1}".format(randVertex0, randVertex1)
        #pprint.pprint(graph)

        contract(graph, randVertex0, randVertex1)

    #pprint.pprint(graph)

    minimumCuts = 0
    for values in graph.values():
        mins.append(len(values))
        break

    count = count - 1

print min(mins)
