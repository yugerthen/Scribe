import os
from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL

client = Groq(api_key=GROQ_API_KEY)

def charger_prompt_systeme():
    chemin = os.path.join(os.path.dirname(__file__), "..", "prompts", "system_prompt.txt")
    with open(chemin, "r", encoding="utf-8") as f:
        return f.read()

def resumer(transcription_texte):
    prompt_systeme = charger_prompt_systeme()
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": prompt_systeme},
                {"role": "user", "content": transcription_texte}
            ],
            model=LLM_MODEL,
            temperature=0.2
        )
    except Exception as e:
        raise RuntimeError(f"Erreur lors de l'appel à l'API Groq (résumé) : {e}")

    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    from transcription import transcrire
    texte = transcrire("audio_samples/test.wav")
    resultat = resumer(texte)
    print(resultat)