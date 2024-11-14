![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MNE](https://img.shields.io/badge/MNE-blue?style=for-the-badge&logoColor=orange&labelColor=blue&color=blue)



# EEG Recognition
<p align="justify">
L'obiettivo principale di questa repository è di sviluppare un sistema di riconoscimento personale basato su segnali EEG, analizzando l’impatto delle diverse bande di frequenza e sperimentando con differenti combinazioni di preprocessing al fine di valutare le prestazioni del nostro classificatore convolutivo.
Successivamente, basandoci sui risultati ottenuti, per rispondere sfide chiave in questo campo (l’importanza della robustezza e della generalizzazione nel riconoscimento EEG al variare degli stati mentali) è stata svolta una ricerca approfondita riguardo la capacità di generalizzazione di un classificatore Ensamble su dati simili e non identici a quelli utilizzati in fase di addestramento.</p>

 
# Dataset utilizzato
<p align="justify">Per il progetto è stata utilizzata una sottoporzione del dataset <i>"EEG Motor Movement/Imagery"</i>, scaricabile da <a href="https://drive.usercontent.google.com/download?id=1WwuAh25Jfx-I8rY3vFGyXiI79YfLYUpH&authuser=0">questo link</a>. Il dataset orginale è composto da 14 diverse esecuzioni sperimentali ottenute da 109 volontari; nel nostro caso è stata utilizzata soltanto la run 01 per raggiungere l'obiettivo principale. Successivamente son state utilizzate la run 02 e la run 06 per addestrare separatamente altri due classificatori convolutivi, utilizzati assieme al precedentemente costruito per formare un Ensamble testato sulle run 03, 04 e 05. Ogni subset utilizzato è pertanto formato da 109 EEG composti da 64 canali registrati utiizzando il sistema BCI2000. Il repository contiene i notebooks e i file necessari per scaricare i vari subset. Ulteriori informazioni riguardo il dataset originale si possono reperire al seguente <a href="https://physionet.org/content/eegmmidb/1.0.0/"> link</a></p>

# Installazione
## **Requisiti:**   
L'unico requisito è un account Google per poter accedere a  <a href="https://drive.google.com/">Google Drive</a> e salvare la cartella contenente i notebooks da eseguire tramite <a href="https://colab.research.google.com">Google Colab</a>.     

## **Istruzioni step-by-step:**   
1) Scaricare i file da GitHub e caricarli su Google Drive nella **<u>stessa cartella</u>**;     
 **NOTA:** _È fortemente consigliato di creare la cartella del progetto nella propria home su Google Drive. Qualora si voglia comunque utilizzare una cartella differente sarà necessario aggiornare il percorso della cartella su ogni notebook._

2) In qualsiasi notebook verrà chiesto di inserire il percorso della cartella Google Drive dove sono contenuti i vari file. Una volta impostata sarà possibile eseguire i notebooks;<br>
 **NOTA:** _Il percorso va impostato manualmente in qualsiasi notebook al momento del suo primo utilizzo, poi rimarrà salvato e non ci sarà bisogno di inserirlo nuovamente._

# Struttura del progetto
Il progetto è stato organizzato in più notebooks/files in base ai modelli e alle operazioni da effettuare:

<div align="center">

| Nome File | Descrizione |
| :---: | :---: |
| `Analisi Dataset_e_Preprocessing.ipynb` | Notebook per l'analisi del dataset, svolgimento di vari tipi di preprocessing e download dei file .npy pronti per il Convolutivo |
| `Classificatore_Convolutivo.ipynb`| Notebook per l'addestramento del modello convolutivo. Permette anche di salvare e caricare configurazioni già pronte |
| `Download_Subset_e_Preprocessing.ipynb`| Permette di prelevare altre run del dataset originale, eseguire il preprocessing definitivo e salvare tutto in file .npy.  |
| `Classificatore_Ensamble.ipynb`| Permette di caricare i modelli pre-addestrati su run 01, 02 e 06 e di combinare le predizioni da testare su un'altra specifica run.  |
| `Risultati.ipynb`| Notebook dove vengono esposti brevemente i risultati riepilogativi del progetto.  |
| `shared_utilities.py`| File python contenente le funzioni condivise fra i vari notebooks |
| `EEG_Motor_Movement-Imagery_ID.json`| File di configurazione per download del subaset iniziale inerente la run 01 (zippato e più veloce rispetto agli altri) |

</div>

# Autori
<a href="https://github.com/Cipe96/EEG-Recognition/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=cipe96/EEG-Recognition"/>
</a>  
