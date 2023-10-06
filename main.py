import pandas as pd
from sklearn.ensemble import IsolationForest
from scapy.all import *
from sklearn.preprocessing import StandardScaler

# Creare un dataset di esempio (in questo caso, usiamo dati di traffico di rete)
def create_sample_dataset():
    # Crea un DataFrame di esempio
    data = {'Packet Length': [100, 120, 130, 140, 200, 400, 500, 1000, 2000, 5000]}
    df = pd.DataFrame(data)
    return df

# Esempio di funzione per rilevare anomalie
def detect_anomalies(df):
    # Normalizza i dati
    scaler = StandardScaler()
    df['Packet Length'] = scaler.fit_transform(df[['Packet Length']])

    # Crea un modello Isolation Forest
    model = IsolationForest(contamination=0.1, random_state=42)

    # Addestra il modello sui dati
    model.fit(df)

    # Predici le anomalie (1 se normale, -1 se anomalia)
    df['Anomaly'] = model.predict(df)

    return df

# Funzione di callback per catturare pacchetti di rete
def packet_callback(packet):
    # Estrai caratteristiche dai pacchetti (in questo caso, la lunghezza del pacchetto)
    packet_length = len(packet)

    # Creare un DataFrame con le caratteristiche
    df = create_sample_dataset()
    df.loc[len(df)] = [packet_length]

    # Rileva anomalie
    df = detect_anomalies(df)

    # Stampa il risultato
    if df.iloc[-1]['Anomaly'] == -1:
        print("Anomaly detected!")

# Cattura il traffico di rete in tempo reale
sniff(filter="tcp", prn=packet_callback)
