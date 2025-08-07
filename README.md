# 📊 Dashboard Interattiva per il Settore Primario

## Descrizione del Progetto

Questo progetto nasce come parte di un project work volto a sviluppare una **dashboard interattiva** in Python, pensata per supportare le aziende del settore primario nel **monitoraggio delle prestazioni ambientali e produttive**.  
La piattaforma consente la **visualizzazione dinamica** di variabili chiave (temperatura, precipitazioni, umidità del suolo, produzione agricola e consumo idrico), con l’obiettivo di facilitare il processo decisionale tramite strumenti accessibili e intuitivi.

## Link utili

- 🔍 **Demo online**: [Visualizza la dashboard](https://project-work-dashboard-settore-primario.onrender.com/)

## Tecnologie e librerie utilizzate

- [Python](https://docs.python.org/3/)
- [Pandas](https://pandas.pydata.org/docs/)
- [NumPy](https://numpy.org/doc/)
- [Plotly](https://plotly.com/python/)
- [Dash](https://dash.plotly.com/)
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)

## Funzionalità principali

- Simulazione realistica di dati ambientali e produttivi (365 giorni).
- Visualizzazione interattiva tramite grafici:
  - Grafico a linee per l’andamento giornaliero.
  - Grafici a barre per medie mensili.
  - Scatter plot e box plot per analisi delle correlazioni.
- Interfaccia web responsive e suddivisa in **tab tematici**.
- Struttura modulare e scalabile, predisposta all’integrazione con dati reali.

## Come eseguire il progetto in locale

1. Clona il repository:

```bash
git clone https://github.com/Kaminari94/PW-Dashboard-Agricola.git
cd PW-Dashboard-Agricola
```

2. Installa i pacchetti richiesti:

```bash
pip install -r requirements.txt
```

3. Avvia l’app:

```bash
python app.py
```

4. Apri il browser e visita:  
`http://127.0.0.1:8050/`

## Obiettivi

- Offrire una piattaforma semplice e accessibile per supportare le decisioni aziendali.
- Favorire una gestione più efficiente delle risorse naturali (acqua, suolo, clima).
- Promuovere la digitalizzazione anche in aziende agricole di piccole e medie dimensioni.

## Note aggiuntive

- I dati sono **simulati** per testare il comportamento della dashboard.
- Il codice è stato ottimizzato per ambienti web (es. [Render.com](https://render.com/)), ma può essere eseguito anche in locale.
- Il progetto è parte di un percorso formativo e può essere ampliato con l’aggiunta di:
  - input reali da sensori IoT
  - notifiche automatiche
  - modelli predittivi

## 💻 Autore

Oscar Vasso – 2025  
Corso di Laurea Triennale in Informatica per le aziende digitali – Classe L-31

## Licenza

Questo progetto è distribuito con licenza **MIT**, è liberamente riutilizzabile e modificabile.
