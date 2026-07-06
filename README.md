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



\## Q3 — Métadonnées de transcription

En plus du texte, l'API Groq renvoie (avec response\_format="verbose\_json") : la langue détectée,

la durée totale, et des segments horodatés contenant des indicateurs de qualité (avg\_logprob,

compression\_ratio, no\_speech\_prob). Ces métadonnées pourraient servir à détecter automatiquement

les passages de mauvaise qualité audio, ou à afficher un sous-titrage synchronisé dans une future

version de Scribe.

