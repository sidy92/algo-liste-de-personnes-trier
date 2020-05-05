ListesEleves=[["Adem","Othman","Aya"],["Baptiste","Walid","Adem"],["Baptiste","Walid","Aya","Adem"],["Alex","Gibaud","Younes","Kevin"],["Gibaud","Remi","Alex","Noureddine","Remi"],["Gibaud","Baptiste"],["Othman","Adem","Noureddine"],["Nourddine","Walid","Baptiste","Aya"]]

def Tri():
    L=[]
    for item in ListesEleves:
        for prenom in item:
            if prenom not in L:
                L.append(prenom)
    return L


def Algo_Principal():
    Dico={}
    Eleve=Tri()
    for i in Eleve:
        a=0
        for prenom in ListesEleves:
            for j in prenom:
                if j==i:
                    a= a+100- k.index(j)
        Dico[i]=a
    return Dico