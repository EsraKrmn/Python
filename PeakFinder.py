
import random

#Generate an array of random numbers
def GenerateRandomArray(n):
    ls= []
    for i in range(n):
         a = random.randint(1,1000)
         ls.append(a)
    return ls

#Generate a matrix of random numbers
def GenerateRandomMatrix(row,column):
    matrix = []
    for i in range(row):          
        a =[]
        for j in range(column):  
            indis = random.randint(1,1000)
            a.append(indis)  
        matrix.append(a)
      
    for i in range(row):
        for j in range(column):
            return matrix

#Straightforward 1D peak finder         
def OneDPeakFinder(rl,n=None):
    if n == None:
        n = round((len(rl))/2)
    a = []
    while True:
        if n == 0:
            if rl[n]>=rl[n+1]:
                a.append(n)
                return (rl[n],n),a
            else:
                a.append(n)
                n = n+1
        if n == len(rl)-1:
            if rl[n]>=rl[n-1]:
                a.append(n)
                return (rl[n],n),a
            else:
                a.append(n)
                n = n-1     
        if rl[n] >= rl[n+1] and rl[n] >= rl[n-1]:
            a.append(n)
            return (rl[n],n),a
        else:
            if  rl[n] >= rl[n+1] or n == len(rl)-1:
                a.append(n)
                n = n-1
            else:
                a.append(n)
                n = n+1
    return "Peak could not be found!"

#Check if the include b in a.
def test(a,b):
    for i in a:
        if i not in b:
            b.append(i)

#Straightforward 2D peak finder
def TwoDPeakFinder(rl,n=None,m=None):
    if n == None:
        n=round(len(rl)/2)
    if m == None:
        m=round(len(rl[0])/2)   
    a = []
    while True:
        if rl[n][m]>rl[n-1][m] and rl[n][m]>rl[n+1][m] and rl[n][m]>rl[n][m+1] and rl[n][m]>rl[n][m-1]: 
            a.append([n,m])
            if m-1>-1:
                a.append([n,m-1])
            if n-1 >-1:
                a.append([n-1,m])
            else:
                a.append([n+1,m])
            return (rl[n][m],[n,m]),a
        for i in range(len(rl)):
            if m == 0:
                if rl[n][m]>rl[n-1][m] and rl[n][m]>rl[n+1][m] and rl[n][m]>rl[n][m+1] :
                    b=[]
                    test(a,b)
                    return (rl[n][m],[n,m]),b
            if n == 0:
                if  rl[n][m]>rl[n+1][m] and rl[n][m]>rl[n][m+1] and rl[n][m]>rl[n][m-1]:
                    b=[]
                    test(a,b)
                    return (rl[n][m],[n,m]),b
            if m == len(rl[0])-1:
                if rl[n][m]>rl[n-1][m] and rl[n][m]>rl[n+1][m]  and rl[n][m]>rl[n][m-1]:
                    b=[]
                    test(a,b)
                    return (rl[n][m],[n,m]),b
            if n== len(rl)-1:
                if rl[n][m]>rl[n-1][m]  and rl[n][m]>rl[n][m+1] and rl[n][m]>rl[n][m-1]:
                    b=[]
                    test(a,b)     
                    return (rl[n][m],[n,m]),b
            if rl[n][m]>rl[n-1][m] and rl[n][m]>rl[n+1][m] and rl[n][m]>rl[n][m+1] and rl[n][m]>rl[n][m-1]:
                b=[]
                test(a,b)       
                return (rl[n][m],[n,m]),b
            if n != 0:
                for i in range(len(rl)):
                    if rl[n-1][m]>=rl[n][m]:
                        a.append([n,m])
                        n = n-1
                        a.append([n,m])
            if m != 0: 
                for i in range(len(rl)):
                    if rl[n][m-1]>=rl[n][m]:
                        a.append([n,m])
                        m = m-1
                        a.append([n,m])
            if n<=len(rl): 
                for i in range(len(rl)):
                    if rl[n+1][m]>=rl[n][m]:
                        a.append([n,m])
                        n=n+1
                        a.append([n,m])
            if m<len(rl[0])-1:    
                for i in range(len(rl)):
                    if rl[n][m+1]>=rl[n][m]:
                        a.append([n,m])
                        m=m+1
                        a.append([n,m])
    return "Peak could not be found!"     