import dlvhex
import networkx as nx # for graph tasks.

# An external atom implementation is similar to a regular function
# in Java, C, etc. friendsOfDegree is name of the function which
# has one input parameter (personOfInterest). For each
# personOfInterest external atom will return its direct friends.
def friendsOfDegree(personOfInterest):
  # graph of the friends will be loaded from the external file
  g = nx.read_weighted_edgelist("example_2_1.edgelist",
    nodetype=str,create_using=nx.DiGraph())

  # Take successor nodes of the node of interest.
  friendList = g.successors(personOfInterest.value())
  # Output the successor nodes
  for node in friendList:
    dlvhex.output( (node,) ) # outputs (tuple of size one)
    
# Register function
def register():
  prop = dlvhex.ExtSourceProperties()
  prop.addFiniteOutputDomain(0) # specify that the graph is finite
  dlvhex.addAtom("friendsOfDegree", (dlvhex.CONSTANT,), 1, prop)
