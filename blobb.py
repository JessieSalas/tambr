from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
from pylab import *

bug = [a for a in open("pan.txt", "r")]
d_list = " ".join(bug)


canvas = plt.figure()
rect = canvas.patch
rect.set_facecolor('white')





text = "My life is a fucking dump. I hate all of my meaningless crap. I don't want to live a shitty life anymore. This horrible and bad crap keeps getting worse. Maybe it isn't that bad. Actually it is kind of neutral. Really, life is not that bad. Life is okay. Life is mediocre. I'm doing alright. I can at least say I'm here. I am pretty fortunate to be at this place. I am more than okay, I'm actually great! I am in love with life. Every minute of my happy life gets better and better! I love everything! LOVE IS LIFE AND GOOD LIVE LOVE HAPPY! HAPPY!"

blob = TextBlob(d_list)
#blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
#  ('threat', 'NN'), ('of', 'IN'), ...]

#blob.noun_phrases   # WordList(['titular threat', 'blob',
#            'ultimate movie monster',
#            'amoeba-like mass', ...])

sent = []
for sentence in blob.sentences:
    print sentence
    s = sentence.sentiment.polarity
    print s
    sent.append(s)

sent = sent
print('sent')
x =  np.array([i for i in range(len(sent))])
print('sent')
"""
x_smooth = np.linspace(x.min(), x.max(), 200)
print('sent')
y_smooth =  spline(x, sent, x_smooth)
print('sent')

sp1 = canvas.add_subplot(1,1,1, axisbg='w')

sp1.plot(x_smooth, y_smooth, 'red', linewidth=1)

plt.tight_layout()
plt.grid(alpha=0.8)
"""
print('sentiment')
print( str( sum(sent) / len(sent)   ))
#plt.scatter(x,sent)
plt.hist(sent, bins=100, normed=True)
plt.show()
#plt.show()
