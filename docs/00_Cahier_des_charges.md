# Cahier des charges
# NaissLink

Version : 1.0 (en cours de développement)

Auteur : Patrice Guayroso

---

# 1. Contexte

Les services de maternité produisent chaque jour des dossiers documentaires destinés aux services d'état civil.

Aujourd'hui, ces dossiers sont souvent constitués manuellement, ce qui entraîne :

- perte de temps
- oublis de documents
- erreurs de classement
- manque de traçabilité
- difficultés de suivi

NaissLink a pour objectif de numériser et sécuriser ce processus.

---

# 2. Objectifs

L'application doit permettre :

- la création d'un dossier documentaire
- le classement des documents
- le contrôle automatique de la complétude
- la transmission du dossier à l'état civil
- la traçabilité complète des actions
- l'assistance par Intelligence Artificielle

---

# 3. Acteurs

## Sage-femme

- crée le dossier
- ajoute les documents
- valide le dossier

## Secrétariat

- contrôle le dossier
- prépare la transmission

## Etat Civil

- reçoit le dossier
- traite la déclaration

## Administrateur

- gère les utilisateurs
- gère les référentiels
- supervise l'application

---

# 4. Fonctionnalités

## Gestion des dossiers

- création
- consultation
- archivage

## Gestion documentaire

- upload
- visualisation PDF
- téléchargement
- suppression

## Référentiels

- types de dossiers
- types de documents
- règles documentaires

## Transmission

- création
- historique
- suivi

## Historique

- journalisation complète

## Tableau de bord

- statistiques
- indicateurs

---

# 5. Intelligence Artificielle

L'IA devra :

- reconnaître les documents
- détecter leur type
- extraire les informations
- contrôler la cohérence
- calculer la complétude
- proposer des corrections

---

# 6. OCR

Lecture automatique de :

- PDF
- JPEG
- PNG

---

# 7. Technologies

Backend

- Python
- Flask
- SQLAlchemy
- PostgreSQL
- Alembic

Frontend

- React
- Material UI
- Axios

---

# 8. Architecture

Architecture inspirée du Domain Driven Design.

backend/

- app
- api
- application
- domain
- infrastructure

frontend/

- components
- pages
- services

---

# 9. Sécurité

- JWT
- Journalisation
- Contrôle des accès
- Sauvegardes
- HTTPS

---

# 10. Roadmap

## Version 0.8

Gestion des transmissions

## Version 0.9

Référentiels documentaires

Moteur de complétude

## Version 1.0

OCR

IA

Transmission automatisée

Tableau de bord

---

# 11. Vision

NaissLink doit devenir une plateforme permettant la gestion complète des dossiers documentaires de naissance avec assistance intelligente et traçabilité intégrale.

L'objectif est de réduire le temps de traitement, d'améliorer la qualité des dossiers et de sécuriser les échanges avec les services d'état civil.