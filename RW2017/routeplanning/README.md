# Route Planning Example

This example demonstrates the usage of external atoms in dlvhex for semantic route planning, where the goal is to find the shortest trip visiting a given set of locations in the city of Vienna under several side constraints.

## Running the Program

The example requires [dlvhex 2.5](http://www.kr.tuwien.ac.at/research/systems/dlvhex/) and the [DL-Lite plugin](https://github.com/hexhex/dlliteplugin) for dlvhex to be installed. The program can then be executed with the following command from this directory:

dlvhex2 route_planning.hex --python-plugin=route_plugin.py --maxint=11 --aggregate-mode=extbl --filter=sequence

If the DL-Lite plugin is not available, the encoding in the file route_planning_without-dl.hex can be used instead.

## Using hexlite

The program can also be executed with the [hexlite](https://github.com/hexhex/hexlite) solver, but the files route_planning_hexlite.hex and route_plugin_hexlite.py have to be used in this case because hexlite uses Python 3 and the DL-Lite plugin is not available in this case.

