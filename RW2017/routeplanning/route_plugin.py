import dlvhex
import networkx as nx
import urllib as ul
import json

def route(graph,start,end):

	G = nx.read_edgelist(graph.value()[1:-1], nodetype=str, data=[('weight',float),('label',str)], create_using=nx.MultiDiGraph())
	
	shortestPath = nx.shortest_path(G, source=start.value()[1:-1], target=end.value()[1:-1], weight='weight')

	for i in range(0,len(shortestPath)-1):
		costs = 10
		for edge in G.edges(data=True):
			if edge[0] == shortestPath[i] and edge[1] == shortestPath[i+1] and edge[2]['weight'] < costs:
				costs = edge[2]['weight']
				transport = edge[2]['label']

		dlvhex.output(('"' + shortestPath[i] + '"','"' + shortestPath[i+1] + '"',int(costs),'"' + transport + '"'))

def needRestaurant(trip,limit):
	tripLength = 0
	maxTripLength = 0

	for x in dlvhex.getInputAtoms():
		if x.tuple()[0] == trip and x.isTrue():
			tripLength += int(x.tuple()[4].value())

	for x in dlvhex.getInputAtoms():
		if x.tuple()[0] == trip and not x.isFalse():
			maxTripLength += int(x.tuple()[4].value())

	if tripLength > int(limit.value()):
		dlvhex.output(())

	if tripLength <= int(limit.value()) and maxTripLength > int(limit.value()):
		dlvhex.outputUnknown(())


def getJSON(url,fields):
	jsonurl = ul.urlopen(url.value()[1:-1])
	data = json.loads(jsonurl.read())

	for field in fields:
		if field.value()[1:-1].isdigit():
			data = data[int(field.value()[1:-1])]
		else:
			data = data[field.value()[1:-1]]

	dlvhex.output(('"' + str(data) + '"', ))

def register():
	prop = dlvhex.ExtSourceProperties()
	prop.addFiniteOutputDomain(0)
	prop.addFiniteOutputDomain(1)
	prop.addFiniteOutputDomain(2)
	prop.addFiniteOutputDomain(3)
	dlvhex.addAtom("route", (dlvhex.CONSTANT, dlvhex.CONSTANT, dlvhex.CONSTANT ), 4, prop)

	prop = dlvhex.ExtSourceProperties()
	prop.addMonotonicInputPredicate(0)
	prop.setProvidesPartialAnswer(True)
	dlvhex.addAtom("needRestaurant", (dlvhex.PREDICATE, dlvhex.CONSTANT ), 0, prop)

	prop = dlvhex.ExtSourceProperties()
	prop.setFunctional(True)
	dlvhex.addAtom("getJSON", (dlvhex.CONSTANT, dlvhex.TUPLE ), 1, prop)





