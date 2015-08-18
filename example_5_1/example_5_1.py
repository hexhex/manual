import dlvhex
# Networkx library is used to handle graph tasks.
import networkx as nx

# External atom implementation is similar to regular function  in Java, C etc.
# friendsOfDegree is name of the function and persons name is input parameter (personOfInterest) 
# for each personOfInterest external atom will return its direct friends
 
def friendsOfDegree(personOfInterest):
  # graph of the friends will be loaded from the external file
  g = nx.read_weighted_edgelist("example_2_1.edgelist", nodetype=str,create_using=nx.DiGraph())

  # Take successor nodes of the node of interest.
  friendList = g.successors(personOfInterest.value())
  # Output the successor nodes
  for node in friendList:
    dlvhex.output((node,)) # outputs direct fiends
    
# Register function
def register():
  prop = dlvhex.ExtSourceProperties()
  prop.addFiniteOutputDomain ( 0 )
  dlvhex.addAtom("friendsOfDegree", (dlvhex.CONSTANT,), 1, prop)
