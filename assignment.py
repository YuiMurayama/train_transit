# coding=utf-8
import networkx as nx
import sys
import json

# import matplotlib.pylab as plt
with open('sample.json', 'r') as f:
  obj = json.load(f)

G = nx.Graph()

for num in range(0,len(obj)):
  G.add_cycle(obj[num]['Stations'])


path = nx.shortest_path(G,source=u"新宿",target=u"学芸大学")
print "駅数は",len(path)

for num in range(0,len(path)):
  sys.stdout.write("".join(path[num]))
  sys.stdout.write("⇨")


# print ",".join(path)

