import plotly.express as px
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

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
graf_temp = px.line(df, x='Data', y='Temperatura (°C)', title="Andamento della Temperatura (°C)").update_traces(line_color="#70C570")
graf_umidita = px.line(df, x='Data', y='Umidità del Suolo (%)', title="Andamento dell'Umidità del Suolo (%)")
graf_precip = px.line(df, x='Data', y='Precipitazioni (mm)', title="Andamento delle Precipitazioni (mm)").update_traces(line_color="#C50EBC")
graf_prod = px.line(df, x='Data', y='Produzione (kg)', title="Andamento della Produzione Agricola (kg)").update_traces(line_color="#C5334E")
graf_consumo = px.line(df, x='Data', y='Consumo Idrico (litri)', title="Andamento del Consumo Idrico (litri)").update_traces(line_color="#C5C345")

scatter_umidita = px.scatter(df, x='Umidità del Suolo (%)', y='Produzione (kg)', title="Relazione tra Umidità del Suolo e Produzione", template="presentation")
scatter_temp = px.scatter(df, x='Temperatura (°C)', y='Produzione (kg)', title="Relazione tra Temperatura e Produzione", template="ggplot2")
box_precip = px.box(df, x='Precipitazioni (mm)', y='Produzione (kg)', title="Relazione tra Precipitazioni e Produzione", template="seaborn")

df['Mese'] = df['Data'].dt.month

mesi_mapping = {
    1: 'Gennaio', 2: 'Febbraio', 3: 'Marzo', 4: 'Aprile',
    5: 'Maggio', 6: 'Giugno', 7: 'Luglio', 8: 'Agosto',
    9: 'Settembre', 10: 'Ottobre', 11: 'Novembre', 12: 'Dicembre'
} #Mappa dei mesi in italiano (manca il locale IT_it sulla macchina render.com e nel piano gratuito non c'è accesso alla console.)

df['Mese_Ordinato'] = df['Mese'].map(mesi_mapping)

media_mensile = df.sort_values('Mese_Ordinato').groupby('Mese_Ordinato')[['Produzione (kg)', 'Consumo Idrico (litri)']].mean()
ordine_cronologico = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno',
                      'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']

graf_comp.update_layout(legend_title_text='Variabile')
graf_comp.update_yaxes(title="Valore")

graf_barre = px.bar(media_mensile, x=media_mensile.index, y='Produzione (kg)', title="Valori Medi Mensili di Produzione in kg").update_traces(marker_color="#70C570")
graf_barre.update_xaxes(title="Mese", categoryorder='array', categoryarray=ordine_cronologico) #Ordina mesi in italiano in ordine cronologico e non alfabetico
graf_barre.update_yaxes(title="Valore")
graf_barre.update_traces(hovertemplate='<b>Variabile: Produzione(kg)</b><br>Mese: %{label}<br>Valore: %{value} kg<extra></extra>')
graf_barre.update_layout(height=600)

graf_idrico = px.bar(media_mensile, x=media_mensile.index, y='Consumo Idrico (litri)', title="Valori Medi Mensili di Consumo Idrico in litri").update_traces(marker_color="#E45F00")
graf_idrico.update_xaxes(title="Mese", categoryorder='array', categoryarray=ordine_cronologico) #Ordina mesi in italiano in ordine cronologico e non alfabetico
graf_idrico.update_yaxes(title="Valore")
graf_idrico.update_traces(hovertemplate='<b>Variabile: Consumo Idrico (lt)</b><br>Mese: %{label}<br>Valore: %{value} lt<extra></extra>')
graf_idrico.update_layout(height=600)

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
            dcc.Graph(figure=graf_barre),
            dcc.Graph(figure=graf_idrico)
        ]),

        dcc.Tab(label='Relazioni tra Variabili', children=[
            dcc.Graph(figure=scatter_umidita),
            dcc.Graph(figure=scatter_temp),
            dcc.Graph(figure=box_precip)
        ]),
    ])
]))

if __name__ == '__main__':
    app.run(debug=False)

