#  BiblioPy - Gestionnaire de Bibliothèque

##  Présentation

BiblioPy est une application en ligne de commande permettant de gérer un catalogue de livres.  
Elle a été développée dans le cadre du projet d’Algorithmique II, en groupe de 4 étudiants.

Le programme permet d’ajouter, rechercher, trier et emprunter des livres.  
Les données sont stockées dans un fichier JSON.

---

##  Fonctionnalités principales

- Ajouter, modifier, supprimer des livres (CRUD)
- Rechercher des livres par titre, auteur, ISBN
- Trier la bibliothèque par titre, auteur, année
- Marquer un livre comme emprunté ou retourné
- Afficher les livres disponibles ou empruntés
- Interface en ligne de commande (CLI)

---

##  Structure du projet

BiblioPy/
├── data_manager.py # Module 1 - Gestion des données
├── search_engine.py # Module 2 - Recherche
├── sort_engine.py # Module 3 - Tri
├── loan_manager.py # Module 4 - Emprunts
├── cli_interface.py # Module 5 - Interface utilisateur
├── bibliotheque.json # Données des livres
└── README.md # Ce fichier


---

##  Répartition des modules

| Étudiant               | Modules réalisés                         |
|------------------------|------------------------------------------|
| **[Ton Nom]**          | Module 3 (Tri), Module 5 (Interface CLI) |
| **Camarade 1**         | Module 1 (DataManager)                   |
| **Camarade 2**         | Module 2 (SearchEngine)                  |
| **Camarade 3**         | Module 4 (LoanManager)                   |

>  Chaque membre travaille sur une branche différente (par module).

---

##  Lancer le projet

1. Ouvrir un terminal dans le dossier du projet
2. Exécuter l’interface principale :

```bash
python cli_interface.py

