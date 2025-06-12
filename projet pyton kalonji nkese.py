


def recherche_sequentiel(liste,element):
     for i in range(len(liste)):
         if liste[i] == element:
             return  (element,i)
         
             
     return print("aucun resultat")

def recherche_dichotomique(liste,element):
    debut = 0
    fin = len(liste)-1
    while debut <= fin :
        milieu =(debut + fin)//2
        if liste[milieu]== element:
            return i
        elif milieu < element:
            debut = milieu+1
        else:
            fin = milieu-1
    return none 
