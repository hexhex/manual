import dlvhex
# Networkx library is used to handle graph tasks
import networkx as nx


# External atom starts, similar to regular function  in Java, C etc.
# edges is name of the function and person is input parameter coming to it 
def edges(currentNode):
  # Sources will be loaded from the file
  g = nx.read_weighted_edgelist("example_4_3.edgelist", nodetype=str,create_using=nx.DiGraph())
  # Take successor nodes of the current node
  friendList = g.successors(currentNode.value())
  # Output the successors
  for node in friendList:
    dlvhex.output((node,)) #sends city and weight to the output
  dlvhex.output((currentNode.value(),)) #sends city and weight to the output

def check(V,U,time,agentNo):
    dlvhex.output(('valid',))

# Register function
def register():
  prop = dlvhex.ExtSourceProperties()
  prop.addFiniteOutputDomain ( 0 )
  dlvhex.addAtom("edges",(dlvhex.CONSTANT,), 1, prop)
  dlvhex.addAtom("check",(dlvhex.CONSTANT, dlvhex.CONSTANT, dlvhex.CONSTANT, dlvhex.CONSTANT,), 1, prop)
