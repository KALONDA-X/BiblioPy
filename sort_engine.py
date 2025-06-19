# Fonction de tri à bulles (Bubble Sort)
# Trie les livres selon la clé fournie (ex: 'titre', 'ISBN', 'auteur', etc.)
def bubble_sort(books, key):
    n = len(books)
     # Parcours de tous les éléments du tableau
    for i in range(n):
         # Derniers i éléments sont déjà triés
        for j in range(0, n-i-1):
             # Comparer deux éléments successifs selon la clé donnée
            if books[j][key] > books[j+1][key]:
                # Échanger les deux éléments s'ils sont dans le mauvais ordre
                books[j], books[j+1] = books[j+1], books[j]
                  # Retourner la liste triée
    return books

# Fonction de tri par insertion (Insertion Sort)
# Trie les livres selon la clé fournie
def insertion_sort(books, key):
     # On commence à partir du deuxième élément
    for i in range(1, len(books)):
        current = books[i]
        j = i - 1
         # Décalage des éléments plus grands que current vers la droite
        while j >= 0 and books[j][key] > current[key]:
            books[j+1] = books[j]
            j -= 1
             # Insertion de l'élément à sa place correcte
        books[j+1] = current
        # Retourner la liste triée
    return books
