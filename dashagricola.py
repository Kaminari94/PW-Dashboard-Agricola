import plotly.express as px
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import locale

locale.setlocale(locale.LC_ALL, 'it_IT')
temperatura = np.random.normal(loc=20, scale=5, size=365)
umidita_suolo = np.random.uniform(low=10, high=50, size=365)
precip = np.random.poisson(lam=5, size=365)
produzione = np.random.normal(loc=500, scale=50, size=365)
acqua = produzione * np.random.normal(loc=1.2, scale=0.1, size=365)

df = pd.DataFrame({
    'Data': pd.date_range(start='2025-01-01', periods=365, freq='D'),
    'Temperatura (°C)': temperatura,
    'Umidità del Suolo (%)': umidita_suolo,
    'Precipitazioni (mm)': precip,
    'Produzione (kg)': produzione,
    'Consumo Idrico (litri)': acqua
})

graf_comp = px.line(df, template='seaborn', x='Data', y=['Temperatura (°C)', 'Umidità del Suolo (%)', 'Precipitazioni (mm)', 'Produzione (kg)', 'Consumo Idrico (litri)'], title="Panoramica Generale delle Variabili e Comparazione")
#Grafici Singoli
graf_temp = px.line(df, x='Data', y='Temperatura (°C)', title="Andamento della Temperatura (°C)")
graf_umidita = px.line(df, x='Data', y='Umidità del Suolo (%)', title="Andamento dell'Umidità del Suolo (%)")
graf_precip = px.line(df, x='Data', y='Precipitazioni (mm)', title="Andamento delle Precipitazioni (mm)")
graf_prod = px.line(df, x='Data', y='Produzione (kg)', title="Andamento della Produzione Agricola (kg)")
graf_consumo = px.line(df, x='Data', y='Consumo Idrico (litri)', title="Andamento del Consumo Idrico (litri)")

scatter_umidita = px.scatter(df, x='Umidità del Suolo (%)', y='Produzione (kg)', title="Relazione tra Umidità del Suolo e Produzione")
scatter_temp = px.scatter(df, x='Temperatura (°C)', y='Produzione (kg)', title="Relazione tra Temperatura e Produzione")
box_precip = px.box(df, x='Precipitazioni (mm)', y='Produzione (kg)', title="Relazione tra Precipitazioni e Produzione", )

df['Mese'] = df['Data'].dt.month_name(locale = 'Italian')
media_mensile = df.groupby('Mese')[['Produzione (kg)', 'Consumo Idrico (litri)']].mean()
ordine_cronologico = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno',
                      'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']
graf_barre = px.bar(media_mensile, x=media_mensile.index, y=['Produzione (kg)', 'Consumo Idrico (litri)'], title="Valori Medi Mensili di Produzione e Consumo Idrico")
graf_comp.update_layout(legend_title_text='Variabile')
graf_comp.update_yaxes(title="Valore")
graf_barre.update_xaxes(categoryorder='array', categoryarray=ordine_cronologico) #Ordina mesi in italiano in ordine cronologico e non alfabetico
graf_barre.update_yaxes(title="Valore")
graf_barre.update_traces(hovertemplate='<b>Variabile: %{data.name}</b><br>Mese: %{label}<br>Valore: %{value}<extra></extra>') #INSERIRE NOME VARIABILE
graf_barre.update_layout(legend_title_text='Variabile')

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Layout della dashboard (con tab per raggruppare grafici)
app.layout = (
    html.Div(className="m-3", children=[
    html.H1("Dashboard per il Settore Primario"),  # Titolo della dashboard
    html.Div(children='''
        Un'app in Dash e Plotly che fornisce strumenti per l'analisi delle performance aziendali
         come la produzione agricola in relazione ai fattori ambientali (temperatura, umidità, precipitazioni).
         Singolo click sulla variabile in legenda per nasconderla.
         Doppio click sulla variabile in legenda per selezionarla singolarmente.
    '''),
    html.Br(),

    dcc.Tabs([
        dcc.Tab(label='Andamento Giornaliero', children=[
            dcc.Graph(figure=graf_comp),
            html.H2("Vista in Depth, per Variabile"),
            dcc.Graph(figure=graf_temp),
            dcc.Graph(figure=graf_umidita),
            dcc.Graph(figure=graf_precip),
            dcc.Graph(figure=graf_prod),
            dcc.Graph(figure=graf_consumo)
        ]),

        dcc.Tab(label='Analisi Mensile', children=[
            dcc.Graph(figure=graf_barre)
        ]),

        dcc.Tab(label='Relazioni tra Variabili', children=[
            dcc.Graph(figure=scatter_umidita),
            dcc.Graph(figure=scatter_temp),
            dcc.Graph(figure=box_precip)
        ]),
    ])
]))

if __name__ == '__main__':
    app.run_server(debug=False)

