import pandas as pd

def sostituisci_nomi_regioni(df):
    df['Regione'] = df['Regione'].replace(['Valle d\'Aosta', 'Piemonte', 'Liguria', 'Lombardia'], 'Nord-ovest')
    df['Regione'] = df['Regione'].replace(['Trentino-Alto Adige', 'Veneto', 'Friuli-Venezia Giulia', 'Emilia-Romagna'], 'Nord-est')
    df['Regione'] = df['Regione'].replace(['Toscana', 'Umbria', 'Marche', 'Lazio', 'Abruzzo'], 'Centro')
    df['Regione'] = df['Regione'].replace(['Molise', 'Campania', 'Puglia', 'Basilicata', 'Calabria'], 'Sud')
    df['Regione'] = df['Regione'].replace(['Sicilia', 'Sardegna'], 'Isole')
    return df

def interpola_valori_mancanti(df):
    if df.isnull().values.any():
        df = df.interpolate()
    return df

