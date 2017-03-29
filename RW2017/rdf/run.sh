#!/bin/bash

DLVHEX=dlvhex2

#$DLVHEX --python-plugin=rdfplugin.py test.hex $*
#$DLVHEX --python-plugin=rdfplugin.py livejournal-knows.hex --filter=knows $*
$DLVHEX --python-plugin=rdfplugin.py livejournal-explore.hex --filter=explore_upto $*

