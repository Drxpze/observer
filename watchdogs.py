import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Usuario/Downloads/"
to_dir = "C:/Users/Usuario/Downloads/Arquivos_baixados"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Classe Gerenciadora de Eventos

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(event)
        print(event.src_path)
        name,extension = os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                
                filename = os.path.basename(event.src_path)
                print("baixado",filename)
                path1 = from_dir + filename
                path2 = to_dir + key
                path3 = to_dir + key + "/" + filename
                if os.path.exists(path2):
                    print("movendo",filename)
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    print("criando diretorio")
                    os.makedirs(path2)
                    print("movendo",filename)
                    shutil.move(path1,path3)
                    time.sleep(1)
    def on_deleted(self, event):
        print(f"opa , alguem me excluiu{event.src_path}!")
            


# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileMovementHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicie o Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("o programa foi interrompido")
    observer.stop()
    