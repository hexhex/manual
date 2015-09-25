import dlvhex

# concat has one input parameter of type tuple
# (=arbitrarily many constants),
# which specifies the terms to be concatenated
def concat(tup):
  # start with empty string
  ret = ""
  for x in tup:
    # append all input constants in sequence
    ret = ret + x.value()
  # output the final string
  dlvhex.output( (ret,) )

# computes the set of all elements in the
# extension of unary predicates p minus q
def setdiff(p, q):
  # go over all input atoms (p or q)
  for x in dlvhex.getTrueInputAtoms():
    # get predicate/argument of atom
    pred, arg = x.tuple() # pred(arg)
    # check if x is of form p(arg)
    if pred == p:
      # produce atom q(arg)
      qatom = dlvhex.storeAtom( (q, arg) )
      # check q(arg) is NOT in input
      if dlvhex.isFalse(qatom):
        # then put arg into the output
        dlvhex.output( (arg,) )

# computes the extension of unary predicates p and q
# returns unique pairing between sorted elements
def sortandmap(p, q):
  # get all tuples
  tuples = [ x.tuple() for x in dlvhex.getTrueInputAtoms() ]
  # p and q tuples
  ptuples = filter(lambda x: x[0] == p, tuples)
  qtuples = filter(lambda x: x[0] == q, tuples)
  # sorted p and q extensions
  pext = sorted(map(lambda x: x[1], ptuples))
  qext = sorted(map(lambda x: x[1], qtuples))
  # output all pairs
  for out in zip(pext, qext):
    dlvhex.output(out)

# register external atoms
def register():
  # setdiff has two predicate input parameters
  # and its output arity is 1
  dlvhex.addAtom("setdiff",
    (dlvhex.PREDICATE, dlvhex.PREDICATE), 1)
  # concat has arbitrarily many input parameters
  # of type constant (=TUPLE) and its output arity is 1
  dlvhex.addAtom("concat", (dlvhex.TUPLE,), 1)
  # sortandmap has two predicate input parameters
  # and its output arity is 2
  dlvhex.addAtom("sortandmap",
    (dlvhex.PREDICATE, dlvhex.PREDICATE), 2)
