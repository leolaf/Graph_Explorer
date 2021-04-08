from GraphExplorer import ConceptNode, InstanceNode, Graph
import sys
import re as regex
from TypeEnum import gout, relation

def creerMistecache():
    """CONSTANTE ATTRIBUTS"""


    """Fonction qui créer puis retourne le graphe de Mistecache"""

    nourriture = ConceptNode("Nourritures")
    recette = ConceptNode("Recettes")
    entree = ConceptNode("Entrées")
    plat = ConceptNode("Plats")
    dessert = ConceptNode("Dessert")
    ingredient = ConceptNode("Ingrédients")
    vegetal = ConceptNode("Végétal")
    animal = ConceptNode("Animal")
    viande = ConceptNode("Viande")
    poisson = ConceptNode("Poisson")



    poisson.addExit(animal,Relation.ISA)
    viande.addExit(animal,Relation.ISA)
    animal.addExit(ingredient,Relation.AKO)
    vegetal.addExit(ingredient,Relation.AKO)
    ingredient.addExit(nourriture,Relation.AKO)
    ingredient.addExit(recette,Relation.PARTOF)
    entree.addExit(recette,Relation.AKO)
    plat.addExit(recette,Relation.AKO)
    dessert.addExit(recette,Relation.AKO)
    recette.addExit(nourriture,Relation.AKO)


    ensemble = [nourriture,recette,entree,plat,dessert,ingredient,vegetal,animal,viande,poisson]
    mistecache = Graph(ensemble)
    return mistecache




def affiche_aide(topic):
    """Affiche l'aide en fonction du topic"""
    print(f"---- HELP {topic.upper()} ----")
    match topic:
        case "add":
            print("The command add create an instance of one or multiple concept(s)")
            print("-- SYNTAX --")
            print("add <instanceName> isa <conceptNode>")
            print("add <instanceName> isa <conceptNode>, <conceptNode>")
            print("-- EXAMPLE --")
            print("add Hareng isa Poisson")
            print("add Melon - Jambon cru isa Entrée, Dessert")
        case "ajouteAtt":
            print("The command update the attributs of a instance")
            print("-- SYNTAX --")
            print("changeAttr <instanceName> <attributKeyName> <value> ")
            print("-- EXAMPLE --")
            print("changeAttr Hareng ph 7")
            print("changeAttr Melon cironconférance 18")
        case "changeAttr":
            print("The command update the attributs of a instance")
            print("-- SYNTAX --")
            print("changeAttr <instanceName> <attributKeyName> <value> ")
            print("-- EXAMPLE --")
            print("changeAttr Hareng ph 7")
            print("changeAttr Melon cironconferance 18")
        case _:
            print()

def skip_spaces(mot):
    while mot[0] == " ":
        mot = mot[1:]
    while mot[len(mot)-1] == " ":
        mot = mot[0:len(mot)-2]
    return mot

def recherche(graph ,liste_nom):
    for nom in liste_nom:

        node = graph.search(nom)
        node.show()
        tab = node.getEntries()
        res.append(node)
        print(node)
        res += tab

        for elem in tab:
            print(elem)

    return res

def ajoute(graph, name, listConcepts):
    newNode = mistecache.addNode(InstanceNode(name))
    for concept in listConcepts:
        conceptNode = rechercherNoeud(mistecache, concept)
        newNode.addExit(conceptNode, relation.INSTANCE)

def ajouteAtt(graph, name, attributKeyName, value):
    noeud = graph.search(name)
    if noeud.getAttr(attributKeyName):
        print(f"The attribut {attributKeyName} already exist, the value is : {noeud.getAttr(attributKeyName)} ")
        return
    noeud.addAttr(attributKeyName, value)

def changeAttribut(graph, name, attributKeyName, value):
    noeud = graph.search(name)
    if !noeud.getAttr(attributKeyName):
        print(f"The attribut {attributKeyName} does not exist")
        return
    noeud.updateAttr(attributKeyName, value)