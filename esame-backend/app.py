from flask import Flask,request, jsonify, make_response
import mysql.connector
from script import createDb
from script import produttivita
from script import media_percentuale
from script import media_variazione
from script import process
import pandas as pd
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

db_conn = createDb.createDb()
produttivita.insert_prod(db_conn)
media_percentuale.insert_prod(db_conn)
media_variazione.insert_prod(db_conn)

@app.route('/produttivita_pesca')
def get_produttivita_pesca():
    cursor = db_conn.cursor()
    query = "SELECT regione, anno, produttivitaPesca FROM produttivita_pesca"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(rows, columns=['regione', 'anno', 'produttivitaPesca'])
    result = df.to_dict('records')
    return jsonify(result)


@app.route('/produttivita_pesca_nazionale')
def get_produttivita_pesca_nazionale():
    cursor = db_conn.cursor()
    query = "SELECT regione, anno, produttivitaPesca FROM produttivita_pesca"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(rows, columns=['regione', 'anno', 'produttivitaPesca'])
    print(df.to_string())
    df_somma_anno = df.groupby('anno')['produttivitaPesca'].sum().reset_index()
    print(df_somma_anno.to_string())
    result = df_somma_anno.to_dict('records')
    return jsonify(result)


@app.route('/media_percentuale')
def get_media_percentuale():
    cursor = db_conn.cursor()
    query = "SELECT regione, anno, media_percentuale FROM media_percentuale"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(rows, columns=['regione', 'anno', 'media_percentuale'])
    result = df.to_dict('records')
    return jsonify(result)

@app.route('/media_variazione')
def get_media_variazione():
    cursor = db_conn.cursor()
    query = "SELECT regione, anno, media_variazione FROM media_variazione"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(rows, columns=['regione', 'anno', 'media_variazione'])
    result = df.to_dict('records')
    return jsonify(result)

@app.route('/media_variazione_nazionale')
def media_variazione_nazionale():
    cursor = db_conn.cursor()
    query = "SELECT regione, anno, media_variazione FROM media_variazione"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(rows, columns=['regione', 'anno', 'media_variazione'])
    df_somma_anno = df.groupby('anno')['media_variazione'].mean().reset_index()
    print(df_somma_anno.to_string())
    result = df_somma_anno.to_dict('records')
    return jsonify(result)


# esportazione
@app.route('/produttivita_pesca_filter')
def get_produttivita_pesca_filter():
    cursor = db_conn.cursor()
    anno_inizio = request.args.get('anno_inizio')
    anno_fine = request.args.get('anno_fine')
    if anno_inizio and anno_fine:
        query = "SELECT regione, anno, produttivitaPesca FROM produttivita_pesca WHERE anno BETWEEN %s AND %s"
        cursor.execute(query, (anno_inizio, anno_fine))
    else:
        query = "SELECT regione, anno, produttivitaPesca FROM produttivita_pesca"
        cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(rows, columns=['regione', 'anno', 'produttivitaPesca'])
    df.sort_values(by='anno', inplace=True)
    result = df.to_dict('records')
    csv = df.to_csv(index=False)
    response = make_response(csv)
    response.headers.set("Content-Disposition", "attachment", filename="produttivita_pesca.csv")
    response.headers.set("Content-Type", "text/csv")
    return response

@app.route('/produttivita_pesca_nazionale_filter')
def get_produttivita_pesca_nazionale_filter():
    cursor = db_conn.cursor()
    anno_inizio = request.args.get('anno_inizio')
    anno_fine = request.args.get('anno_fine')
    if anno_inizio and anno_fine:
        query = "SELECT regione, anno, produttivitaPesca FROM produttivita_pesca WHERE anno BETWEEN %s AND %s"
        cursor.execute(query, (anno_inizio, anno_fine))
    else:
        query = "SELECT regione, anno, produttivitaPesca FROM produttivita_pesca"
        cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(rows, columns=['regione', 'anno', 'produttivitaPesca'])
    df_somma_anno = df.groupby('anno')['produttivitaPesca'].sum().reset_index()
    print(df_somma_anno.to_string())
    df.sort_values(by='anno', inplace=True)
    result = df.to_dict('records')
    csv = df.to_csv(index=False)
    response = make_response(csv)
    response.headers.set("Content-Disposition", "attachment", filename="produttivita_pesca.csv")
    response.headers.set("Content-Type", "text/csv")
    return response


@app.route('/media_percentuale_filter')
def get_media_percentuale_filter():
    cursor = db_conn.cursor()
    anno_inizio = request.args.get('anno_inizio')
    anno_fine = request.args.get('anno_fine')
    if anno_inizio and anno_fine:
        query = "SELECT regione, anno, media_percentuale FROM media_percentuale WHERE anno BETWEEN %s AND %s"
        cursor.execute(query, (anno_inizio, anno_fine))
    else:
        query = "SELECT regione, anno, media_percentuale FROM media_percentuale"
        cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(rows, columns=['regione', 'anno', 'media_percentuale'])
    df.sort_values(by='anno', inplace=True)
    result = df.to_dict('records')
    csv = df.to_csv(index=False)
    response = make_response(csv)
    response.headers.set("Content-Disposition", "attachment", filename="media_percentuale.csv")
    response.headers.set("Content-Type", "text/csv")
    return response


@app.route('/media_variazione_filter')
def get_media_variazione_filter():
    cursor = db_conn.cursor()
    anno_inizio = request.args.get('anno_inizio')
    anno_fine = request.args.get('anno_fine')
    if anno_inizio and anno_fine:
        query = "SELECT regione, anno, media_variazione FROM media_variazione WHERE anno BETWEEN %s AND %s"
        cursor.execute(query, (anno_inizio, anno_fine))
    else:
        query = "SELECT regione, anno, media_variazione FROM media_variazione"
        cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(rows, columns=['regione', 'anno', 'media_variazione'])
    df.sort_values(by='anno', inplace=True)
    result = df.to_dict('records')
    csv = df.to_csv(index=False)
    response = make_response(csv)
    response.headers.set("Content-Disposition", "attachment", filename="media_variazione.csv")
    response.headers.set("Content-Type", "text/csv")
    return response



@app.route('/media_variazione_nazionale_filter')
def get_media_variazione_filter_nazionale():
    cursor = db_conn.cursor()
    anno_inizio = request.args.get('anno_inizio')
    anno_fine = request.args.get('anno_fine')
    if anno_inizio and anno_fine:
        query = "SELECT regione, anno, media_variazione FROM media_variazione WHERE anno BETWEEN %s AND %s"
        cursor.execute(query, (anno_inizio, anno_fine))
    else:
        query = "SELECT regione, anno, media_variazione FROM media_variazione"
        cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(rows, columns=['regione', 'anno', 'media_variazione'])
    df = df.groupby('anno')['media_variazione'].mean().reset_index()
    print(df.to_string())
    csv = df.to_csv(index=False)
    response = make_response(csv)
    response.headers.set("Content-Disposition", "attachment", filename="media_variazione.csv")
    response.headers.set("Content-Type", "text/csv")
    return response

#esportazione 3 tabelle 
@app.route('/produttivita_pesca_standard')
def get_produttivita_pesca_standard():
    df = pd.read_csv('data/produttivita_pesca.csv', delimiter=';', encoding='ISO-8859-1')
    csv = df.to_csv(index=False)
    response = make_response(csv)
    response.headers.set("Content-Disposition", "attachment", filename="produttivita_pesca.csv")
    response.headers.set("Content-Type", "text/csv")
    return response
@app.route('/media_percentuale_standard')
def get_media_percentuale_standard():
    df = pd.read_csv('data/importanza_pesca.csv', delimiter=';', encoding='ISO-8859-1')
    csv = df.to_csv(index=False)
    response = make_response(csv)
    response.headers.set("Content-Disposition", "attachment", filename="produttivita_pesca.csv")
    response.headers.set("Content-Type", "text/csv")
    return response
@app.route('/media_variazione_standard')
def get_media_variazione_standard():
    df = pd.read_csv('data/andamento.csv', delimiter=';', encoding='ISO-8859-1')
    csv = df.to_csv(index=False)
    response = make_response(csv)
    response.headers.set("Content-Disposition", "attachment", filename="produttivita_pesca.csv")
    response.headers.set("Content-Type", "text/csv")
    return response

if __name__ == '__main__':
    app.run()