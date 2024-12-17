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

def convolutivo(classi, shape, filtri, dropout, strati, primo_sep=False):
    '''
    Funzione per creare il modello convolutivo.
    
    Parametri:
    - classi: numero di classi per la classificazione finale.
    - shape: input shape per il modello.
    - filtri: numero di filtri iniziali che si raddoppiano ad ogni strato.
    - dropout: percentuale di dropout, che si dimezza ad ogni strato.
    - strati: numero di strati convolutivi prima di passare al Dense.
    - primo_sep: se True, usa SeparableConv1D nel primo strato.
    '''
    
    # Aggiungi un layer di input all'inizio per specificare la forma
    inputs = tf.keras.layers.Input(shape)
    
    # Primo strato convolutivo, opzionalmente separabile
    if primo_sep:
        x = tf.keras.layers.SeparableConv1D(filters=filtri, kernel_size=5, padding='same', activation='relu')(inputs)
    else:
        x = tf.keras.layers.Conv1D(filters=filtri, kernel_size=3, padding='same', activation='relu')(inputs)
    
    # Aggiungi BatchNormalization e Dropout subito dopo il primo strato convolutivo
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Dropout(dropout)(x)
    
    # Utilizziamo strati convoluzionali per estrarre caratteristiche locali
    for i in range(1, strati):  
        filtri *= 2
        dropout /= 2
        x = tf.keras.layers.SeparableConv1D(filters=filtri, kernel_size=3, padding='same', activation='relu')(x)
        # Ad ogni ciclo, aggiungiamo un'ulteriore BatchNormalization e Dropout
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.Dropout(dropout)(x)
    

    # Appiattiamo tutto prima di passare al Dense
    x = tf.keras.layers.GlobalAveragePooling1D()(x)

    # Aggiungiamo uno strato Dense per la classificazione finale
    outputs = tf.keras.layers.Dense(classi, activation='softmax')(x)

    # Creiamo il modello
    model = tf.keras.Model(inputs=inputs, outputs=outputs)
    
    return model


# -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # 

def channel_names():
    
    '''
    Funzione per riportare il nome dei canali utilizzati dal dataset EEG Motor Movement/Imagery.
    
    '''
    ch_list = []
    ch_list = ['FC5', 'FC3', 'FC1', 'FCz', 'FC2', 'FC4', 'FC6', 'C5',
            'C3', 'C1', 'Cz', 'C2', 'C4', 'C6', 'CP5', 'CP3',
            'CP1', 'CPz', 'CP2', 'CP4', 'CP6', 'Fp1', 'Fpz', 'Fp2',
            'AF7', 'AF3', 'AFz', 'AF4', 'AF8', 'F7', 'F5', 'F3',
            'F1', 'Fz', 'F2', 'F4', 'F6', 'F8', 'FT7', 'FT8',
            'T7', 'T8', 'T9', 'T10', 'TP7', 'TP8', 'P7', 'P5',
            'P3', 'P1', 'Pz', 'P2', 'P4', 'P6', 'P8', 'PO7',
            'PO3', 'POz', 'PO4', 'PO8', 'O1', 'Oz', 'O2', 'Iz']
    
    return ch_list


# -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # 
