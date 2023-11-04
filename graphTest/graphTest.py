import pylab;
import random;


def getX():
    xVal = random.choice(range(0,11));
    return xVal;

def getY():
    yVal = random.choice(range(0,11));
    return yVal;
    
def graph():
    i = 0;
    while(i <= 10):
        xAxis = [0];
        yAxix = [0];
        xAxis.append(getX());
        yAxix.append(getY());
        i = i + 1;
    pylab.figure(2);
    pylab.plot(xAxis, yAxix);
    pylab.show();
#main
#pylab.figure(1);
#pylab.plot([1,3,4,5,6,7], [34,67,54,21,34,12]);
#pylab.show();
graph();
print "hello world!!! :)";