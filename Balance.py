from __future__ import barry_as_FLUFL
from posixpath import split
from ClassVar import Ledger
import importlib
from treelib import *


from Util import *


def generateBalance():
    sum = float(0)

    longestStringLenght = len(max(Ledger.listedValues, key=len)) + 1

    balanceDictionary = {}

    listedConcepts = []

    for date in Ledger.transactionsDictionaries:
        for concept in Ledger.transactionsDictionaries[date]:
            value = Ledger.transactionsDictionaries[date][concept]
            if type(value) == float:

                if concept[:-2] in balanceDictionary.keys():

                    balanceDictionary[concept[:-2]
                                      ] = balanceDictionary[concept[:-2]] + value
                else:
                    balanceDictionary[concept[:-2]] = value

                sum = sum + value

    individualConcept = []
    maxNumbers = []
    sortedConcepts = []

    for concept in balanceDictionary.keys():
        value = balanceDictionary[concept]
        splittedConcept = concept.split(r":")
        if not concept in sortedConcepts:
            sortedConcepts.append(str(concept))
        for i in range(0, len(splittedConcept)):
            if not (splittedConcept[i] + str(i)) in individualConcept:
                individualConcept.append(splittedConcept[i] + str(i))
                maxNumbers.append(int(i))
    
    
    sortedConcepts = sorted(sortedConcepts)
    #print(sortedConcepts)
    maxNumbers.sort()
    maxNumber = maxNumbers[-1]
    tree = Tree()
    #print(balanceDictionary.keys())
    #print("\n")
    #print(sorted(balanceDictionary.keys()))

    def buildTree():

        duplicatedCounter = int(0)
        tree.create_node("Balance", "balance")
        for wholeConcept in (balanceDictionary.keys()):
            splittedConcept = pointsListConcept(wholeConcept)
            for i in range(0, len(splittedConcept)):
                if i > 0:

                    if tree.contains(splittedConcept[i-1]) and not tree.contains(splittedConcept[i]):
                        tree.create_node(
                            splittedConcept[i], splittedConcept[i], parent=splittedConcept[i-1])
                        if i == len(splittedConcept)-1:
                            tree[splittedConcept[i]].data = balanceDictionary[wholeConcept]
                        
                    if tree.contains(splittedConcept[i]) and (tree.parent(splittedConcept[i]).identifier != splittedConcept[i-1]):
                        #print(splittedConcept[i],"duplicado en otro nodo\n" , "parent: ", splittedConcept[i-1])
                        duplicatedCounter += 1
                        nodeName = str(splittedConcept[i]) + str(duplicatedCounter)
                        tree.create_node(nodeName, nodeName, parent=splittedConcept[i-1])
                        if i == len(splittedConcept)-1:
                            tree[nodeName].data = balanceDictionary[wholeConcept]


                else:
                    if not tree.contains(splittedConcept[i]):
                        tree.create_node(
                            splittedConcept[i], splittedConcept[i], parent="balance")
                        if i == len(splittedConcept)-1:
                            tree[splittedConcept[i]].data = balanceDictionary[wholeConcept]


                

        #tree.show()

    def dataFillTree(node):

        if tree[node].is_leaf():
            return tree[node].data
        else:
            for child in tree.children(node):

                if type(tree[node].data) != float:
                    tree[node].data = float(0)

                tree[node].data += float(dataFillTree(child.identifier))
            return tree[node].data

    def printTree(node):

        if tree.get_node(node).is_leaf():
            
            if (tree[node].identifier)[-1].isdigit():
                print(r"$", str(tree[node].data).rjust(longestStringLenght), " " * tree.level(node) * 3, (tree[node].identifier)[:-1])
            else:
                print(r"$", str(tree[node].data).rjust(longestStringLenght), " " * tree.level(node) * 3, tree[node].identifier)
        else:
            if (tree[node].identifier)[-1].isdigit():
                print(r"$", str(tree[node].data).rjust(longestStringLenght), " " * tree.level(node) * 3, (tree[node].identifier)[:-1])
            
            elif tree[node].identifier != "balance":
                print(r"$", str(tree[node].data).rjust(longestStringLenght), " " * tree.level(node) * 3, tree[node].identifier)

            for child in tree.children(node):
                printTree(child.identifier)
                
    def cleanTree():
        nodeList = tree.all_nodes()
        for node in nodeList:
            nodeName = node.identifier
            if node in tree.all_nodes():
                if len(tree.children(nodeName)) == 1 and node.data == tree.children(nodeName)[0].data:
                    #print(nodeName , "has only 1 child")
                    newName = node.identifier + r":" + tree.children(nodeName)[0].identifier
                    tree.update_node(nodeName, identifier = newName, tag = newName)
                    tree.remove_node(tree.children(newName)[0].identifier)
                    #print(node)
        #tree.show()

    def addTithe(tithe):
        if not tree[tithe].is_root():
            taxedData = tree.parent(tithe).data
            taxableData = tree[Ledger.taxableValue].data
            tree.update_node(tree.parent(tithe).identifier, data= round(taxedData + taxableData * Ledger.taxValue - 0.1 , 1) )
            addTithe(tree.parent(tithe).identifier)
        if tree[tithe].is_leaf():
            tree.update_node(tithe, data= round(taxableData * Ledger.taxValue, 1) )
            
        
        
        
            
                
        
            
    def finalAddition(root):
        sum = float(0)
        for node in tree.children(root):
            sum += float(node.data)
        return sum
        

    buildTree()
    dataFillTree("balance")
    cleanTree()
    addTithe(Ledger.taxName)
    printTree("balance")
    sum = finalAddition("balance")
    sum = round(sum, 1)

    print("--" * longestStringLenght * 2)
    print(r"$", str(sum).rjust(longestStringLenght))
