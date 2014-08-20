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

global_cities = [tuple(i[1:3]) for i in data[8:]]
CityPop = len(global_cities) 

def algorithm_choice():
	if sys.argv[1] == "1":
		Path = random_walk()
		print measure(Path)
		grapher(Path)
	elif sys.argv[1] == "2":
		Path = nearest_neighbor()
		print measure(Path)
	elif sys.argv[1] == "42":
		Path = random_walk()
		print manhattan_measure(Path)
		grapher(Path)
	else: 
		print "This salesman only walks randomly, shortsightedly, and along funny metrics."


"""

Brute force optimization by doing repeated iterations of the random_walk()
For some reason each iteration returns the same value
(Same basic structure as manhattan_search())

def random_search():
	shortest_path = []
	shortest_length = 10**100
	for i in range(0,3):
		w = random_walk()
		print measure(w)
		grapher(w)
		quit()
		if measure(w) < shortest_length:
			shortest_length = measure(w)
			shortest_path = w
		w = []
	print shortest_length
	
	grapher(shortest_path)

"""

def random_walk():
	cities = global_cities
	Path = []
	while len(cities) > 1:
		next_step = random.randint(0,len(cities)-2)
		Path.append(cities[next_step])
		del cities[next_step]
	
	return Path

"""
def manhattan_random_search():
	shortest_path = []
	shortest_length = 10**100
	for i in range(0,3):
		w = random_walk()
		print manhattan_measure(w)
		quit()
		if manhattan_measure(w) < shortest_length:
			shortest_length = manhattan_measure(w)
			shortest_path = w
		w = []
	print shortest_length
	
	grapher(shortest_path)
"""
# Get the loops right
# DEBUG THE CITY TUPLES IF NEED BE -- THAT'S PROBABLY WHERE THE PROBLEM IS


def nearest_neighbor():
	nearest_distance = 10000000
	cities = global_cities

	Path = []
	first_step = random.randint(0,len(cities)-2)

	Path.append(cities[first_step])
	del cities[first_step]

	while len(cities) > 1:
		for i in range(0,len(cities)-1):
			d = [Path[-1],cities[i]]
			print d
			print neighbor_measure(d)
			
			if neighbor_measure(d) < nearest_distance:
				near_index = i
				nearest_distance = neighbor_measure(d)
		Path.append(cities[near_index])
		del cities[near_index]

		print len(cities)
		print "Next Step"

	return Path

def measure(Path_Tuples):
	distance = 0
	for x in range(0,len(Path_Tuples)-2):
		distance += round(( (float(Path_Tuples[x][0]) - float(Path_Tuples[x+1][0]))**2 + (float(Path_Tuples[x][1]) - float(Path_Tuples[x+1][1]))**2 )**.5)
	return distance

def neighbor_measure(Path_Tuples):
	distance = 0
	distance += round(( (float(Path_Tuples[0][0]) - float(Path_Tuples[1][0]))**2 + (float(Path_Tuples[0][1]) - float(Path_Tuples[1][1]))**2 )**.5)
	return distance

def manhattan_measure(Path_Tuples):
	distance = 0
	for x in range(0,len(Path_Tuples)-2):
		distance += abs(float(Path_Tuples[x][0]) - float(Path_Tuples[x+1][0])) + abs(float(Path_Tuples[x][1]) - float(Path_Tuples[x+1][1]))
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
