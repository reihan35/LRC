from LRC_TME8_definitions_Allen import *

def transposeSet(s):
    l = []
    for i in s:
        l.append(transpose[i])

    return set(l)

def symetrieSet(s):
    l = []
    for i in s:
        l.append(symetrie[i])

    return set(l)

def compose(r1, r2):
    if r1 == '=':
        return set(r2)
    elif r2 == '=':
        return set(r1)
    elif (r1,r2) in compositionBase:
        return compositionBase[(r1,r2)]
    elif (transpose[r2],transpose[r1]) in compositionBase:
        return transposeSet(compositionBase[(transpose[r2],transpose[r1])])
    elif (symetrie[r1], symetrie[r2]) in compositionBase:
        return symetrieSet(compositionBase[(symetrie[r1],symetrie[r2])])
    else:
        return transposeSet(symetrieSet(compositionBase[(transpose[symetrie[r2]], transpose[symetrie[r1]])]))

def compositionSet(S1, S2):
    l = []
    for s1 in S1:
        for s2 in S2:
            l.extend(compose(s1,s2))
    l = set(l)
    return l

#print("= o d : {}".format(compose('=', 'd')))
#print("m o d : {} ".format(compose('m', 'd')))
#print("ot o > : {}".format(compose('ot', '>')))
#print("> o e : {}".format(compose('>', 'e')))
#print("ot o m : {}".format(compose('ot', 'm')))
#
#S1 = ['d', '=', 's', 'e']
#S2 = ['m', '<']
#
#print(compositionSet(S1,S2))

class Graphe:

    def __init__(self):
        self.noeuds = []
        self.relations = dict()

    def getRelations(self,i,j):
        if (i,j) in self.relations:
            return self.relations[(i,j)]
        elif (j,i) in self.relations:
            return transposeSet(self.relations[(j,i)])
        else:
            return {'<', 'm', 'o', 'et', 'dt', 's', '=', 'st', 'd', 'e', 'ot', 'mt', '>'}

    def ajouter(self,i,j,r):
        if (i,j) not in self.relations:
            self.relations[(i,j)] = r
        else:
            self.relations[(i,j)].union(r)

    def propagation(self,a,b):
        p = [(a,b)]

        while p != []:
            (i,j) = p.pop()
            #print("R_{}{}".format(i,j))
            new_rels = self.relations.copy()

            for k in self.noeuds:
                if k != i and k != j:
                    new_rels[(i,k)] = self.getRelations(i,k).intersection(\
                            compositionSet(self.getRelations(i,j), self.getRelations(j,k)))
                    new_rels[(k,j)] = self.getRelations(k,j).intersection(\
                            compositionSet(self.getRelations(k,i), self.getRelations(i,j)))

#                    print("R_{}{} ^ (R_{}{} o R_{}{}) = {}".format(i, k, i,j, j, k, new_rels[(i,k)]))
#                    print("R_{}{} ^ (R_{}{} o R_{}{}) = {}".format(k, j ,k, i, i,j, new_rels[(k,j)]))
#                    print("R_{}{} o R_{}{} = {}".format(i,j, j, k, compositionSet(self.getRelations(i,j), self.getRelations(j,k))))
#                    print("R_{}{} o R_{}{} = {}".format(k,i, i, j, compositionSet(self.getRelations(k,i), self.getRelations(i,j))))

#                    print("R_{}{} : {}, newR_{}{} : {} ".format(i,k, new_rels[(i,k)], i, k, self.getRelations(i,k)))
#                    print("R_{}{} : {}, newR_{}{} : {}".format(k,j, new_rels[(k,j)], k, j, self.getRelations(k,j)))
                    if new_rels[(i,k)] == set() or new_rels[(k,j)] == set():
                        print("Contradiction temporelle")
                        return
                    if new_rels[(i,k)] != self.getRelations(i,k):
                        self.relations[(i,k)] = new_rels[(i,k)]
                        p.append((i,k))
                    if new_rels[(k,j)] != self.getRelations(k,j):
                        self.relations[(k,j)] = new_rels[(k,j)]
                        p.append((k,j))



#TEST
'''
4.
g = Graphe()
g.noeuds = ["A","B","C"]
g.ajouter("A","B",{"<"})
g.ajouter("A","C",{">"})
g.ajouter("A","C",{"<"})
g.ajouter("B", "C", {"="})
print("Relations : {}".format(g.relations))
print("R({},{}) : {}".format("B", "A", g.getRelations("B","A")))
print("R({},{}) : {}".format("C", "A", g.getRelations("C","A")))
print("R({},{}) : {}".format("B", "C", g.getRelations("B","C")))

g.propagation("B","C")
print(g.relations)
'''

'''
4.
g = Graphe()
g.noeuds = ["S", "L", "R"]
g.ajouter("L", "S", {"ot", "mt"})
g.ajouter("R", "S", {">", "mt", "<", "m"})
print("Relations : {}".format(g.relations))
g.propagation("L","S")
g.propagation("R","S")
print("R_LS = {} ".format(g.getRelations("L", "S")))
print("R_LR = {} ".format(g.getRelations("L", "R")))
print("R_SR = {} ".format(g.getRelations("S", "R")))
g.relations[('R','S')] = {">", "mt"}
print("Relations : {}".format(g.relations))
g.propagation("R","S");
print("R_LS = {} ".format(g.getRelations("L", "S")))
print("R_LR = {} ".format(g.getRelations("L", "R")))
print("R_SR = {} ".format(g.getRelations("S", "R")))
'''

g = Graphe()
g.noeuds = ['J', 'D', 'P', 'C']
g.ajouter('J','D', {'o', 'et', 'd', 's', '=', 'st', 'd', 'ot', 'e'})
g.ajouter('D', 'P', {'m', '<'})
g.ajouter('J', 'C', {'=', 'e', 'et'})
g.ajouter('C', 'D', {'d', '=', 's', 'e'})
print("R_JD = {}".format(g.getRelations('J','D')))
print("R_JC = {}".format(g.getRelations('J','C')))
print("R_DP = {}".format(g.getRelations('D','P')))
print("R_CD = {}".format(g.getRelations('C','D')))
print("R_CP = {}".format(g.getRelations('C','P')))
g.propagation('C', 'D')
print("Après propagation : ")
print("R_JD = {}".format(g.getRelations('J','D')))
print("R_JC = {}".format(g.getRelations('J','C')))
print("R_DP = {}".format(g.getRelations('D','P')))
print("R_CD = {}".format(g.getRelations('C','D')))
print("R_CP = {}".format(g.getRelations('C','P')))
