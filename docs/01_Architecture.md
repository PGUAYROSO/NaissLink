# NaissLink
## Architecture du projet

Version : 0.8
Auteur : Patrice Guayroso
Date : Juillet 2026

---

# Présentation

NaissLink est une application permettant la gestion du dossier documentaire de naissance dans un établissement de santé.

Elle a pour objectif de :

- Centraliser les documents de naissance
- Vérifier automatiquement la complétude d'un dossier
- Assister les utilisateurs grâce à l'OCR et à l'IA
- Faciliter la transmission vers les services d'état civil
- Garantir la traçabilité des actions

---

# Architecture générale

```
React
(Material UI)

        │

Axios REST

        │

Flask API

        │

Application (Cas d'utilisation)

        │

Repositories

        │

SQLAlchemy

        │

PostgreSQL
```

---

# Architecture logicielle

Le projet est organisé selon une architecture inspirée du Domain Driven Design.

```
backend/

app/
api/
application/
domain/
infrastructure/
migrations/
```

---

# Domaine métier

Le cœur du projet est le Dossier Documentaire.

Un dossier documentaire contient :

- des documents
- un historique
- une transmission
- un état d'avancement

---

# Modules

## Utilisateurs

Authentification JWT

Gestion des rôles

Journalisation

---

## Dossiers

Création

Consultation

Archivage

---

## Documents

Ajout

Suppression

Visualisation

Téléchargement

---

## Référentiels

Types de documents

Types de dossiers

Règles documentaires

---

## Historique

Traçabilité

Journal des actions

---

## Transmission

Transmission du dossier documentaire vers l'état civil.

---

# Technologies

Backend

- Python
- Flask
- SQLAlchemy
- Alembic
- PostgreSQL

Frontend

- React
- Vite
- Material UI
- Axios

---

# Evolutions prévues

Version 0.8

Gestion des transmissions

Version 0.9

OCR

Version 1.0

Intelligence Artificielle

Reconnaissance automatique des documents

Pré-remplissage des dossiers

Contrôle automatique des pièces

Transmission automatisée