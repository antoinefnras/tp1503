import math
import random

def dist(x,y):
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)

def moyenne(l):
    a=0;
    b=0;
    for i in range(len(l)):
        a=a+l[i][0]
        b=b+l[i][1]
    a=a/len(l)
    b=b/len(l)
    return a,b

l=[]
for _ in range(100):
    a=random.randint(-10,10)
    b=random.randint(-10,10)
    c=(a,b)
    l.append(c)
print("Liste des points : ",l)

def kmeans(k,l):

    #Initialisation
    indices=[]
    for _ in range(len(l)):
        indices.append(0)
    classes=[]
    for i in range(k):
        classes.append(l[i])

    print("Itération 0")
    for i in range(k):
        print("  Classe ",i," : ",classes[i])

    #10 itérations
    for m in range(10):

        #Calcul des distances par rapport aux centres
        for i in range(len(l)):
            min=dist(l[i],classes[0])
            indices[i]=0
            for j in range(1,k):
                a=dist(l[i],classes[j])
                if a<min:
                    min=a
                    indices[i]=j

        #Recalcul des centres
        for i in range(k):
            o=[]
            for j in range(len(indices)):
                if indices[j]==i:
                    o.append(l[j])
            classes[i]=moyenne(o)

        #Affichage
        print("Itération ",m+1)
        for n in range(k):
            print("  Classe ",n," : ",classes[n])

kmeans(3,l)

