import re

class Graph:
    def __init__(self, gdict = None):
        if gdict == None:
            gdict = dict()
        self.gdict = gdict

    def items(self):
        return self.gdict.items()

    def vertice(self, vrtx):
        try:
            return list(self.gdict[vrtx])
        except KeyError:
            return None

    def edges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []

    def addEdge(self, edge):
        if edge[0] in self.gdict:
            self.gdict[edge[0]].append(edge[1])
        else:
            self.gdict[edge[0]] = [edge[1]]

with open('input') as file:
    lines = file.readlines()
    lines = [line[:len(line)-1] for line in lines]

# Part 1:
graph = Graph()
for line in lines:
    args = re.split(' bags contain | bags, | bag, | bags.| bag.', line)
    args.pop()
    for i in range(1, len(args)):
        if args[i][0:2] == 'no':
            continue
        graph.addEdge([args[i][2:], (int(args[i][0]), args[0])])

def getAllParents(G, color, cSet):
    cSet.add(color)
    if G.vertice(color) != None:
        for parent in G.vertice(color):
            pSet = getAllParents(G, parent[1], cSet)
            cSet = cSet.union(pSet)
    return cSet

print(len(getAllParents(graph, 'shiny gold', set()))-1)

# Part 2:
graph = Graph()
for line in lines:
    args = re.split(' bags contain | bags, | bag, | bags.| bag.', line)
    args.pop()
    for i in range(1, len(args)):
        if args[i][0:2] == 'no':
            continue
        graph.addEdge([args[0], (int(args[i][0]), args[i][2:])])

def countAllChildren(G, color, s):
    if G.vertice(color) != None:
        # G.visit(color)
        for child in G.vertice(color):
            s += child[0] * countAllChildren(G, child[1], 1)
    return s

print(countAllChildren(graph, 'shiny gold', 1)-1)
