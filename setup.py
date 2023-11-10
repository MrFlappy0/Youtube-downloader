import os

# Installer les modules nécessaires
os.system("pip install pytube tqdm wget")

# Créer le dossier de téléchargement et le fichier url.txt
download_dir = os.path.join(os.path.expanduser("~"), "Downloads", "Youtube download")
if not os.path.exists(download_dir):
    os.mkdir(download_dir)
    os.mkdir(os.path.join(download_dir, "data"))
    with open(os.path.join(download_dir, "url.txt"), "w") as f:
        f.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ\n")
else:
    if not os.path.exists(os.path.join(download_dir, "data")):
        os.mkdir(os.path.join(download_dir, "data"))

# Télécharger le fichier Python à partir de GitHub
os.system("wget https://raw.githubusercontent.com/user/repo/branch/download.py -P " + download_dir)