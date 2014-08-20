# random and nearest neighbor reqs
# sample.tsp -- 709 random, 669 nearest neighbor, 550 letter of rec
# https://github.com/ga-students/DS-LA-03/wiki/Lesson-02-Assignment-Traveling-Salesman-Problem
# Manhattan salesman

import sys, getopt
import random
import networkx as nx
import matplotlib.pyplot as plt

with open(sys.argv[2]) as raw_file:
	data = []
	for line in raw_file:
		data.append(line.split())

global_cities = data[8:]
CityPop = len(global_cities) 



def algorithm_choice():
	if sys.argv[1] == "1":
		random_search()
	elif sys.argv[1] == "2":
		nearest_neighbor()
	elif sys.argv[1] == "42":
		nearest_neighbor()
	else: 
		print "This salesman only walks randomly, shortsightedly, and along funny metrics"

def random_search():
	shortest_path = []
	shortest_length = 10**100
	for i in range(0,3):
		w = random_walk()
		print measure(w)
		if measure(w) < shortest_length:
			shortest_length = measure(w)
			shortest_path = w
		w = []
	print shortest_length
	
	grapher(shortest_path)

def random_walk():
	cities = global_cities
	print cities
	Path = []
	while len(cities) > 1:
		next_step = random.randint(0,len(cities)-2)
		Path.append(cities[next_step])
		del cities[next_step]
	Path_Tuples = [tuple(i[1:3]) for i in Path]
	
	
	return Path_Tuples

"""
def nearest_neighbor():
	cities = global_cities
	while len(cities) > 1:
		first_step = random.randint(0,len(cities)-2)
		Path.append(cities[first_step])
		del cities[first_step]
		for i in cities:

		next_step = 
		Path.append(cities[next_step])
		del cities[next_step]
	Path_Tuples = [tuple(i[1:3]) for i in Path]
	return Path_Tuples

"""

def measure(Path_Tuples):
	distance = 0
	for x in range(0,len(Path_Tuples)-2):
		distance += ( (int(Path_Tuples[x][0]) - int(Path_Tuples[x+1][0]))**2 + (int(Path_Tuples[x][1]) - int(Path_Tuples[x+1][1]))**2 )**.5
	return distance

def manhattan_measure(Path_Tuples):
	distance = 0
	for x in range(0,len(Path_Tuples)-2):
		distance += abs(int(Path_Tuples[x][0]) - int(Path_Tuples[x+1][0])) + abs(int(Path_Tuples[x][1]) - int(Path_Tuples[x+1][1]))
	return distance

#play around with this to get the right graph type http://networkx.github.io/documentation/latest/examples/drawing/random_geometric_graph.html

def grapher(path):
	# extract nodes from graph
    nodes = set([n1 for n1, n2 in path] + [n2 for n1, n2 in path])

    # create networkx graph
    G=nx.Graph()

    # add nodes
    for node in nodes:
        G.add_node(node)

    # add edges
    for edge in path:
        G.add_edge(edge[0], edge[1])

    # draw graph
    pos = nx.shell_layout(G)
    nx.draw(G, pos)

    # show graph
    plt.show()


algorithm_choice()

print "You should also try option 42.  But only if you've ever travelled in Manhattan ;)"

"""

def euclidean_distance():
	return ((x1-x2)**2+(y1-y2)**2


def manhattan_distance():
	return abs(x1-x2)+abs(y1-y2)

"""






"""

A theoretically more generalizable path opening procedure that I got from: 
http://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-a-python-script

getting the followig

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname('sample.tsp')))

print location


"""
