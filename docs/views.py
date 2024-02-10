import os

from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound

# Create your views here.

ROOT_DOCS = "/home/cedric/docs/docs/build/html"

def main(request, path):
    # Chemin du dossier de la documentation générée par Sphinx
    sphinx_docs_path = os.path.join(ROOT_DOCS)
    print(f"sphinx_doc_path {sphinx_docs_path}")

    # Chemin complet vers le fichier demandé (index.html ou tout autre fichier)
    full_path = os.path.join(ROOT_DOCS, path)
    print(full_path)

    # Vérifier si le fichier existe
    if os.path.exists(full_path):
        # Renvoyer le contenu du fichier demandé
        with open(full_path, 'r') as f:
            content = f.read()
        return HttpResponse(content, content_type='text/html')
    else:
        # Retourner une réponse 404 si le fichier n'existe pas
        return HttpResponseNotFound("Fichier non trouvé")

