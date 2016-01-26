#Visualize the feedback from mid-course survey
from __future__ import print_function
from pylab import *
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.style.use('ggplot')
import numpy as np

from time import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF


def sieve(strlist):
    out = []
    for s in strlist:
        if not any([s in r and s!=r for r in strlist]):
            out.append(s)
    return out

def ngrams(inpur, n):
    inpur = inpur.split(" ")
    outpur = []
    for i in range(len(inpur) -n+1):
        outpur.append(inpur[i:i+n])
    return outpur

if __name__ == "__main__":
    """
    #Open the  file containing the data we want to plot
    data = pd.read_excel('SURVEY.xlsx')
    keys = [1,2,3,4]
    titles = ["How do you like the course so far? \n [1-7 with 7 being very enjoyable]", "Do you feel this course connects well with the main data science course? \n [1-7 with 7 being very connected]", "Does this course make you feel like pursiong cognitive science in the fututre? \n [1-7 with 7 being very likely]", "Are you comfortable with the course load? \n [1-7 with 7 being too much and 1 being too little and 4 being just right]", "What would you like to see more or less in this course?", "What is your (intended) major(s)?"]
    for i in range(4):

        #We are going to make 4 histograms, for the first 4 numerical responses
        d = data[keys[i]]     
        t = titles[i]
        ylab = "Amount of Responses"
        xlab = "Student Rating"
        p = d.plot(kind='hist',xlim=(0,7), figsize=(8,8))
        p.set_title(t)
        p.set_xlabel(xlab)
        p.set_ylabel(ylab)
        plt.show()

    #Make a pie chart for quesion 6
    d = data[6]
    print(d)
    t = titles[5]
    reason_counts = d.value_counts()
    print(reason_counts)
    counts = list(reason_counts)
    categories = list(reason_counts.keys())
    pie(counts, labels=categories, autopct='%1.1f%%', startangle=90)
    title(t)
    plt.show()
    """   
     
    n_samples = 20000
    n_features = 10000
    n_topics = 5
    n_top_words = 10
    #d = data[5] + data["1_w"]
    #d_list = [a for a in data[5]]
     
    #Extract topics from question 5
     
    #d_list = [a for a in data[q].dropna()]
    dlist = [a.strip() for a in open("alice.txt", "r")]
    x = dlist
    x = [i+ " " +j for i,j in zip(x[::2], x[1::2])]
    x = [i+ " " +j for i,j in zip(x[::2], x[1::2])]
    x = [i+ " " +j for i,j in zip(x[::2], x[1::2])]
    x = [i+ " " +j for i,j in zip(x[::2], x[1::2])]
    x = [i+ " " +j for i,j in zip(x[::2], x[1::2])]
    d_list = x
    #d_list = " ".join(bug)
    print(d_list[:30])
    #d_list.extend([gg for gg in data[q].dropna()])

    vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=n_features, stop_words='english')
    tfidf = vectorizer.fit_transform(d_list)
    nmf = NMF(n_components=n_topics, random_state=1).fit(tfidf)
    feature_names = vectorizer.get_feature_names()
    
    for topic_idx, topic in enumerate(nmf.components_):
        print("Topic #%d:" % topic_idx)
        t = [feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
        found = []
        t = sieve(t)
        for feature in t:
            print(feature)
        for feature in t:
            for comment in d_list:
                if feature in comment:
                    #print("@@" + comment + "\n")
                    pass
        print(",".join(t))
        print()
    

    """
    #now extract topics in all other written commentary
    ql = ["1_w", "2_w", "3_w", "4_w", "5_w", "6_w"]

    d_list = []
    for qll in ql:
        d_list.extend([gg for gg in data[qll].dropna()])

    #extract all strings from the data structure
    vectorizer = TfidfVectorizer(ngram_range=(1,2),max_features=n_features, stop_words='english')
    tfidf = vectorizer.fit_transform(d_list)
    nmf = NMF(n_components=n_topics, random_state=1).fit(tfidf)
    feature_names = vectorizer.get_feature_names()

    for topic_idx, topic in enumerate(nmf.components_):
        print("Topic #%d:" % topic_idx)
        t = [feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
        found = []
        t = sieve(t)
        for feature in t:
            print(feature)
        for feature in t:
            for comment in d_list:
                if feature in comment:
                    print("@@" + comment + "\n")
                    pass
        print(",".join(t))
        print()
    """
    print("Success!")
