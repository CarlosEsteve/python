# filepath: C:/repo_remoto/python/Pandas/tasks.py
import requests
from invoke import task

@task
def download_notebook(c, url, output):
    response = requests.get(url)
    if response.status_code == 200:
        with open(output, 'wb') as f:
            f.write(response.content)
        print(f"Notebook descargado y guardado en {output}")
    else:
        print(f"Error al descargar el notebook: {response.status_code}")