# Scribe

Scribe est un outil en ligne de commande qui transforme un enregistrement audio
(réunion, cours, note vocale) en compte rendu écrit et structuré.

## Fonctionnement

1. L'utilisateur fournit un fichier audio.
2. Un modèle Speech-to-Text (Groq) transcrit l'audio en texte brut.
3. Un LLM (Groq) reformule ce texte en compte rendu structuré : titre, points clés, décisions, actions.

## Installation

\## Installation

1\. Cloner le dépôt : git clone https://github.com/yugerthen/Scribe.git

2\. Installer les dépendances : pip install -r requirements.txt

3\. Copier .env.example en .env et renseigner votre clé API Groq (console.groq.com)

## Usage

\## Usage

python src/main.py audio\_samples/test.wav



Le compte rendu s'affiche dans le terminal et est sauvegardé dans un fichier

compte\_rendu\_AAAAMMJJ\_HHMMSS.md à la racine du projet.



\## Q3 — Métadonnées de transcription

En plus du texte, l'API Groq renvoie (avec response\_format="verbose\_json") : la langue détectée,

la durée totale, et des segments horodatés contenant des indicateurs de qualité (avg\_logprob,

compression\_ratio, no\_speech\_prob). Ces métadonnées pourraient servir à détecter automatiquement

les passages de mauvaise qualité audio, ou à afficher un sous-titrage synchronisé dans une future

version de Scribe.



\## Q4 — Choix de la température

Température fixée à 0.2 pour le résumé : on veut un compte rendu fidèle et factuel, pas créatif.

Une température basse réduit la variabilité et le risque d'invention (hallucination) de contenu

absent de la transcription.



\## Q5 — Prompt système et tokens en cache

Le prompt système est identique à chaque appel (il ne change pas d'un audio à l'autre). Groq peut

mettre en cache ce préfixe commun (prompt caching), ce qui réduit la latence et le coût des appels

répétés puisque seul le contenu utilisateur (la transcription) change à chaque requête.

