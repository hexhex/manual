import dlvhex

# concat has one input parameter of type tuple (=arbitrarily
# many constants), which specifies the terms to be concatenated
def concat(tup):
  # start with empty string and sequentialy append all inputs
  ret = ""
  for x in tup:
    ret = ret + x.value()

  # output the final string
  dlvhex.output((ret, ))
# register all external atoms
def register():
  # concat has arbitrarily many input parameters
  # of type constant (=TUPLE) and its output arity is 1
  dlvhex.addAtom("concat", (dlvhex.TUPLE, ), 1)
