# Esame-ITS-Fintech-II

Esame fatto in 6 ore

# Start

Per avviare il progetto:

- mettersi dentro la cartella esame-backend ed installare i requirements.txt
- mettersi dentro la cartella esame-frontend fare "npm i" e "npm start"

# Scelta tecnologie

Una volta letta la traccia ho scelto di sviuluppare l'applicazione mediante il database mysql, backend in python(flask) e frontend in angular
Ho preferito python poichè secondo me era più adeguato per trattre i tipi di dati di cui si aveva a disposizione.

# Sviluppo

## Creazione db

All'avvio dell applicazione viene creato il db in mysql chiamato "Esame" e popolato come nel segunte punto

## Script importazione dati

Nella sezione script vi sono degli script che leggono i dati presi da csv nella directory data e li leggono, una volta letti vengono caricati all'interno del database

## Post processing

Sempre nella sezione script è stato un lavoro di post processo nel quale i dati vengono oraganizzati tramite rinomino di tabelle e viene fatto anche un check dei dati

## Calcolo serie calcolate

Per fare questa operazione viene fatta una get, nel quale i dati vengono presi e rielaborati, nel caso richieste totali suddivise per anni viene fatta una somma dei valori e poi raggrupate per le regione precedente raggruppate , mentre per i calcoli a cui si fa riferimento al totNazione viene fatta una somma di essi e poi restiutita.
Tutti questi dati suddivisi per anno come richeisto.

## Esportazione CSV

Per l'esportazione in csv invece son state fatte altre chimate get nel quale si può passare un filtro (da anno, a anno) oppure no e tale chiamata scarica i dati tramtie csv

# Frontend

Per quanto riguarda il forntend è stato fatto un menubar dove è possibile muoversi all interno dell applicazione, nelle varie tab ho messo le tabelle principali delle serie calcolate per mostrarle all'utente.

## Autore

- Matteo Drago
