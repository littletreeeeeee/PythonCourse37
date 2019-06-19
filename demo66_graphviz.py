import graphviz as gv
import itertools

list1 = list('ABCDEFGH')

#g1 = gv.Graph(format='svg')
g1 = gv.Digraph(format='svg')
for i in list1:
    g1.node(i)

# edges = [e for e in itertools.permutations(list1, 2)] #排列
edges = [e for e in itertools.combinations(list1, 2)] #組合

for e0, e1 in edges:
    g1.edge(e0, e1)
g1.render('graph\\demo66')