def recherche_sequentiel(books, key, value):
    return[book for book in books if book.get(key, '') == value]

def recherche_dichotomique(books, key, value):
    debut,fin = 0,len(books)-1
    result =[]

    while debut <= fin:
        millieu =(debut+fin)//2
        millieu_val = books[millieu][key]
        value = value

        if millieu_val == value:
           result.books[millieu]
           i = mid-1
           while i >= 0 and books[i][key] == value:
                 result.insert(0,books[i])
                 i-= 1
           i= millieu+1
           while i < len(books) and books[i][key] == value:
               result.append(books[i])
               i+=1
           break
        elif millieu_val < value :
           debut = millieu+1
        else:
           fin = millieu-1


    return result
