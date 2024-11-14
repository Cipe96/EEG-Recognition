# IMPORT LIBRERIE
import tensorflow as tf
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

def convolutivo(classi, shape, filtri, dropout, strati):
  '''
  Funzione per scaricare il dataset.
  
  Parametri:
  - shape: Input shape per il modello.
  - filtri: numero di filtri iniziali che si raddoppiano ad ogni strato.
  - dropout: si dimezza ad ogni strato ed è la percentuale di dati che dimentica per migliorare la generalizzazione.
  - strati: numero di strati convolutivi prima di passare al Dense
  '''
  
  # Aggiungi un layer di input all'inizio per specificare la forma
  inputs = tf.keras.layers.Input(shape)

  # Utilizziamo strati convoluzionali per estrarre caratteristiche locali
  for i in range(strati):
    if i == 0:
      x = tf.keras.layers.Conv1D(filters=filtri, kernel_size=3, padding='same', activation='relu')(inputs)
    else:
      x = tf.keras.layers.SeparableConv1D(filters=filtri, kernel_size=3, padding='same', activation='relu')(inputs)

    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Dropout(dropout)(x)

    filtri *= 2
    dropout /= 2

  #Appiattiamo tutto primo di consegnare al Dense
  x = tf.keras.layers.GlobalAveragePooling1D()(x)

  # Aggiungiamo uno strato Dense per la classificazione finale
  outputs = tf.keras.layers.Dense(classi, activation='softmax')(x)

  model = tf.keras.Model(inputs=inputs, outputs=outputs)
  
  return model

# -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # 
