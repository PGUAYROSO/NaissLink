# 🏥 NaissLink

## Gestion intelligente du dossier documentaire de naissance

NaissLink est une application web destinée aux établissements de santé permettant la gestion complète du dossier documentaire de naissance.

Le projet a pour objectif de sécuriser, simplifier et automatiser le traitement des déclarations de naissance grâce à une architecture moderne, un moteur de règles documentaires et l'intelligence artificielle.

---

# Fonctionnalités

## Dossiers documentaires

- Création d'un dossier
- Consultation
- Archivage
- Historique

## Documents

- Téléversement
- Visualisation PDF
- Téléchargement
- Suppression
- Classement

## Utilisateurs

- Authentification JWT
- Gestion des rôles
- Journalisation

## Transmission

- Transmission vers l'état civil
- Historique
- Traçabilité

## Intelligence Artificielle (à venir)

- OCR
- Reconnaissance automatique des documents
- Vérification de la complétude
- Pré-remplissage des dossiers

---

# Technologies

## Backend

- Python 3.13
- Flask
- SQLAlchemy
- Alembic
- PostgreSQL
- JWT

## Frontend

- React
- Vite
- Material UI
- Axios

---

# Architecture

```
React

↓

REST API

↓

Flask

↓

Application

↓

Repositories

↓

SQLAlchemy

↓

PostgreSQL
```

---

# Organisation du projet

```
backend/
frontend/
docs/
tests/
```

---

# Documentation

La documentation complète est disponible dans le dossier **docs**.

- Architecture
- Base de données
- API REST
- Workflow métier
- Guide d'installation
- Guide utilisateur
- Journal de développement
- Roadmap

---

# Roadmap

## Version 0.8

- Gestion des transmissions

## Version 0.9

- Référentiel documentaire

- Moteur de complétude

## Version 1.0

- OCR

- Intelligence artificielle

- Transmission automatisée

---

# Auteur

Patrice Guayroso

Centre Hospitalier de la Basse-Terre

Guadeloupe