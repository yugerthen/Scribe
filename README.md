# Scribe

Scribe est un outil en ligne de commande qui transforme un enregistrement audio
(réunion, cours, note vocale) en compte rendu écrit et structuré.

## Fonctionnement

1. L'utilisateur fournit un fichier audio.
2. Un modèle Speech-to-Text (Groq) transcrit l'audio en texte brut.
3. Un LLM (Groq) reformule ce texte en compte rendu structuré : titre, points clés, décisions, actions.

## Installation

(à compléter à l'étape 2)

## Usage

(à compléter à l'étape 5)



\## Choix des modèles

\- STT : whisper-large-v3-turbo — rapide et économique, largement suffisant pour transcrire des réunions/cours.

\- LLM : llama-3.3-70b-versatile — meilleure qualité de synthèse/structuration qu'un modèle plus léger, important pour un compte rendu fidèle.

