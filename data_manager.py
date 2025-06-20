import json
import os

DATA_FILE = "bibliotheque.json"

# Charger les livres depuis le fichier JSON
def load_books():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# Sauvegarder les livres dans le fichier JSON
def save_books(books):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

# Vérifie si l'ISBN est valide (10 ou 13 chiffres numériques)
def is_valid_isbn(isbn):
    return isbn.isdigit() and len(isbn) in [10, 13]

# Vérifie si le livre est unique (titre et ISBN)
def is_unique_book(books, isbn, titre):
    for book in books:
        if book['ISBN'] == isbn or book['titre'].lower() == titre.lower():
            return False
    return True

# Ajouter un livre si l'ISBN est valide et s'il est unique
def add_book(books, book):
    if not is_valid_isbn(book['ISBN']):
        print("ISBN invalide. Il doit contenir 10 ou 13 chiffres.")
        return
    if not is_unique_book(books, book['ISBN'], book['titre']):
        print("Ce livre existe déjà (même titre ou même ISBN).")
        return
    books.append(book)
    save_books(books)
    print("Livre ajouté avec succès.")

# Supprimer un livre par ISBN
def delete_book(books, isbn):
    new_books = [book for book in books if book['ISBN'] != isbn]
    if len(new_books) == len(books):
        print("Aucun livre trouvé avec cet ISBN.")
    else:
        save_books(new_books)
        print("Livre supprimé avec succès.")
    return new_books

# Mettre à jour les informations d’un livre à partir de son ISBN
def update_book(books, isbn, updated_fields):
    found = False
    for book in books:
        if book['ISBN'] == isbn:
            book.update(updated_fields)
            found = True
            break
    if found:
        save_books(books)
        print("Livre mis à jour avec succès.")
    else:
        print("Livre non trouvé.")
    return books


