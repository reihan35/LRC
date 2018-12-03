from LRC_TME8_definitions_Allen import *

def transposeSet(s):
	l = []
	for i in s:
		l.append(transpose[i])
		
	return l
	
def symetrieSet(s):
	l = []
	for i in s:
		l.append(symetrie[i])
		
	return l
	
def compose(r1, r2):
	if r1 == '=':
		return r2
	elif r2 == '=':
		return r1
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
	
print(compose('=', 'd'))
print(compose('m', 'd'))
print(compose('ot', '>'))
print(compose('>', 'e'))
print(compose('ot', 'm'))

S1 = ['d', '=', 's', 'e']
S2 = ['m', '<']

print(compositionSet(S1,S2))

class Graphe:
	
	def __init__(self):
		self.noeuds = []
		self.relations = dict()
		
	def getRelations(self,i,j):
		if (i,j) in self.relations:
			return self.relations[(i,j)]
		elif (j,i) in self.relations:
			return self.relations[(j,i)]
		else:
			return {'<', 'm', 'o', 'et', 'dt', 's', '=', 'st', 'd', 'e', 'ot', 'mt', '>'}
	
	def ajouter(self,i,j,r):
		if (i,j) not in self.relations:
			self.relations[(i,j)] = r
		else:
			self.relations[(i,j)].union(r)
	
	def propagation(self,a,b, r):
		p = [(a,b)]
		
		while p != []:
			(i,j) = p.pop()
			new_rels = self.relations
				
			for k in self.noeuds:
				if k != i and k != j:
					new_rels[(i,k)] = self.getRelations(i,k).intersection(\
						compositionSet(self.getRelations(i,j), self.getRelations(j,k)))
					new_rels[(k,j)] = self.getRelations(k,j).intersection(\
						compositionSet(self.getRelations(k,i), self.getRelations(i,j)))
							
					if new_rels[(i,k)] == set() or new_rels[(k,j)] == set():
						return 
					if new_rels[(i,k)] != self.getRelations(i,k):
						self.relations[(i,k)] = new_rels[(i,k)]
						p.append((i,k))
					if new_rels[(k,j)] != self.getRelations(k,j):
						print ("contradiction temporelle")
						self.relations[(k,j)] = new_rels[(k,j)]
						p.append((k,j))
						
						
						
#TEST

g = Graphe()
g.noeuds = ["A","B","C"]
g.ajouter("A","B",{"<"})
g.ajouter("A","C",{">"})				
print(g.relations)		 	 	
g.propagation("B","C", "=")			
print(g.relations)		 
#g.ajouter("A","C",{">"})					 	
#g.ajouter("A","C",{">"})					 	
				
				
				
				
				
				
				
				
				
				
				
				
				
	
