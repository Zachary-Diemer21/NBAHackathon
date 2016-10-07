import numpy
from numpy import genfromtxt

dx=1
my_data=genfromtxt('Shot_summary_2014_2015.csv', delimiter=',')

gradient=numpy.zeros((int((max(my_data[1:218789,14])+1)/dx),int((max(my_data[1:218789,18])+1)/dx))) ##initializing the array for expected value 
stddev=numpy.zeros((int((max(my_data[1:218789,14])+1)/dx),int((max(my_data[1:218789,18])+1)/dx)))   ##an error array
for i in range(0, int(max(my_data[1:218790,14])+1)):    ##looping through distances from hoops
    for k in range(0, int(max(my_data[1:100,18])+1)):   ##looping through defender distance
        temp=0
        totalnumber=0
        variance=0
        for j in range(1,218790):
            if i<my_data[j,14]<i+dx:                    ##restricting to shot distances between i and i+dx
                if k<my_data[j,18]<k+dx:                ##restricting to defender distances between k and k+dx
                    temp+=my_data[j,20]                 ##determining the number points scored from this situation
                    totalnumber+=1.                     ##determining the total number of shots taken from this situation
        if totalnumber==0:                              ##considering the case where this never comes up
            gradient[i,k]=0
        else:
            gradient[i,k]=temp/totalnumber              ##computing average number of points scored from tthis situation
        for j in range(1,218790):                      #error calculations
            if i<my_data[j,14]<i+dx:
                if k<my_data[j,18]<k+dx:
                    if totalnumber==0:
                        variance+=0
                    else:
                        variance+=(1./totalnumber*(my_data[j,20]-gradient[i,k])**2)          
        stddev[i,k]=variance**1/2
print gradient
print stddev

numpy.savetxt("foo.csv", gradient, delimiter=",")      ##saving output files