import dlvhex
import networkx as nx # for graphs

def edges(currentNode):
  # hardcoded source for graph
  g = nx.read_weighted_edgelist("example_4_pathfind.graph",
        nodetype=str,create_using=nx.DiGraph())
  # output successors
  for node in g.successors(currentNode.value()):
    dlvhex.output( (node,) )

def check(A,V,U):
  if A.value()=='1' and V.value()=='two' and U.value()=='five':
    pass # no path = no tuple = atom false
  else:
    # empty tuple = true, no tuple = false
    dlvhex.output( () )

# Register function
def register():
  prop = dlvhex.ExtSourceProperties()
  prop.addFiniteOutputDomain(0)
  dlvhex.addAtom("edges",(dlvhex.CONSTANT,), 1, prop)
  dlvhex.addAtom("check",
    (dlvhex.CONSTANT, dlvhex.CONSTANT, dlvhex.CONSTANT), 0)
