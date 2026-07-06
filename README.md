# Scribe

Scribe est un outil en ligne de commande qui transforme un enregistrement audio
(reunion, cours, note vocale) en compte rendu ecrit et structure.

## Fonctionnement
1. L'utilisateur fournit un fichier audio.
2. Un modele Speech-to-Text (Groq) transcrit l'audio en texte brut.
3. Un LLM (Groq) reformule ce texte en compte rendu structure : titre, points cles, decisions, actions.

## Installation
1. Cloner le depot : git clone https://github.com/yugerthen/Scribe.git
2. Installer les dependances : pip install -r requirements.txt
3. Copier .env.example en .env et renseigner votre cle API Groq (console.groq.com)

## Usage
python src/main.py audio_samples/test.wav

Le compte rendu s'affiche dans le terminal et est sauvegarde dans un fichier
compte_rendu_AAAAMMJJ_HHMMSS.md a la racine du projet.

## Choix des modeles
- STT : whisper-large-v3-turbo - rapide et economique, largement suffisant pour transcrire des reunions/cours.
- LLM : llama-3.3-70b-versatile - meilleure qualite de synthese/structuration qu'un modele plus leger, important pour un compte rendu fidele.

## Q1 - Pourquoi le .gitignore doit exister avant tout code manipulant des secrets
Un fichier commite une seule fois reste dans l'historique Git pour toujours, meme si on le supprime apres. Le seul moyen fiable de ne jamais exposer une cle API est de l'exclure avant qu'elle soit ajoutee au depot.

## Q3 - Metadonnees de transcription
En plus du texte, l'API Groq renvoie (avec response_format="verbose_json") : la langue detectee, la duree totale, et des segments horodates contenant des indicateurs de qualite (avg_logprob, compression_ratio, no_speech_prob). Ces metadonnees pourraient servir a detecter automatiquement les passages de mauvaise qualite audio, ou a afficher un sous-titrage synchronise dans une future version de Scribe.

## Q4 - Choix de la temperature
Temperature fixee a 0.2 pour le resume : on veut un compte rendu fidele et factuel, pas creatif. Une temperature basse reduit la variabilite et le risque d'invention (hallucination) de contenu absent de la transcription.

## Q5 - Prompt systeme et tokens en cache
Le prompt systeme est identique a chaque appel (il ne change pas d'un audio a l'autre). Groq peut mettre en cache ce prefixe commun (prompt caching), ce qui reduit la latence et le cout des appels repetes puisque seul le contenu utilisateur (la transcription) change a chaque requete.
