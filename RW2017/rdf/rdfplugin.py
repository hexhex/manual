# set TEST=True to test rdflib without HEX
TEST=False

if not TEST:
  import dlvhex
import rdflib

def rdf(url):
  '''
  input: URL
  outputs: S P O of all RDF triples found at URL
  '''
  g = rdflib.Graph()
  g.parse(url.value().strip('"'))
  for s, o, p in g.triples((None,None,None)):
    #print repr([s, o, p])
    dlvhex.output(tuple([ '"'+str(v)+'"' for v in [s, o, p]]))

def register():
	prop = dlvhex.ExtSourceProperties()
	prop.addFiniteOutputDomain(0)
	prop.addFiniteOutputDomain(1)
	prop.addFiniteOutputDomain(2)
	dlvhex.addAtom("rdf", (dlvhex.CONSTANT,), 3, prop)

def testrdflib():
  URL = 'http://njh.me/foaf.rdf'
  #URL = 'file:///home/ps/Downloads/njh.foaf.rdf'

  g = rdflib.Graph()
  g.parse(URL)
  for s, o, p in g.triples((None,None,None)):
    print repr([s, o, p])

if TEST:
  testrdflib()
