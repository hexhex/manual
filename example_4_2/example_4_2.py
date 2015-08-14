import dlvhex
# Networkx library is used to handle graph tasks
import networkx as nx

# External atom starts, similar to regular function  in Java, C etc.
# edges is name of the function and person is input parameter coming to it 
def edges(currentNode):
  # Sources will be loaded from the file
  g = nx.read_weighted_edgelist("example_4_2.edgelist", nodetype=str,create_using=nx.DiGraph())

  # Take successor nodes of the current node
  friendList = g.successors(currentNode.value())
  # Output these successors
  # Find weight in the graph for edge currentNode ---> successorNode
  # Output that node with its weight
  for node in friendList:
    j=g[currentNode.value()][node]['weight'] # I WANT TO OUPUT J WHICH IS WEIGHT AS WELL#
    dlvhex.output((node,int(j))) #sends city and weight to the output
    
# Register function
def register():
  prop = dlvhex.ExtSourceProperties()
  prop.addFiniteOutputDomain ( 0 )
  dlvhex.addAtom("edges", (dlvhex.CONSTANT,), 2, prop)
