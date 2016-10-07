import matplotlib.pyplot as plt
import numpy
from numpy import genfromtxt

Final=genfromtxt('SimplifiedDataSetFinal.csv', delimiter=',')  ##the file with pre-requisite data

defDist=1    ##user specified value for defender distance
shotDist=22  ##user specified value for shot distance

defenderdist=int(defDist)+0.5    ##for searching the array
shotdist=int(shotDist)+0.5       ##for searching the array

##the function is below
ExpectedValue=(Final[shotDist,1]-Final[shotDist,0])*(1-numpy.exp(-(0.2*defDist**2)))+Final[shotDist,0]


print ExpectedValue

