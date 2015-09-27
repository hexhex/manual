import dlvhex
import networkx as nx # for graph tasks

# get edges from given node in given file
def edges(fileName, currentNode):
  # Sources will be loaded from the file
  g = nx.read_weighted_edgelist(fileName.value().strip('"'),
          nodetype=str, create_using=nx.DiGraph())
  # Output successor nodes of the current node including weight
  for node in g.successors(currentNode.value()):
    weight = g[currentNode.value()][node]['weight']
    # produce one output tuple
    dlvhex.output( (node,int(weight)) )
    
def register():
  prop = dlvhex.ExtSourceProperties()
  # specify that "edges" produces finite set of output tuples
  prop.addFiniteOutputDomain(0)
  dlvhex.addAtom("edges",(dlvhex.CONSTANT,dlvhex.CONSTANT),2,prop)
