# IMPORT LIBRERIE
import gdown
import glob
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

def list_edf_files(base_folder, run_number):
    # Costruisci il pattern del file in base al numero di run fornito
    file_pattern = f"S*R01.edf"  # In questo dataset abbiamo solo la run 1
    # Crea il percorso completo per il pattern
    full_pattern = os.path.join(base_folder, file_pattern)
    # Usa glob per trovare tutti i file che corrispondono al pattern
    file_list = glob.glob(full_pattern)
    # Restituisce la lista dei percorsi dei file
    return file_list

# -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # 
