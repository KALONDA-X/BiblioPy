# Fonction de tri à bulles (Bubble Sort)
# Trie la liste books selon la clé key (ex: 'titre', 'ISBN', 'auteur', 'année')
def bubble_sort(books, key):
    n = len(books)
    # Parcours de tous les éléments du tableau
    for i in range(n):
        # Les derniers i éléments sont déjà triés
        for j in range(0, n - i - 1):
            # Comparer deux éléments successifs selon la clé donnée
            if books[j][key] > books[j + 1][key]:
                # Échanger les deux éléments s'ils sont dans le mauvais ordre
                books[j], books[j + 1] = books[j + 1], books[j]
    # Retourner la liste triée
    return books

# Fonction de tri par insertion (Insertion Sort)
# Trie la liste books selon la clé key (ex: 'titre', 'ISBN', 'auteur', 'année')
def insertion_sort(books, key):
    # Commencer à partir du deuxième élément
    for i in range(1, len(books)):
        current = books[i]
        j = i - 1
        # Décalage des éléments plus grands que current vers la droite
        while j >= 0 and books[j][key] > current[key]:
            books[j + 1] = books[j]
            j -= 1
        # Insertion de l'élément à sa place correcte
        books[j + 1] = current
    # Retourner la liste triée
    return books

# Exemple d'utilisation dans ton menu (partie choix 5)


'''
elif choice == '5':
    key = input("Trier par (titre/auteur/année): ").lower()
    methode = input("Méthode de tri (bulle/insertion): ").lower()

    if methode == "bulle":
        livres_tries = bubble_sort(books, key)
    elif methode == "insertion":
        livres_tries = insertion_sort(books, key)
    else:
        print("Méthode invalide. Choisissez 'bulle' ou 'insertion'.")
        continue

    print("\n--- Livres triés ---")
    for livre in livres_tries:
        print(livre)
 elif choice == '5':
            key = input("Trier par (titre/auteur/année): ").strip().lower()
            if key not in ['titre', 'auteur', 'année']:
                print("Clé invalide. Choisissez parmi : titre, auteur, année.")
                continue

            methode = input("Méthode de tri (bulle/insertion): ").strip().lower()
            if methode == 'bulle':
                sorted_books = bubble_sort(books, key)
            elif methode == 'insertion':
                sorted_books = insertion_sort(books, key)
            else:
                print("Méthode invalide. Choisissez 'bulle' ou 'insertion'.")
                continue

            print("\n--- Liste triée des livres ---")
            for i, book in enumerate(sorted_books, start=1):
                print(f"{i}. Titre: {book['titre']} | Auteur: {book['auteur']} | ISBN: {book['ISBN']} | Année: {book['année']} | Statut: {book['status']}")


'''