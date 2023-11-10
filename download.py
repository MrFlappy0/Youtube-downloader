import os
from pytube import YouTube, Playlist
from pytube.cli import on_progress


def get_video_details(url):
    # Récupère les détails de la vidéo YouTube à partir de l'URL
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        return yt
    except Exception as e:
        print("Une erreur s'est produite lors de la récupération des détails de la vidéo :", e)
        return None

def print_video_details(yt):
    # Affiche les détails de la vidéo YouTube
    if yt is not None:
        print("Titre :", yt.title)
        print("Nombre de vues :", yt.views)
        print("Durée :", yt.length, "secondes")
        print("Note moyenne :", yt.rating)

def download_video(yt, quality, only_audio):
    # Télécharge la vidéo YouTube
    if yt is not None:
        try:
            if only_audio:
                ys = yt.streams.get_audio_only()
            else:
                if quality == 'high':
                    ys = yt.streams.get_highest_resolution()
                else:
                    ys = yt.streams.get_lowest_resolution()
            print("Téléchargement en cours...")
            ys.download(output_path=os.path.join(os.path.expanduser('~'), 'Downloads', 'Youtube download', 'data'))
            print("Téléchargement terminé !")
        except Exception as e:
            print("Une erreur s'est produite lors du téléchargement de la vidéo :", e)

def download_playlist(url, quality, only_audio):
    # Télécharge une playlist YouTube entière
    try:
        playlist = Playlist(url)
        for video in playlist.videos:
            download_video(video, quality, only_audio)
    except Exception as e:
        print("Une erreur s'est produite lors du téléchargement de la playlist :", e)

def read_urls_from_file(filename):
    # Lit les URL de vidéos à partir d'un fichier .txt
    try:
        with open(filename, 'r') as file:
            urls = file.readlines()
        return urls
    except Exception as e:
        print("Une erreur s'est produite lors de la lecture du fichier :", e)
        return []

def help():
    # Affiche le menu d'aide
    print("Entrez '1' pour entrer une URL de vidéo YouTube.")
    print("Entrez '2' pour lire les URL de vidéos à partir d'un fichier .txt.")
    print("Entrez '3' pour entrer une URL de playlist YouTube.")

def main():
    # Point d'entrée principal du programme
    help()
    choice = input("Votre choix : ")
    quality = input("Choisissez la qualité de la vidéo (high/low) : ")
    only_audio = input("Télécharger uniquement l'audio (yes/no) : ") == 'yes'
    if not os.path.exists(os.path.join(os.path.expanduser('~'), 'Downloads', 'Youtube download', 'data')):
        os.makedirs(os.path.join(os.path.expanduser('~'), 'Downloads', 'Youtube download', 'data'))
    if choice == '1':
        url = input("Entrez l'URL de la vidéo YouTube : ")
        yt = get_video_details(url)
        print_video_details(yt)
        download_video(yt, quality, only_audio)
    elif choice == '2':
        filename = os.path.join(os.path.expanduser('~'), 'Downloads', 'Youtube download', 'url.txt')
        if os.path.exists(filename):
            urls = read_urls_from_file(filename)
            for url in urls:
                yt = get_video_details(url.strip())
                print_video_details(yt)
                download_video(yt, quality, only_audio)
        else:
            print("Le fichier", filename, "n'existe pas.")
    elif choice == '3':
        url = input("Entrez l'URL de la playlist YouTube : ")
        download_playlist(url, quality, only_audio)

if __name__ == "__main__":
    main()
