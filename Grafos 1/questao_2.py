
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.distance = 0
        self.predecessor = None
        self.color = "white"


    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def removeNeighbor(self, nbr):
        if nbr in self.connectedTo: self.connectedTo.pop(nbr)

    def getConnections(self):
        return sorted([(self.getWeight(neighbor), neighbor.getId()) for neighbor in self.connectedTo.keys()])

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def setDistance(self, distance):
        self.distance = distance

    def setPredecessor(self, predecessor):
        self.predecessor = predecessor

    def setColor(self, color):
        self.color = color

    def getDistance(self, distance):
        return self.distance

    def getPredecessor(self, predecessor):
        return self.predecessor

    def getColor(self, color):
        return self.color

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.numWeight = 0
        self.numEdges = 0

    def addVertex(self,key):
        if key in self.vertList.keys(): return
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def removeVertex(self, key):
        self.numVertices -= 1
        toRemove = self.getVertex(key)

        while len(toRemove.connectedTo) != 0:
            for i in toRemove.connectedTo:
                self.removeEdge(key, i)
                break

        for vertex in self:
            if toRemove in vertex.connectedTo: 
                self.numEdges -= 1
                self.numWeight -= float(vertex.getWeight(toRemove))
                vertex.removeNeighbor(key)


        self.vertList.pop(key)

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)
        self.numWeight += float(weight)
        self.numEdges += 1

    def removeEdge(self, source, destine):
        if type(source) == str:
            source = self.getVertex(source)
        elif not source: return

        self.numWeight -= float(source.getWeight(destine))
        self.numEdges -= 1
        source.removeNeighbor(destine)

    def getVertices(self):
        return self.vertList.keys()


    def __contains__(self,n):
        return n in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())


## TroubleShooting

graph = Graph()
n = int(input())


#Setting the graph 
#including the neighboors
for i in range(n):
    data = input().split()

    id = data[0]
    graph.addVertex(id)
    current = graph.getVertex(id)

    times = data[1]
    people = data[2:]

    for crush in people:
        if crush not in graph: graph.addVertex(crush)
        neighboor = graph.getVertex(crush)
        current.addNeighbor(neighboor, 1)


flag = False
for vertex in graph:
    for crush in vertex.connectedTo:
        for neighboor in crush.connectedTo:
            if vertex.getId() == neighboor.getId(): 
                print("Hoje tem!")
                flag = True
        if flag: break
    if flag: break
else:
    print("... que ama ninguem.")