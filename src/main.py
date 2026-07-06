import sys
from datetime import datetime
from transcription import transcrire
from summary import resumer

def main():
    if len(sys.argv) < 2:
        print("Usage : python main.py <chemin_fichier_audio>")
        sys.exit(1)

    chemin_audio = sys.argv[1]

    print("Transcription en cours...")
    texte = transcrire(chemin_audio)

    print("Rédaction du compte rendu en cours...")
    compte_rendu = resumer(texte)

    print("\n" + compte_rendu)

    horodatage = datetime.now().strftime("%Y%m%d_%H%M%S")
    nom_fichier = f"compte_rendu_{horodatage}.md"
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(compte_rendu)

    print(f"\nCompte rendu sauvegardé dans {nom_fichier}")

if __name__ == "__main__":
    main()