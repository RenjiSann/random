


class binaryTree:

	def __init__(self, key, leftChild = None, rightChild = None):
		"""
			constructeur, méthode appelée pour l'instanciation un arbre binaire
		"""

		self.key = key
		self.left = leftChild
		self.right = rightChild



def size(T):
	"""
		retourne la taille (le nombre de noeuds) de l'arbre
	"""
	if T == None:	# Si l'arbre est vide, il n'a aucun noeud, donc sa taille est 0
		return 0
	
	res = 1			# Si l'arbre n'est pas vide, sa taille est 1 + la taille de ses fils

	res += size(T.left)
	res += size(T.right)

	return res


def height(T):
	"""
		retourne la hauteur de l'arbre, soit la plus grande longueur de cheminement de ses noeuds
		la hauteur d'un noeud racine est 0 et -1 pour un arbre vide
	"""

	if T == None:	# cas de l'arbre vide
		return -1

	h_left = height(T.left)		# on récupère la hauteur du sous-arbre gauche
	h_right = height(T.right)	# et celle du sous-arbre droit

	return 1 + max(h_left, h_right) # la hauteur d'un noeud est 1 + la hauteur max entre ses 2 fils



	"""
		Les deux fonctions suivantes sont des modèles montrant les 2 parcours possibles d'un arbre.
		
		Le premier est appelé  PARCOURS PROFONDEUR  ou DFS (pour Depth First Search) et consiste à
		'visiter' un des sous arbres du noeud entièrement avant de visiter l'autre sous arbre

		Le second est appelé  PARCOURS LARGEUR  ou BFS (pour Breadth First Search) et consiste cette
		fois à 'visiter' tous les fils d'un noeud avant de passer aux petits fils


                      YOU
                     /   \
                    /     \
                   M       P
				  / \     / \
			    GMM GPM GMP GPM

		On peut faire un parallèle avec un arbre généalogique. Imaginez que vous êtes en présence
		de vos 2 parents et vos 4 grand parents et que vous vouliez leur demander leur âge un par un.
		
		La méthode profondeur consisterait à demander d'abord à votre mère, puis à sa mère à elle, soit
		votre grand-mère maternelle. Enfin, puisque vos arrières grands parents ne sont pas là, vous 
		'remontez', puis demandez au père de votre mère, soit votre grand père maternel. Une fois celà
		fait, vous avez demandé l'âge de toute la famille de votre mère, passons donc à la famille paternelle.
		Vous commencez par votre père, puis votre grand mère paternelle, et enfin votre grand père paternel.
		Ainsi vous avez demandé l'âge de toute votre famille présente.

		En utilisant le parcours largeur, vous demanderez l'âge de votre famille dans cet ordre:
			mère, père, grand mère maternelle, grand père maternel, grand mère paternelle, grand père paternel


		

	"""


def DFS(T):
	if T == None:
		# traitement de cas d'arrêt
		return

	# traitement préfixe (effectué avant de "descendre" aux noeuds suivants)
	print(T.key[0]+" ", T.key[1])

	DFS(T.left) # Appel récursif de la fonction sur le sous-arbre gauche

	# traitement infixe (effectué entre l'appel récursif des fils) (inutilisé dans cet exemple)

	DFS(T.right) # Appel récursif de la fonction sur le sous-arbre droit

	# traitement suffixe (effectué après les appels récursifs sur les fils) (inutilisé dans cet exemple)



def BFS(T):
	q = [] 		# q sera une queue, une liste de donnée telle que la valeur qui en sort est la première qui y est entrée (c'est une structure FiFo, First in, First out)

	q.append(T) # on ajoute T dans la queue, celle-ci contiendra toujours à sa première place le noeud suivant à traiter

	while q != []:	# tant que la queue n'est pas vide (tant qu'il reste des éléments à traiter)

		k = q.pop(0) #on récupère le 1er élément de la file en le supprimant

		# traitement du noeud
		print(k.key[0]+" ", k.key[1])

		if k.left != None:		# Si le sous-arbre gauche existe, alors on l'ajoute à la file des noeuds à traiter
			q.append(k.left)
		if k.right != None:
			q.append(k.right)	# Idem pour le sous-arbre droit



arbre1 = binaryTree(("you", 17), 
			binaryTree(("mother",45), 
				binaryTree(("grand mother (mother)",82), None, None),
				binaryTree(("grand father (mother)",79), None, None)
			),
			binaryTree(("father", 48),
				binaryTree(("grand mother (father)",75), None, None),
				binaryTree(("grand father (father)",73), None, None)
			)
		)

print("Ages en parcours profondeur:")
DFS(arbre1)
print("Ages en parcours largeur")
BFS(arbre1)