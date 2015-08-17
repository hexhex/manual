import dlvhex

# Python plugin implementation for the rq external atom.
def rq(predic):
  for x in dlvhex.getTrueInputAtoms():
    io = {'ind':'money','amalB':'goggles','altD':'yogamat','gansD':'money'}
    inp = x.tuple()[1].value()
    if predic == x.tuple()[0]:
      if inp in io:
        dlvhex.output((io[inp],))

# register function
def register():
  dlvhex.addAtom("rq", (dlvhex.PREDICATE, ), 1)
