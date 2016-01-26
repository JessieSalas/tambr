import pickle
import glob
import numpy as np
import cPickle

class EntityComparer:
    """
    Various methods for comparing entities with word embeddings
    """
    def __init__(self,vectorfile, words):
        #load the vector dictionary form vectorfile
        with open(vectorfile,'rb') as infile: 
            print ('loading vectors...')
            self.vectors = cPickle.load(infile)
            print ('loaded!')

        #populate internal patches dictionary
        patches = {}     
        all_patches = []
        for filename in glob.glob('./synths/*.txt'): 
            print filename
            patchname = filename.split('/')[-1]
            mine = [line.lower().strip() for line in open(filename, 'r')]
            patches[patchname] = mine
            all_patches.extend(mine)

        self.patches = all_patches 
        self.words = all_patches    

    def distance(self, v1, v2):
        """
        returns the cosine distance between two vectors.
        """
        return np.dot(v1, v2) / (np.sqrt(np.dot(v1, v1)) * np.sqrt(np.dot(v2, v2)))

    def nNearest(self, entity, n=10):
        """
        for any entity, which could be multiple words long,
        return the n most similar keys from v_dict, in terms of the values of v_dict.

        keys of v dict are words or phrases

        values of v dict are word embedding vectors

        entity is a string
         
        """
        vectors = self.getVectors()
        all_words = self.getWords() 

        content = entity.split()
        conjoined = "_".join(content)

        #setup empty list to populate with cosine distances
        cosine_distances = []

        if conjoined in vectors:
            word_vec = vectors[conjoined]
            for possible_match in all_words:

                content2 = possible_match.split()
                conjoined2 = "_".join(content2)

                if conjoined2 in vectors: 

                    other_vec = vectors[conjoined2]

                    d = self.distance(word_vec,other_vec)
                    package = (d, possible_match)
                    cosine_distances.append(package)
                        

                else:
                    distance_list = []
                    for word2 in content2:
                        if word2 in vectors:
                            other_vec = vectors[word2]
                            d = self.distance(word_vec,other_vec)
                            distance_list.append(d)
                            
                    if len(distance_list) != 0:
                        entity_distance = sum(distance_list) / (1.0 * len(distance_list))
                        package = (entity_distance, possible_match)
                        cosine_distances.append(package)
                    
                    else:
                        pass
                        #in this last case, neither the entire entity nor any element of 
                        #the entity was found
            
        else:
            #now we compute the pairwise distance 
            for possible_match in all_words:

                content2 = possible_match.split()
      E.          conjoined2 = "_".join(content2)




                if conjoined2 in vectors: 

                    other_vec = vectors[conjoined2]

                    distance_list = []
                    for word in content:
                        if word in vectors: 
                            word_vec = vectors[word]
                            d = self.distance(word_vec,other_vec)
                            distance_list.append(d)
                            
                    if len(distance_list) != 0:
                        entity_distance = sum(distance_list) / (1.0 * len(distance_list))
                        package = (entity_distance, possible_match)
                        cosine_distances.append(package)
           




                else:
                    distance_list = []
                    for word2 in content2:
                        if word2 in vectors:
                            other_vec = vectors[word2]





                            distance_list2 = []
                            for word in content:
                                if word in vectors: 
                                    word_vec = vectors[word]
                                    d = self.distance(word_vec,other_vec)
                                    distance_list2.append(d)
                                    
                            if len(distance_list) != 0:
                                entity_distance2 = sum(distance_list) / (1.0 * len(distance_list2))
                                package = (entity_distance2, possible_match)
                                cosine_distances.append(package)
                            







                            
                    if len(distance_list) != 0:
                        entity_distance = sum(distance_list) / (1.0 * len(distance_list))
                        package = (entity_distance, possible_match)
                        cosine_distances.append(package)
                    

        sorted_distances = [e for e in reversed(sorted(cosine_distances))]
        
        print('aye')
        return sorted_distances

    def getVectors(self):
        """
        returns the vector dictionary
        """
        return self.vectors              

    def pairwiseDistance(self, v):
        """
        returns a matrix containing the pairwise distance of a dictionary
        """
        M = np.zeros( (len(v), len(v)))
        for i in range(len(v)):
            print i
            for j in range(len(v)):
                d = distance(vectors[v[i]], vectors[v[j]])
                M[i][j] = d
        return M


    def pairwiseDistance(self,v):
        """
        returns a matrix containing the pairwise distance of a dictionary
        """
        M = np.zeros( (len(v), len(v)))
        for i in range(len(v)):
            print i
            for j in range(len(v)):
                d = distance(vectors[v[i]], vectors[v[j]])
                M[i][j] = d
        return M

    def getWords(self):
        """
        Return internal words list
        """
        return self.words


if __name__ == "__main__":
    v_file = 'vectors_100k2.pickle'
    all_words = [line.strip() for line in open('./tags.txt', 'r')]

    E = EntityComparer(v_file, all_words)

    #loading all the patches into a dictionary 

    """
    patches = {}
    ofof = 0
    fafa = 0

    for filename in glob.glob('./synths/*.txt'): 
        print filename
        patchname = filename.split('/')[-1]
        patches[patchname] = [line.lower().strip() for line in open(filename, 'r')]
        for p in patches[patchname]:
            found = False
            for sub in p.split():
                if sub in vectors:
                    found = True
            if found: 
                fafa += 1
            else:
                print(p)
            ofof +=1
    print "{0} patches found".format(fafa)
    print "{0} patches total".format(ofof)

    """
    b = E.nNearest("mars", 10)
    print b[:20]
