#Read data from data base
import math
import numpy as np
import matplotlib.pyplot as plt 
from scipy import stats
import dtw as dtw
#
#def z_score(x=[],y=[]):
#        
#    x = np.array(x)
#    y = np.array(y)
#    
#        
#    return stats.zscore(x) , stats.zscore(y) 
def return_array(data):
        plotX = []
        plotY = []
        plotZ = []
        for t in data:
            #print(t.split(' '))
            num = t.split(' ')
            plotX.append(int(num[0]))
            plotY.append(int(num[1]))
            plotZ.append(int(num[6]))
        normX, normY, normZ = stats.zscore(plotX), stats.zscore(plotY), stats.zscore(plotZ)
        npX = np.array(normX)
        npY = np.array(normY)
        npZ = np.array(normZ)
        
        del_X = np.diff(npX, n=1)
        del_Y = np.diff(npY, n=1)
        del_Z = np.diff(npZ, n=1)
        return np.vstack((del_X,del_Y,del_Z)).T
#def del_values(x=[], y=[]):
#    del_x=[]
#    del_y=[]
#    
#    for i in x-1 :
def detection(user,signature):
        #username = input("Enter user name to test : ")
        #username.upper()
        #username = user
        signatureDB = open(f"C:\\Users\\CP LAB33\\Downloads\\khushboo_DMML\\Task2\\Task2\\U{user}S{signature}.TXT","r")
        count = signatureDB.readline()
        content = signatureDB.readlines()
        S1 =  return_array(content)
        
        distGen = 0
        distFake = 0
        
        for i in range(1,6):
            #username2 = f"U1S{i}"
            signatureDB2 = open(f"C:\\Users\\CP LAB33\\Downloads\\khushboo_DMML\\Task2\\Task2\\U{user}S{i}.TXT","r")
            count = signatureDB2.readline()
            content2 = signatureDB2.readlines()
            S2 =  return_array(content2)  
            euclidean_norm = lambda S1,S2: math.sqrt((S1[0]-S2[0])**2 + (S1[1]-S2[1])**2 + (S1[2]-S2[2])**2) 
            a,b,c,d = dtw.dtw(S1,S2,dist=euclidean_norm)
            distGen = distGen + a
            signatureDB2.close()
        
        avgDistGen = distGen / 5
        
        for i in range(21,26):
           # username2 = f"U1S{i}"
            signatureDB2 = open(f"C:\\Users\\CP LAB33\\Downloads\\khushboo_DMML\\Task2\\Task2\\U{user}S{i}.TXT","r")
            count = signatureDB2.readline()
            content3 = signatureDB2.readlines()
            S3 =  return_array(content3)  
            euclidean_norm = lambda S1,S3: math.sqrt((S1[0]-S3[0])**2 + (S1[1]-S3[1])**2 + (S1[2]-S3[2])**2) 
            a1,b,c,d = dtw.dtw(S1,S3,dist=euclidean_norm)
            distFake = distFake + a1
            signatureDB2.close()
        
        avgDistFake = distFake / 5
        
        #print("\ndistFake : ",distFake)
        #print("\ndistGen : ",distGen)
        
#        print(b)
#        print(c)
#        print(d)
        
        
        #print(avgDistFake -  avgDistGen)
        
        #return avgDistGen, avgDistFake
        
        if((avgDistFake -  avgDistGen) > 0):
            #print(f"{username} is genuine signature.") #Genuine
            return 0
        else:
            #print(f"{username} is forged signature.") # Forged
            return 1

       
P = 0
F = 0
for i in range(1,41):
    for j in range(1,41):

        if((j>=1 and j<=21) and detection(i,j)==0):
            P = P+1
            print("P=",P)
        elif((j>=21 and j<=41) and detection(i,j)==1):
            P = P+1
            print("P=",P)
        else:
            F=F+1
            print("F=",F)
        

accuracy = (P/(P+F))*100
print("Accuracy : ", accuracy)

