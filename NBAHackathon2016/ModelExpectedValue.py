import matplotlib.pyplot as plt
import numpy
from numpy import genfromtxt

Final=genfromtxt('SimplifiedDataSetFinal.csv', delimiter=',')

defDist=1
shotDist=22

defenderdist=int(defDist)+0.5
shotdist=int(shotDist)+0.5
if shotDist>24.9:
    ExpectedValue=0
else:
    ExpectedValue=(Final[shotdist,1]-Final[shotdist,0])*(1-numpy.exp(-(0.2*defDist**2)))+Final[shotdist,0]
    
#ExpectedValue=(Final[shotdist,1]-Final[shotdist,0])*(1-numpy.exp(-(7.5789377*10**-6*defDist**4-3.78946158*10**-4*defDist**3+6.74138941*10**-3*defDist**2-5.1627094*10**-2*defDist+2.39788026*10**-1)))+Final[shotdist,0]
#ExpectedValue=(Final[shotdist,1]-Final[shotdist,0])*(1-numpy.exp((0.00100471*defDist**2-0.02530199*defDist+0.22231295)))+Final[shotdist,0]
#ExpectedValue=(Final[shotdist,1]-Final[shotdist,0])*(1-numpy.exp(-(7.5789377*10**-6*defDist**4-3.78946158*10**-4*defDist**3+6.74138941*10**-3*defDist**2-5.1627094*10**-2*defDist+2.39788026*10**-1)))+Final[shotdist,0]
print ExpectedValue

