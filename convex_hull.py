"""
Code to get and plot the convex hull
using incremental algorithm

Author: Pratik Mallya
January 2012
"""
from matplotlib.pyplot import plot,show,scatter
from numpy import random, argsort

def slope (a,b):
    """ returns slope """
    return (b[1] - a[1]) / (b[0] - a[0])

def IsRightPoint (a, b, c):
    """ tests whether c-b is to the right of b-a"""
    if ( slope(b,c) < slope(a,b) ):
        return True
    else :
        return False

def MakeConvex (ind, x, y):
    """ 
    checks whether the list ind contains
    a convex partial polygon. Otherwise, fixes
    it!
    """
    fin =[ind[0],ind[1]]
    for i in range (2,len(ind)):
        fin.append(ind[i])
        while (True):
            a = [ x[fin[-3]], y[fin[-3]] ]
            b = [ x[fin[-2]], y[fin[-2]] ]
            c = [ x[fin[-1]], y[fin[-1]] ]
            if(IsRightPoint (a,b,c)):
                break
            else :
                del fin[-2]
                if(len(fin)<3):
                    break
    return fin

#random.seed(9024)
x = random.random(1000)
y = random.random(1000)

ind = argsort(x)
x = x[ind]
y = y[ind]

alph = (y[-1] - y[0]) / (x[-1] - x[0])

# put the indices of points in upper
# convex region here
indu = [0,1]

# find the upper convex region
for i in range(2 , x.size):
    if((y[i] - y[0]) / (x[i] - x[0]) >= alph):
        indu.append(i)

indl = [x.size-1,x.size-2]

# find the lower convex region
for i in range(x.size-3,0,-1):
    if((y[i] - y[0]) / (x[i] - x[0]) < alph):
        indl.append(i)

# since the comaprison is with 0, the last
# leg is always left out 
indl.append(0)

indux = MakeConvex (indu, x, y)
indlx = MakeConvex (indl, x, y) 
scatter(x,y)
plot(x[indux], y[indux],'b')
plot(x[indlx], y[indlx],'r')
show()
