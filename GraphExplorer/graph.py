class Graph(object):

	# Constructeur
	# Entrée : liste de noeud (facultatif, par défaut : liste vide)
	def __init__(self, set=[]):
		self.set = set

	# Procédure d'ajout de noeud au graphe
	def addNode(self, n):
		if(self.set == None):
			self.set = [n]
		else:
			self.set.append(n)

	# Procédure de suppression d'un noeud du graphe
	def deleteNode(self, node):
		for noeud in self.set:
			if node in self.getExits(self.set):
				self.deleteExit(node,noeud)
			if node in self.getEntries(self.set):
				self.deleteEntry(node,noeud)

		self.set.remove(node)


	# Fonction de récupération des noeuds du graphes
	# Sorties : liste de noeud
	def getNodeSet(self):
		return self.set

	def path_in_width(self, startingNode):
		queue = Queue()
		for node in self.getNodeSet():
			node.tree = None
			node.distance = None
			node.color = "white"
		#Pour tous les sommets -> mettre en blanc et arbo = None
		startingNode.distance = 0
		queue.stack(startingNode)
		startingNode.color = "grey"

		while not(queue.isEmpty()):
			node = queue.unstack()
			nextNodes = node.getNodes()
			for nextNode in nextNodes:
				if nextNode.color == "white":
					queue.stack(nextNode)
					nextNode.color = "grey"
					nextNode.tree = node
					nextNode.distance = node.distance + 1
			node.color = "black"

	def deep_traversal(self, startingNode):
		nodeStack = Stack()
		for node in self.getNodeSet():
			node.marked = False
		startingNode.distance = 0
		nodeStack.stack(startingNode)
		while not(nodeStack.isEmpty()):
			node = nodeStack.unstack()
			if(not(node.marked)):
				node.marked = True
			for child in node.getNodes():
				if(not(child.marked)):
					child.distance = node.distance + 1
					nodeStack.stack(child)

	def dijkstra(self, startingNode):
		p = Graph()
		nodes = self.getNodeSet()
		for node in nodes:
			node.distance = None
		startingNode.distance = 0
		# On vérfie que les deux graphes ne possèdent pas les mêmes noeuds
		while not(same_values_in_it(p.getNodeSet(), nodes)):
			nodeMinDistance = None
			# On choisit le noeud avec le moins de distance du graphe
			for node in nodes:
				if(node.distance != None and not(node in p.getNodeSet())):
					if (nodeMinDistance != None):
						if(node.distance < nodeMinDistance.distance):
							nodeMinDistance = node
					nodeMinDistance = node
			p.addNode(nodeMinDistance)
			# Pour chaque voisin du noeud on vérifie que sa distance ne s'est pas réduite ou on l'initialise
			for neighbour in nodeMinDistance.getNodes():
				if not(neighbour in p.getNodeSet()):
					if(neighbour.distance == None or neighbour.distance > (nodeMinDistance.distance + nodeMinDistance.getWeight(neighbour))):
						neighbour.distance = nodeMinDistance.distance + nodeMinDistance.getWeight(neighbour)

	def search(self, name):
		for node in self.getNodeSet():
			if node.getName() == name:
				return node
		return None
