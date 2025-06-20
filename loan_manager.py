from datetime import datetime  # Importe « datetime » pour travailler avec les dates.

# Fonction pour emprunter un livre
def borrow_book(books, isbn, emprunteur):
    """
    Marque un livre comme emprunté s’il est disponible,
    ajoute le nom de l’emprunteur et la date d’emprunt.
    """
    for book in books:  # Parcours chaque dictionnaire « book » dans la liste « books »
        # Vérifie que l’ISBN correspond et que le livre est disponible
        if book['ISBN'] == isbn and book['status'] == 'disponible':
            book['status'] = 'emprunté'  # Change le statut à « emprunté »
            book['emprunteur'] = emprunteur  # Ajoute le nom de l’emprunteur
            # Enregistre la date du jour sous forme 'AAAA-MM-JJ'
            book['date_emprunt'] = datetime.today().strftime('%Y-%m-%d')
            return True  # Emprunt réussi
    return False  # Aucune correspondance ou livre non disponible

# Fonction pour retourner un livre
def return_book(books, isbn):
    """
    Marque un livre comme retourné,
    supprime les infos d’emprunteur et la date d’emprunt.
    """
    for book in books:  # Parcours de tous les livres
        # Vérifie que l’ISBN correspond et que le livre est actuellement emprunté
        if book['ISBN'] == isbn and book['status'] == 'emprunté':
            book['status'] = 'disponible'  # Remet le statut à « disponible »
            book.pop('emprunteur', None)    # Supprime l’emprunteur si présent
            book.pop('date_emprunt', None)  # Supprime la date d’emprunt
            return True  # Retour effectué avec succès
    return False  # Aucun livre emprunté correspondant trouvé

# Fonction pour afficher les livres empruntés
def list_borrowed_books(books):
    """
    Retourne la liste des livres actuellement empruntés.
    """
    # Filtre et retourne seulement les livres dont le statut est « emprunté »
    return [book for book in books if book['status'] == 'emprunté']
