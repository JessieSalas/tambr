#Functions pertaining to similarity between topics
import cPickle as pickle
from scipy.spatial import distance as dist
import numpy
"""
def distance(w1,w2):
    '''
    Gets euclidian distance between two word vectors
    w1:
        string word
    w2:
        string word
    ''' 
    return dist.euclidean(w1,w2)
"""

def distance(v1, v2):
    return np.dot(v1, v2) / (np.sqrt(np.dot(v1, v1)) * np.sqrt(np.dot(v2, v2)))

def nNearest(w, n=10):
    """
    returns the n nearest (most similar) words
    for a given word w 
    """
    if w in vectors:
        vw = vectors[w]
        for w2 in vectors.keys():
            d = distance(w2,w1)
    else:
        raise Exception('Not found!')

def pairwiseDistance(v):
    """
    returns a matrix containing the pairwise distance of a dictionary
    """
    M = numpy.zeros( (len(v), len(v) ))
    keys = v.keys()
    for i in range(len(keys)):
        print i
        for j in range(len(keys)):
            d = distance(v[keys[i]], v[keys[j]])
            M[i][j] = d
    return M

if __name__ == "__main__":
    with open('vectors_100k.pickle','rb') as infile: 
        print ('loading vectors...')
        vectors = pickle.load(infile)
        print ('loaded!')
    D = pairwiseDistance(vectors)
