# Youtube-downloader
Ce code est un programme Python qui permet de récupérer des détails et de télécharger des vidéos à partir de liens YouTube. Voici une description détaillée du code pour GitHub :

Le programme commence par importer deux bibliothèques : pytube pour interagir avec YouTube et tqdm pour afficher une barre de progression pendant le téléchargement.

Ensuite, il définit trois fonctions principales :

get_video_details(url): Cette fonction prend une URL YouTube en entrée, utilise la bibliothèque pytube pour obtenir les détails de la vidéo associée à cette URL, puis renvoie ces détails sous forme d'objet YouTube (yt). En cas d'erreur lors de la récupération des détails, elle affiche un message d'erreur.

print_video_details(yt): Cette fonction prend un objet YouTube (yt) en entrée et affiche les détails de la vidéo, tels que le titre, le nombre de vues, la durée et la note moyenne.

download_video(yt): Cette fonction prend également un objet YouTube (yt) en entrée et tente de télécharger la vidéo avec la meilleure résolution disponible. Elle affiche un message de progression pendant le téléchargement et signale si une erreur se produit.

Le programme définit également une fonction read_urls_from_file(filename) qui lit les URLs de vidéos à partir d'un fichier texte (.txt) spécifié. Les URLs lues sont renvoyées sous forme de liste.

La fonction help() affiche un menu d'aide avec deux options : entrer une URL de vidéo YouTube ou lire les URLs à partir d'un fichier .txt.

La fonction principale main() commence en affichant le menu d'aide, puis en demandant à l'utilisateur de choisir entre les deux options. En fonction de la réponse de l'utilisateur, le programme récupère les détails de la vidéo et les télécharge, soit en demandant l'URL de la vidéo YouTube, soit en lisant les URLs à partir d'un fichier .txt.

Enfin, la fonction main() est exécutée si le script est exécuté en tant que programme principal.
