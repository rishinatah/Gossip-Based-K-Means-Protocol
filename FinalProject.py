#!/usr/bin/env python

from networkx import *
from math import *
import sys
import random
#import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

#scikit

#from sklearn.cluster import KMeans
#from sklearn import *

G = nx.read_adjlist("cit-HepPh.txt",comments = '#');

# This is the number of citations : Deg = nx.degree(G);
nodes = G.nodes();

citationNumber = {};

#Dictionary for sotring number of citations
for n in nodes:
	citationNumber[n] = G.degree(n);

#Modified Averaging Gossip Algorithm

for i in nodes : 
	neighbors = G.neighbors(i)
	for j in neighbors : 
		if abs(citationNumber[i] - citationNumber[j]) <= 5 :
			newAvgVal = (citationNumber[j] + citationNumber[i])/2;
			citationNumber[i] = newAvgVal;
			citationNumber[j] = newAvgVal;
			#gossip percolation by pairwise information exchange

#K - Means Clustering 

#value of k
k = 10;

#find seeds/centroids

s = {};
clusterSet = {};

for i in range(1,k + 1) :
	s[i] = random.choice(citationNumber.keys());
	clusterSet[s[i]] = [];

#K - means algorithm
#We have used only one itertion of the K-means algorithm here. 

def kmeans(data):
	for i in data.keys():
		metric = [];
		for j in range(1,k+1):
			distMetric = abs(data[i] - data[s[j]]);
			metric.append(distMetric);
		minDist = min(metric);
		metricIndex = metric.index(minDist);
		clusterSet[s[metricIndex+1]].append(i);

kmeans(citationNumber);

#print clusterSet;

for i in range(1,k+1): 
	print "The cluster centroid is : \n";
	print s[i];
	print "\n";
	print "The nodes in this cluster : \n";
	print clusterSet[s[i]];
	print "\n";
	
