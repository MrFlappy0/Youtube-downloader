import os

# Install necessary modules
os.system("pip install pytube tqdm")

# Create directory for downloads and url.txt file
download_dir = os.path.join(os.path.expanduser("~"), "Downloads", "Youtube download")
if not os.path.exists(download_dir):
    os.mkdir(download_dir)
    os.mkdir(os.path.join(download_dir, "data"))
    with open(os.path.join(download_dir, "url.txt"), "w") as f:
        f.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ\n")
else:
    if not os.path.exists(os.path.join(download_dir, "data")):
        os.mkdir(os.path.join(download_dir, "data"))

# Change current working directory to Youtube download folder
os.chdir(download_dir)

# Copy existing code from pythube.py
from pytube import YouTube
from tqdm import tqdm

def get_video_details(url):
    try:
        yt = YouTube(url)
        return yt
    except Exception as e:
        print("Une erreur s'est produite lors de la récupération des détails de la vidéo :", e)
        return None

def print_video_details(yt):
    if yt is not None:
        print("Titre :", yt.title)
        print("Nombre de vues :", yt.views)
        print("Durée :", yt.length, "secondes")
        print("Note moyenne :", yt.rating)

def download_video(yt):
    if yt is not None:
        try:
            ys = yt.streams.get_highest_resolution()
            print("Téléchargement en cours...")
            ys.download(output_path='data')
            print("Téléchargement terminé !")
        except Exception as e:
            print("Une erreur s'est produite lors du téléchargement de la vidéo :", e)

def read_urls_from_file(filename):
    try:
        with open(filename, 'r') as file:
            urls = file.readlines()
        return urls
    except Exception as e:
        print("Une erreur s'est produite lors de la lecture du fichier :", e)
        return []

def help():
    print("Entrez '1' pour entrer une URL de vidéo YouTube.")
    print("Entrez '2' pour lire les URL de vidéos à partir d'un fichier .txt.")

def main():
    help()
    choice = input("Votre choix : ")
    if choice == '1':
        url = input("Entrez l'URL de la vidéo YouTube : ")
        yt = get_video_details(url)
        print_video_details(yt)
        download_video(yt)
    elif choice == '2':
        filename = input("Entrez le nom du fichier .txt (il doit être dans le même dossier que ce programme) : ")
        urls = read_urls_from_file(filename)
        for url in urls:
            yt = get_video_details(url.strip())
            print_video_details(yt)
            download_video(yt)

if __name__ == "__main__":
    main()
    
