# Rilevamento Anomalie nel Traffico di Rete con Isolation Forest

Questo repository contiene un semplice script Python che dimostra come utilizzare l'Isolation Forest, un algoritmo di apprendimento automatico, per rilevare anomalie nel traffico di rete utilizzando dati di lunghezza dei pacchetti.

## Requisiti

- Python 3.x
- Librerie Python: pandas, scapy, scikit-learn

## Utilizzo

1. Assicurati di aver installato tutte le librerie necessarie. Puoi farlo utilizzando `pip`:

   ```shell
   pip install pandas scapy scikit-learn
   
2.Esegui lo script Python fornito:

python network_anomaly_detection.py

Lo script catturerà il traffico di rete in tempo reale e utilizzerà l'Isolation Forest per rilevare anomalie nella lunghezza dei pacchetti.

#Dettagli dell'applicazione

    Il codice crea un DataFrame di esempio con dati di lunghezza dei pacchetti.
    Normalizza i dati utilizzando lo StandardScaler di scikit-learn.
    Utilizza l'Isolation Forest per addestrare un modello di rilevamento delle anomalie.
    Durante la cattura del traffico di rete, estrae la lunghezza del pacchetto e utilizza il modello per rilevare anomalie.
    Se viene rilevata un'anomalia, lo script stamperà un messaggio di avviso.

#Personalizzazione

Questo script è un esempio di base di come utilizzare l'Isolation Forest per il rilevamento delle anomalie nel traffico di rete. Puoi personalizzare ulteriormente il codice aggiungendo funzionalità come la memorizzazione dei dati, la registrazione delle anomalie o l'adattamento a diversi tipi di dati di traffico.
Note

    Questo è un esempio educativo e dimostrativo. Assicurati di utilizzare dati reali e un modello di rilevamento delle anomalie più sofisticato per scopi di sicurezza del traffico di rete in un ambiente di produzione.
