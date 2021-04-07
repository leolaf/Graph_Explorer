class Node(object):

	# Constructeur
	# Entrées : nom -> string
	# 			isOriented -> booleen (facultatif, par défaut : False) (True si Noeud de graphe orienté, False sinon)
	def __init__(self, name, isOriented = False):
		self.name = name
		self.isOriented = isOriented
		# Représentation des noeud précedents en dictionnaire python (clé : noeud, valeur : poids de l'arc)
		self.previousNodes = dict()
		# Représentation des noeud suivants en dictionnaire python (clé : noeud, valeur : poids de l'arc)
		self.nextNodes = dict()

	# Fonction de transformation en chaine de caractère
	# Sortie : string
	def __str__(self):
		return self.name

	# Fonction décrivant l'équivalence entre deux noeuds
	# Sortie : booléen (True si égaux, False sinon)
	def __eq__(self, n):
		if(self is None and n is None):
			return True
		elif(self is None or n is None):
			return False
		return (self.name == n.name and 
				self.isOriented == n.isOriented and
				self.previousNodes == n.previousNodes and
				self.nextNodes == n.nextNodes)

	# Fonction de hashage du noeud, utile pour être utilisé en tant que clé de dictionnaire
	# Sortie : entier toujours égal à 0
	def __hash__(self):
		return 0

	# Procédure de liage de noeuds
	# Si graphe non orienté : lie le noeud a un autre
	# Entrée : noeud à lier
	def addNode(self, node, weight = 1):
		if(not(self.isOriented)):
			if(node in self.getNodes()):
				return
			if(self.previousNodes == None):
				self.previousNodes = dict()
			self.previousNodes[node] = weight
			self.nextNodes = self.previousNodes
			return node.addNode(self,weight)
		else: 
			print("The node " + str(self) + " is part of an oriented graph.\nPlease use addEntry(Node) and addExit(Node) methods on that node.")

	# Procédure de liage de noeud
	# Si graphe non orienté : lie le noeud a un noeud de sortie
	# Entrée : noeud à lier
	def addExit(self, node, weight = 1):
		if(not(self.isOriented)):
			print("The node " + str(self) + " is not part of an oriented graph.\nPlease use addNode(Node) method on that node.")
		else:
			if(self.nextNodes == None):
				self.nextNodes = dict()
			self.nextNodes[node] = weight
			if(not(self in node.getEntries())):
				node.addEntry(self, weight)

	# Procédure de liage de noeud
	# Si graphe non orienté : lie le noeud a un noeud d'entré
	# Entrée : noeud à lier
	def addEntry(self, node):
		if(not(self.isOriented)):
			print("The node " + str(self) + " is not part of an oriented graph.\nPlease use addNode(Node) method on that node.")
		else:
			if(self.previousNodes == None):
				self.previousNodes = dict()
			self.previousNodes.append(node)
			if(not(self in node.getExits())):
				node.addExit(self, weight)

	# Fonction qui retourne la liste des noeuds de sortie
	# Sortie : liste de noeuds
	def getExits(self):
		if(not(self.isOriented)):
			print("The node " + str(self) + " is not part of an oriented graph.\nPlease use getNode() method on that node.")
		else:
			if(self.nextNodes == None):
				self.nextNodes = dict()
			return list(self.nextNodes.keys())

	# Fonction qui retourne la liste des noeuds d'entrée
	# Sortie : liste de noeuds
	def getEntries(self):
		if(not(self.isOriented)):
			print("The node " + str(self) + " is not part of an oriented graph.\nPlease use getNode() method on that node.")
		else:
			if(self.previousNodes == None):
				self.previousNodes = dict()
			return list(self.previousNodes.keys())


	# Fonction qui retourne la liste des noeuds liés
	# Sortie : liste de noeuds
	def getNodes(self):
		if(self.isOriented):
			print("The node " + str(self) + " is part of an oriented graph.\nPlease use getExits() and getEntries() methods on that node.")
		else:
			if(self.previousNodes == None):
				self.previousNodes = dict()
			return list(self.previousNodes.keys())

	# Fonction qui retourne le poids entre le noeud et un autre noeud
	# Entrée : noeud lié a ce noeud
	# Sortie : élement correspondant au poids 
	def getWeight(self,node):
		if(self.isOriented):
			if(node in self.getExits()):
				return self.nextNodes[node]
		return self.previousNodes[node] 