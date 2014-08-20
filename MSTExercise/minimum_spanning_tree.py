import sys, getopt
import random
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter 

with open(sys.argv[1]) as raw_file:
	data = []
	for line in raw_file:
		data.append(line.split())
        
        
number_nodes = int(data[0][0])
number_edges = int(data[1][0])
network = data[2:]

def Grapher(network):

    G=nx.Graph()

    #for each point in
    #add each[0],each[1],weight=each[2]

    for point in network:
        G.add_edge(point[0],point[1],weight=point[2])

    #print number of edges and nodes
    print "The number of nodes in the MST is " + str(G.number_of_nodes())
    print "The number of edges in the MST is " + str(G.number_of_edges())


    elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.3]
    esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.3]

    pos=nx.spring_layout(G) # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G,pos,node_size=700)

    # edges
    nx.draw_networkx_edges(G,pos,edgelist=elarge,
                    width=6)
    nx.draw_networkx_edges(G,pos,edgelist=esmall,
                    width=6,alpha=0.5,edge_color='b',style='dashed')

    # labels
    nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

    plt.axis('off')
    plt.savefig("weighted_graph.png") # save as png
    plt.show() # display

def ReverseDelete(network):
    #sort edges in decreasing weight
    sorted_network = sorted(network, key=itemgetter(2), reverse=True)
    
    MST=nx.Graph()
    for point in sorted_network:
        MST.add_edge(point[0],point[1], key=None)
    
    
#issue is that deleting the item will shift the order and thus FUCK up my process the little fucker fuck

    test_network = sorted_network
    MST = sorted_network
    
    for i in range(len(sorted_network)):
        test_network = [x for x in test_network if x != sorted_network[i]]
        
        test=nx.Graph()
        for point in test_network:
            test.add_edge(point[0],point[1], key=None)
            
        #check if connected AND has same number of nodes
        if nx.is_connected(test) == True and test.number_of_nodes() == number_nodes:
            MST = [x for x in MST if x != sorted_network[i]]
        
        #reset test network so that we're not exploring an arbitrarily truncated graph
        test_network = MST
    
    print "This is the minimum spanning tree"
    print MST
    sum = 0
    for weight in MST:
        sum += float(weight[2])
    print "the total weight is " + str(sum)
    Grapher(MST)
        
ReverseDelete(network)