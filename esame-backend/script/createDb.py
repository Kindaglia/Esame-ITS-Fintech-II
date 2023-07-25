import mysql.connector

def createDb():
    db_config = {
        'host': 'localhost',
        'port': 3307,
        'user': 'root',
        'password': ''
    }

    # Connessione al database
    db_conn = mysql.connector.connect(**db_config)

    # Creazione del database e della tabella
    cursor = db_conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS esame")
    cursor.execute("USE esame")
    cursor.execute("CREATE TABLE IF NOT EXISTS produttivita_pesca (id INT AUTO_INCREMENT PRIMARY KEY, regione VARCHAR(255), anno INT, produttivitaPesca FLOAT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS media_percentuale (id INT AUTO_INCREMENT PRIMARY KEY, regione VARCHAR(255), anno INT, media_percentuale FLOAT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS media_variazione (id INT AUTO_INCREMENT PRIMARY KEY, regione VARCHAR(255), anno INT, media_variazione FLOAT)")

    return db_conn