import pandas as pd
from script import process
import mysql.connector



def insert_prod(conn):
  df = pd.read_csv('data/produttivita_pesca.csv', delimiter=';', encoding='ISO-8859-1')
  #guarda se ci sono valori mancanti e li fixa
  process.interpola_valori_mancanti(df)
  #rinomina in modo le regioni rafunandole
  process.sostituisci_nomi_regioni(df)
  #li raggruppa insieme
  df_grouped = df.groupby(['Regione', 'Anno'], as_index=False).agg({'Produttività in migliaia di euro': 'sum'})
  #rinomino gli header delle tabelle
  df_grouped = df_grouped.rename(columns={'Anno': 'anno', 'Regione': 'regione', 'Produttività in migliaia di euro': 'produttivitaPesca'})
  #li ordino per nome
  df_sorted = df_grouped.sort_values('anno')
  print(df_sorted.to_string())
  cursor = conn.cursor()
  data = [tuple(x) for x in df_sorted.to_numpy()]
  sql = "INSERT INTO produttivita_pesca (regione, anno, produttivitaPesca) VALUES (%s, %s, %s)"

  for row in data:
      cursor.execute(sql, row)
  conn.commit()