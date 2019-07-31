# TriadCounter
# Language: Python
# Input: CSV (signed, weighted network)
# Output: Screen (statistics)
# Tested with: PluMA 1.0, Python 3.6

PluMA plugin to take a signed, weighted network and output the number of stable
and unstable triads, a useful metric for social network research (Easley, 2010).

This plugin expects input in CSV format, where rows and columns each correspond to
nodes and entries in the matrix to edges; for example A(i, j) would be the weight
of the edge from node i to node j.  A weight of zero means no edge.

Stable social networks have triads that are all stable, meaning that the number
of positive edges is odd (either 3 or 1).  This implies that in stable social networks,
nodes with common friends or enemies should be also friends (not enemies).
