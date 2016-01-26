#generates music based on emotion parameters
import numpy as np
import random
from pprint import pprint
from midiutil.MidiFile import MIDIFile 

'''
def getLogFunctionFromPoints(x1, y1, x2, y2):
    """
    Returns a logarithmic function 
    """
    """
 
    x1 = x1 + 2
    x2 = x2 + 2

    a = (    (y1-y2 )/np.log( x1 / x2  )) 

    b = (  np.exp(    (  (y2* np.log(x1)) - (  y1 * np.log(x2)  )   )/ ( y1-y2  )  )  )

    
    def returnFunc(x):
        """
        A logarithhmic function of x
        """
        my_a = float(a)
        my_b = float(b)
        
    """
    pass
'''

def getMelodyFromFT(ft_array):
    """
    fourier transform array shows melodic arches
    """
    mel = []
    for n in ft_array:
        mel.append( np.rint( n/.33 ))
    good = []

    curr = 50
    for n in mel:
        curr += n
        good.append(curr)
    return good
    

def getDurationFromMelody(mel_array):
    duration = []
    for m in range(len(mel_array) -1):
        m1 = mel_array[m]
        m2 = mel_array[m+1]
        delta = abs(m2-m1)
        duration.append(delta)
    return duration
    


def getNumInstrumentsFromVariance(x):
    """
    returns the amount of instruments from the variance
    variance could be from 0 to 11, as output from the sentiment

    just returns closest integer
    """
    return   np.rint( abs(x-1.5))

def getVolumeFromSentiment(sent):
    """
    Dynamic changing in volume for sentiment increases or descreases
    """

    x1 = -11.0
    y1 =  10.0

    x2 = 11.0
    y2 = 100.0

    #introduce negativity bias
    x1 = x1 + 15
    x2 = x2 + 15

    a = (    (y1-y2 )/np.log( x1 / x2  )) 

    print 'a'
    print a

    b = (  np.exp(    (  (y2* np.log(x1)) - (  y1 * np.log(x2)  )   )/ ( y1-y2  )  )  )
    print b
    print 'b'

    #account for regativity bias

    volume_vector = []

    for x in sent:
        print 's'
        print x
        x = x + 15
        print x
        volume_vector.append(np.rint(( a * np.log( b * x  ))))

    return  volume_vector


def buildChordFromSentiment(fundamental, sent, n_voices):
    """
    -11  to 11
    11 is happiest chord
    -11 is saddest chord

    0 is neutral chord

    The length of 'chord' corresponds to n_voices 

    """
    chord = []
    intervals = [0,12, 7, 5, 4,9,2,11,10,8,3,6,1]
    if sent > 11:
        sent = 11
    if sent <-10:
        sent = -10
    max_interval = int(np.rint(((-6.0/11) * sent) + 6))
    if max_interval == 0:
        max_interval = 1
    my_range = intervals[:max_interval]
    print my_range
    for i in range(n_voices):
        pitch = random.choice(my_range)
        if pitch == fundamental:

            n = random.choice(range(1,3))
            ptch = pitch + (n * 12)

        n = random.choice([ i for i in range(-1,2)])
        ptch = pitch + (n * 12)

        chord.append(fundamental + pitch)
    return chord

def getTempoFromPolarity(x):
    """
    polarity is from -1 to +1

    rounds to nearest integer

    grave to prestissimo
    grave = 30
    prestissimo = 200
    """

    x1 = -1.0
    y1 =  30

    x2 = 1.0
    y2 = 200

    #introduce negativity bias
    x1 = x1 + 2
    x2 = x2 + 2

    a = (    (y1-y2 )/np.log( x1 / x2  )) 

    b = (  np.exp(    (  (y2* np.log(x1)) - (  y1 * np.log(x2)  )   )/ ( y1-y2  )  )  )

    #account for regativity bias
    x = x + 2
    return   np.rint(( a * np.log( b * x  )))


if __name__ == "__main__":

    macft = [ float(line.strip()) for line in open("alicefft.txt","r")]
    macsent = []
    for line in open("alicesent.txt","r"):
        macsent.extend( [int(i) for i in line.strip().split()])
    print macsent
    mel = getMelodyFromFT(macft)
    dur = getDurationFromMelody(mel)


    M = MIDIFile(5)

    track = 0
    time = 0
    x = macsent 

    #x = [ max( [abs(i), abs(j)] ) for i,j in zip(x[::2], x[1::2])]
    #x = [ max( [abs(i), abs(j)] ) for i,j in zip(x[::2], x[1::2])]

    x = [( i,j ) for i,j in zip(x[::2], x[1::2])]
    y = []
    for v in x:
        abs0 = abs(v[0])
        abs1 = abs(v[1])
        if abs0 > abs1:
            greatest = v[0]
        else:
            greatest = v[1]
        y.append(greatest)
    x = y


    x = [( i,j ) for i,j in zip(x[::2], x[1::2])]
    y = []
    for v in x:
        abs0 = abs(v[0])
        abs1 = abs(v[1])
        if abs0 > abs1:
            greatest = v[0]
        else:
            greatest = v[1]
        y.append(greatest)
    x = y

    x = [( i,j ) for i,j in zip(x[::2], x[1::2])]
    y = []
    for v in x:
        abs0 = abs(v[0])
        abs1 = abs(v[1])
        if abs0 > abs1:
            greatest = v[0]
        else:
            greatest = v[1]
        y.append(greatest)
    x = y

    x = [( i,j ) for i,j in zip(x[::2], x[1::2])]
    y = []
    for v in x:
        abs0 = abs(v[0])
        abs1 = abs(v[1])
        if abs0 > abs1:
            greatest = v[0]
        else:
            greatest = v[1]
        y.append(greatest)
    x = y

    x = [( i,j ) for i,j in zip(x[::2], x[1::2])]
    y = []
    for v in x:
        abs0 = abs(v[0])
        abs1 = abs(v[1])
        if abs0 > abs1:
            greatest = v[0]
        else:
            greatest = v[1]
        y.append(greatest)
    x = y

    x = [( i,j ) for i,j in zip(x[::2], x[1::2])]
    y = []
    for v in x:
        abs0 = abs(v[0])
        abs1 = abs(v[1])
        if abs0 > abs1:
            greatest = v[0]
        else:
            greatest = v[1]
        y.append(greatest)
    x = y


    x = [int( np.rint(  ( i+ j)/2.0 ) )  for i,j in zip(x[::2], x[1::2])]

    """
    x = [int( np.rint(  ( i+ j)/2.0 ) )  for i,j in zip(x[::2], x[1::2])]
    x = [int( np.rint(  ( i+ j)/2.0 ) )  for i,j in zip(x[::2], x[1::2])]
    x = [int( np.rint(  ( i+ j)/2.0 ) )  for i,j in zip(x[::2], x[1::2])]
    x = [int( np.rint(  ( i+ j)/2.0 ) )  for i,j in zip(x[::2], x[1::2])]
    x = [int( np.rint(  ( i+ j)/2.0 ) )  for i,j in zip(x[::2], x[1::2])]
    """

    macsent = x
    print('now')
    print x
    M.addTrackName(track,time, "trackstomp")
    M.addTempo(track,time, 140)

    track = 0 
    channel = 0
    pitch = 60
    time = 0
    duration = 32
    volume = 100
    sentiment = [10, 5, 0, -5, -10]
    voices = 5
    rands = [k for k in range(voices)]
            
    volume_vec = [int(abs(v)) for v in getVolumeFromSentiment(macsent)]

    for b in macsent:
        chord = buildChordFromSentiment(50, b, 6)
        for i in range(5):
            M.addNote(i, 0, chord[i] , time, duration, volume_vec[i])
            """
            M.addNote(track, 1, chord[1] , time, duration, volume)
            M.addNote(track, 2, chord[2] , time, duration, volume)
            M.addNote(track, 3, chord[3] , time, duration, volume)
            M.addNote(track, 4, chord[4] , time, duration, volume)
            """
        tt = time
        last_v = 0
        for i in range(duration/2): 
            print duration/16
            print 'ax'
            if i%2 == 0:
                M.addNote(track, 5, chord[random.choice(rands)] +12, tt + last_v, (duration/8 + last_v), volume_vec[i%len(volume_vec)])
            else:
                M.addNote(track, 5, chord[random.choice(rands)] +12, tt - last_v, (duration/16 - last_v), volume_vec[i%len(volume_vec)])
            last_v = random.choice([2, -1, -1, .25, .5, 1, 0,0,0,0,0])

            tt += duration/16

        time +=duration
    
    """
    for i in range(99):
        #M.addNote(track, channel, pitch, i, duration,volume - i )
        M.addNote(track, channel, mel[i]/2 , i + dur[i], dur[i], volume)
    """

    outfile = open("testy2.mid", "wb")
    M.writeFile(outfile)
    outfile.close()
