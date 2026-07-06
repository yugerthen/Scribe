import os
from groq import Groq
from config import GROQ_API_KEY, STT_MODEL

client = Groq(api_key=GROQ_API_KEY)

def transcrire(chemin_fichier):
    if not os.path.exists(chemin_fichier):
        raise FileNotFoundError(f"Fichier audio introuvable : {chemin_fichier}")
    try:
        with open(chemin_fichier, "rb") as file:
            transcription = client.audio.transcriptions.create(
                file=file,
                model=STT_MODEL,
                response_format="verbose_json",
                language="en",
                temperature=0.0
            )
    except Exception as e:
        raise RuntimeError(f"Erreur lors de l'appel à l'API Groq : {e}")
    return transcription.text

if __name__ == "__main__":
    resultat = transcrire("audio_samples/test.wav")
    print(resultat)