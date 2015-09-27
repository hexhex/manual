import dlvhex

RES = { 'ind':'money', 'amalB':'goggles',
        'altD':'yogamat', 'gansD':'money'}

# return required resources given swimming locations
def rq(loc_pred):
  for x in dlvhex.getTrueInputAtoms():
    arg = x.tuple()[1].value() # get argument
    if loc_pred == x.tuple()[0]: # check predicate
      if arg in RES:
        dlvhex.output( (RES[arg],) )

# register external atom
def register():
  dlvhex.addAtom("rq", (dlvhex.PREDICATE,), 1)
