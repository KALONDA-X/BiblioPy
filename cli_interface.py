'''from data_manager import load_books, save_books, add_book, delete_book, update_book
from search_engine import recherche_sequentiel, recherche_dichotomique
from sort_engine import bubble_sort, insertion_sort
from loan_manager import borrow_book,return_book,list_borrowed_books

def show_menu():
    print("\n=== BiblioPy - Gestionnaire de Bibliothèque ===")
    print("1. Ajouter un livre")
    print("2. Supprimer un livre")
    print("3. Modifier un livre")
    print("4. Rechercher un livre")
    print("5. Lister les livres triés")
    print("6. Emprunter un livre")
    print("7. Retourner un livre")
    print("8. Voir livres empruntés")
    print("9. Quitter")

def main():
    books = load_books()

    while True:
        show_menu()
        choice = input("Choix: ")

        if choice == '1':
            titre = input("Titre: ")
            auteur = input("Auteur: ")

            # Demander un ISBN valide
            while True:
                isbn = input("ISBN (10 ou 13 chiffres): ")
                if isbn.isdigit() and len(isbn) in [10, 13]:
                    break
                else:
                    print("ISBN invalide. Il doit contenir exactement 10 ou 13 chiffres.")

            # Demander une année valide
            while True:
                annee_input = input("Année: ")
                if annee_input.isdigit():
                    annee = int(annee_input)
                    break
                else:
                    print("Veuillez entrer une année valide (nombre entier).")

            book = {
                "titre": titre,
                "auteur": auteur,
                "ISBN": isbn,
                "année": annee,
                "status": "disponible"
            }
            add_book(books, book)

        elif choice == '2':
            isbn = input("ISBN du livre à supprimer: ")
            books = delete_book(books, isbn)
            print("Livre supprimé.")

        elif choice == '3':
            isbn = input("ISBN du livre à modifier: ")
            champs = {}
            champs["titre"] = input("Nouveau titre: ")
            champs["auteur"] = input("Nouvel auteur: ")
            champs["année"] = input("Nouvelle année: ")
            update_book(books, isbn, champs)
            print("Livre modifié.")

        elif choice == '4':
            key = input("Rechercher par (titre/auteur/ISBN): ")
            val = input("Mot-clé: ")
            found = recherche_sequentiel(books, key, val)
            for book in found:
                print(book)

        elif choice == '5':
            # Demander la méthode de tri
            methode = input("Méthode de tri (bulle/insertion) : ").strip().lower()
            # Demander la clé de tri
            key = input("Trier par (titre/auteur/année) : ").strip().lower()
            if key not in ['titre', 'auteur', 'année']:
                print("Clé invalide. Choisissez parmi : titre, auteur, année.")
                continue
            

            # Appliquer le tri selon la méthode choisie
            if methode == "bulle":
                books_tries = bubble_sort(books, key)
            elif methode == "insertion":
                books_tries = insertion_sort(books, key)
            else:
                print("Méthode invalide. Choisissez 'bulle' ou 'insertion'.")
                continue  # revenir au menu

            # Afficher les livres triés
            print("\n--- Liste triée des livres ---")
            for book in books_tries:
                print(f"Titre : {book['titre']} | Auteur : {book['auteur']} | "
                    f"ISBN : {book['ISBN']} | Année : {book['année']} | Statut : {book['status']}")

        elif choice == '6':
            isbn = input("ISBN du livre à emprunter: ")
            nom = input("Nom emprunteur : ")
            if borrow_book(books, isbn, nom):
                print("Livre emprunté.")
            else:
                print("Erreur: livre non disponible.")

        elif choice == '7':
            isbn = input("ISBN du livre à retourner: ")
            if return_book(books, isbn):
                print("Livre retourné.")
            else:
                print("Erreur: ce livre n'était pas emprunté.")

        elif choice == '8':
            empruntes = list_borrowed_books(books)
            for livre in empruntes:
                print(f"{livre['titre']} - pris par {livre.get('emprunteur')}")

        elif choice == '9':
            save_books(books)
            print("Données sauvegardées. À bientôt !")
            break

        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
'''
# Importation des fonctions nécessaires depuis les différents modules
from data_manager import load_books, save_books, add_book, delete_book, update_book
from search_engine import recherche_sequentiel, recherche_dichotomique
from sort_engine import bubble_sort, insertion_sort
from loan_manager import borrow_book, return_book, list_borrowed_books

# Fonction qui affiche le menu principal à l'utilisateur
def show_menu():
    print("\n=== BiblioPy - Gestionnaire de Bibliothèque ===")  # Titre du menu
    print("1. Ajouter un livre")        # Option 1
    print("2. Supprimer un livre")      # Option 2
    print("3. Modifier un livre")       # Option 3
    print("4. Rechercher un livre")     # Option 4
    print("5. Lister les livres triés") # Option 5
    print("6. Emprunter un livre")      # Option 6
    print("7. Retourner un livre")      # Option 7
    print("8. Voir livres empruntés")   # Option 8
    print("9. Quitter")                 # Option 9

# Fonction principale qui gère le programme
def main():
    books = load_books()  # Chargement des livres à partir du fichier JSON

    while True:  # Boucle infinie du menu
        show_menu()  # Affichage du menu
        choice = input("Choix: ")  # Demande le choix à l'utilisateur

        # === AJOUT D’UN LIVRE ===
        if choice == '1':
            titre = input("Titre: ")  # Saisie du titre
            auteur = input("Auteur: ")  # Saisie de l’auteur

            # Boucle de validation de l'ISBN (10 ou 13 chiffres)
            while True:
                isbn = input("ISBN (10 ou 13 chiffres): ")
                if isbn.isdigit() and len(isbn) in [10, 13]:
                    break
                else:
                    print("ISBN invalide. Il doit contenir exactement 10 ou 13 chiffres.")

            # Boucle de validation de l’année (entier)
            while True:
                annee_input = input("Année: ")
                if annee_input.isdigit():
                    annee = int(annee_input)
                    break
                else:
                    print("Veuillez entrer une année valide (nombre entier).")

            # Création du dictionnaire représentant un livre
            book = {
                "titre": titre,
                "auteur": auteur,
                "ISBN": isbn,
                "année": annee,
                "status": "disponible"  # Statut initial
            }

            add_book(books, book)  # Ajout du livre à la collection

        # === SUPPRESSION D’UN LIVRE ===
        elif choice == '2':
            isbn = input("ISBN du livre à supprimer: ")  # Saisie de l’ISBN
            books = delete_book(books, isbn)  # Suppression par ISBN
            print("Livre supprimé.")  # Confirmation

        # === MODIFICATION D’UN LIVRE ===
        elif choice == '3':
            isbn = input("ISBN du livre à modifier: ")  # Saisie ISBN
            champs = {}  # Dictionnaire des champs modifiés
            champs["titre"] = input("Nouveau titre: ")  # Nouveau titre
            champs["auteur"] = input("Nouvel auteur: ")  # Nouvel auteur
            champs["année"] = input("Nouvelle année: ")  # Nouvelle année
            update_book(books, isbn, champs)  # Application des modifications
            print("Livre modifié.")  # Confirmation

        # === RECHERCHE D’UN LIVRE ===
        elif choice == '4':
            key = input("Rechercher par (titre/auteur/ISBN): ")  # Clé de recherche
            val = input("Mot-clé: ")  # Valeur à rechercher
            found = recherche_sequentiel(books, key, val)  # Appel de la recherche
            for book in found:  # Affichage des livres trouvés
                print(book)

        # === TRI DES LIVRES ===
        elif choice == '5':
            methode = input("Méthode de tri (bulle/insertion) : ").strip().lower()  # Saisie méthode
            key = input("Trier par (titre/auteur/année) : ").strip().lower()  # Saisie clé

            # Validation de la clé
            if key not in ['titre', 'auteur', 'année']:
                print("Clé invalide. Choisissez parmi : titre, auteur, année.")
                continue  # Retour au menu

            # Choix du tri à appliquer
            if methode == "bulle":
                books_tries = bubble_sort(books, key)  # Tri à bulles
            elif methode == "insertion":
                books_tries = insertion_sort(books, key)  # Tri par insertion
            else:
                print("Méthode invalide. Choisissez 'bulle' ou 'insertion'.")
                continue  # Retour au menu

            # Affichage des livres triés
            print("\n--- Liste triée des livres ---")
            for book in books_tries:
                print(f"Titre : {book['titre']} | Auteur : {book['auteur']} | "
                      f"ISBN : {book['ISBN']} | Année : {book['année']} | Statut : {book['status']}")

        # === EMPRUNT D’UN LIVRE ===
        elif choice == '6':
            isbn = input("ISBN du livre à emprunter: ")  # Saisie ISBN
            nom = input("Nom emprunteur : ")  # Saisie nom emprunteur
            if borrow_book(books, isbn, nom):  # Tente l’emprunt
                print("Livre emprunté.")  # Succès
            else:
                print("Erreur: livre non disponible.")  # Échec

        # === RETOUR D’UN LIVRE ===
        elif choice == '7':
            isbn = input("ISBN du livre à retourner: ")  # Saisie ISBN
            if return_book(books, isbn):  # Tente le retour
                print("Livre retourné.")  # Succès
            else:
                print("Erreur: ce livre n'était pas emprunté.")  # Échec

        # === AFFICHAGE DES LIVRES EMPRUNTÉS ===
        elif choice == '8':
            empruntes = list_borrowed_books(books)  # Récupération des livres empruntés
            for livre in empruntes:  # Affichage
                print(f"{livre['titre']} - pris par {livre.get('emprunteur')}")

        # === QUITTER LE PROGRAMME ===
        elif choice == '9':
            save_books(books)  # Sauvegarde des livres dans le fichier
            print("Données sauvegardées. À bientôt !")  # Message de sortie
            break  # Quitte la boucle

        # === ENTRÉE NON VALIDE ===
        else:
            print("Choix invalide.")  # Message d’erreur si mauvais choix

# Point d’entrée du programme : appel à main() si le script est exécuté directement
if __name__ == "__main__":
    main()
