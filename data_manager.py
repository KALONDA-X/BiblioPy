import json  # Pour gérer la lecture et écriture JSON
import os    # Pour vérifier l'existence du fichier

DATA_FILE = "bibliotheque.json"  # Nom du fichier de données

# Charger les livres depuis le fichier JSON
def load_books():
    # Si le fichier n'existe pas, retourner une liste vide (pas de livres)
    if not os.path.exists(DATA_FILE):
        return []
    # Ouvrir le fichier en mode lecture avec encodage utf-8
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        # Charger et retourner la liste des livres sous forme de dictionnaires
        return json.load(f)

# Sauvegarder les livres dans le fichier JSON
def save_books(books):
    # Ouvrir le fichier en mode écriture, avec indent pour format lisible, ensure_ascii=False pour les caractères spéciaux
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

# Vérifie si l'ISBN est valide (doit être une chaîne de chiffres, longueur 10 ou 13)
def is_valid_isbn(isbn):
    return isbn.isdigit() and len(isbn) in [10, 13]

# Vérifie que le livre est unique en comparant ISBN et titre (titre insensible à la casse)
def is_unique_book(books, isbn, titre):
    for book in books:
        # Si ISBN ou titre déjà présent dans la liste, livre non unique
        if book['ISBN'] == isbn or book['titre'].lower() == titre.lower():
            return False
    return True  # Aucun doublon trouvé, livre unique

# Ajouter un livre dans la liste si l'ISBN est valide et si le livre est unique
def add_book(books, book):
    if not is_valid_isbn(book['ISBN']):
        print("ISBN invalide. Il doit contenir 10 ou 13 chiffres.")
        return  # Arrêter la fonction si ISBN non valide
    if not is_unique_book(books, book['ISBN'], book['titre']):
        print("Ce livre existe déjà (même titre ou même ISBN).")
        return  # Arrêter si livre déjà présent
    books.append(book)  # Ajouter le livre à la liste
    save_books(books)   # Sauvegarder la liste mise à jour dans le fichier
    print("Livre ajouté avec succès.")

# Supprimer un livre identifié par son ISBN
def delete_book(books, isbn):
    # Créer une nouvelle liste sans le livre à supprimer
    new_books = [book for book in books if book['ISBN'] != isbn]
    # Si la longueur n'a pas changé, le livre n'a pas été trouvé
    if len(new_books) == len(books):
        print("Aucun livre trouvé avec cet ISBN.")
    else:
        save_books(new_books)  # Sauvegarder la nouvelle liste
        print("Livre supprimé avec succès.")
    return new_books  # Retourner la liste mise à jour

# Mettre à jour les champs d'un livre identifié par son ISBN
def update_book(books, isbn, updated_fields):
    found = False  # Indicateur si livre trouvé
    for book in books:
        if book['ISBN'] == isbn:
            book.update(updated_fields)  # Mettre à jour les champs fournis
            found = True
            break  # Sortir de la boucle une fois le livre trouvé
    if found:
        save_books(books)  # Sauvegarder la liste mise à jour
        print("Livre mis à jour avec succès.")  # Confirmer la mise à jour
    else:
        print("Livre non trouvé.")  # Avertir si ISBN introuvable
    return books  # Retourner la liste (modifiée ou non)



      
