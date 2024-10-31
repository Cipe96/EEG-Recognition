# IMPORT LIBRERIE
import gdown
import os
# -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # 

def download_dataset(file_id, output, msg=False):
  '''
  Funzione per scaricare il dataset.
  
  Parametri:
  - file_id: ID del file su Google Drive.
  - output: nome da assegnare al file appena scaricato.
  - msg: se True, stampa il messaggio alla fine del download (default = False).
  '''
  
  url = f'https://drive.google.com/uc?id={file_id}'
  gdown.download(url, output, quiet=False)
  if msg:
    print(f"\nFile scaricato e salvato come {output}!\n")

# -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # 
