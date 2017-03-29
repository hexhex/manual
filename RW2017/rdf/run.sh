#!/bin/bash

DLVHEX=dlvhex2

#$DLVHEX --python-plugin=rdfplugin.py test.hex $*
$DLVHEX --python-plugin=rdfplugin.py livejournal.hex --filter=knows $*

