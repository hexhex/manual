import dlvhex

# concat has one input parameter of type tuple (=arbitrarily many constants),
# which specifies the terms to be concatenated
def concat(tup):
	# start with empty string and append all input constants in sequence
	ret = ""
	for x in tup:
		ret = ret + x.value()

	# output the final string
	dlvhex.output((ret, ))

# computes the set of all elements in the extension
# of unary predicate p but not in that of q
def setdiff(p,q):
	# for all input atoms (over p or q)
	for x in dlvhex.getTrueInputAtoms():
		# check if the predicate is p
		if x.tuple()[0] == p:
			# check if the atom with predicate
			# being changed to q is NOT in the input
			if dlvhex.isFalse(dlvhex.storeAtom((q, x.tuple()[1]))):
				# then the element is in the output
				dlvhex.output((x.tuple()[1], ));

# register all external atoms
def register():
	# setdiff has two predicate input parametrers and its output arity is 1
	dlvhex.addAtom("setdiff", (dlvhex.PREDICATE, dlvhex.PREDICATE), 1)
	# concat has arbitrarily many input parameters
	# of type constant (=TUPLE) and its output arity is 1
	dlvhex.addAtom("concat", (dlvhex.TUPLE, ), 1)
