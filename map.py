from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import folium
from flask import Flask,send_file

mapa = folium.Map(location=[-15.793889, -47.882778], zoom_start=11)

folium.Marker(location=[-15.664972957076163, -48.1978452469064],
              popup='<b>UPA Brazlândia</b><br><p> Capacidade de atendimento: 4.500 pessoas/mês.<br>Profissionais de saúde: mais de 140, entre médicos, enfermeiros, técnicos de enfermagem, laboratoristas e pessoal administrativo.<br> Estrutura de Atendimento: Sala Verde: 10 poltronas para medicação,inalação e reidratação.<br>Sala Amarela: 6 leitos de observação e um leito individual.<br>Sala Vermelha:2 leitos para pacientes em situação crítica emergencial.<br>Sala de Classificação de Risco: 1 <br>Consultórios: 3 <br>Abastecimento de Oxigênio: Tanque de oxigênio instalado, quatro metros de altura. <br>Capacidade de armazenamento: 5.000 metros cúbicos de criogênicos, que são gases armazenados a baixas temperaturas, como o oxigênio e o nitrogênio.<br>Serviços Extras não exigidos pelo Ministério da Saúde:<br>Sala para exames de Raio-X <br>Laboratório para exames gerais<br> </p>',
              tooltip='Clique aqui para mais informações',icon=folium.Icon(color='blue',icon='info-sign')).add_to(mapa)

folium.Marker(location=[-15.824848200744162, -48.1212051314302],
              popup='UPA Ceilândia',
              tooltip='Clique aqui para mais informações',icon=folium.Icon(color='blue',icon='info-sign')).add_to(mapa)

folium.Marker(location=[-15.790586450587476, -48.13524771164782],
              popup='UPA Ceilândia II',
              tooltip='Clique aqui para mais informações',icon=folium.Icon(color='blue',icon='info-sign')).add_to(mapa)

folium.Marker(location=[-16.014122752744726, -48.05412108465914],
              popup='UPA Gama',
              tooltip='Clique aqui para mais informações',icon=folium.Icon(color='blue',icon='info-sign')).add_to(mapa)

folium.Marker(location=[-15.875315008774466, -47.98208366724949],
              popup='UPA Núcleo Bandeirante',
              tooltip='Clique aqui para mais informações',icon=folium.Icon(color='blue',icon='info-sign')).add_to(mapa)

folium.Marker(location=[-15.769534237335765, -47.78514135869146],
              popup='UPA Paranoá',
              tooltip='Clique aqui para mais informações',icon=folium.Icon(color='blue',icon='info-sign')).add_to(mapa)

folium.Marker(location=[-15.616316019859863, -47.691688],
              popup='UPA Planaltina',
              tooltip='Clique aqui para mais informações',icon=folium.Icon(color='blue',icon='info-sign')).add_to(mapa)

folium.Marker(location=[-15.911295746931572, -48.05735016931827],
              popup='UPA Recanto das Emas',
              tooltip='Clique aqui para mais informações',icon=folium.Icon(color='blue',icon='info-sign')).add_to(mapa)

folium.Marker(location=[-15.899507628091067, -48.040044169318264],
              popup='UPA Riacho Fundo II',
              tooltip='Clique aqui para mais informações',icon=folium.Icon(color='blue',icon='info-sign')).add_to(mapa)

folium.Marker(location=[-15.882624337884254, -48.1001645584189],
              popup='UPA Samambaia',
              tooltip='Clique aqui para mais informações',icon=folium.Icon(color='blue',icon='info-sign')).add_to(mapa)

folium.Marker(location=[-15.90005598621392, -47.77768083068174],
              popup='UPA São Sebastião',
              tooltip='Clique aqui para mais informações',icon=folium.Icon(color='blue',icon='info-sign')).add_to(mapa)

folium.Marker(location=[-15.63913039804857, -47.819696373011304],
              popup='UPA Sobradinho',
              tooltip='Clique aqui para mais informações',icon=folium.Icon(color='blue',icon='info-sign')).add_to(mapa)

folium.Marker(location=[-15.796877585587598, -48.02460908465915],
              popup='UPA Vicente Pires',
              tooltip='Clique aqui para mais informações',icon=folium.Icon(color='blue',icon='info-sign')).add_to(mapa)


app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#df = pd.read_excel("../dados_igesdf/07.06.2022.xlsx")
#df = pd.read_excel("../dados_igesdf/base_2020_2022.xlsx")

df = pd.read_excel("07.06.2022.xlsx")
dm = pd.read_csv("Infosaude2.csv", sep=";")


#CRIANDO O GRAFICO COM BASE NA PLANILHA
fig2 = px.bar(df, x="UNIDADE", y="TOTAL", color="TIPO", text_auto=True)
#fig = px.bar(df, x="EMPRESA", y="TOTAL", color="TIPO", barmode="group")
fig = px.pie(df,values='TOTAL', names='UNIDADE', title='Junho 2022')

fig3 = px.bar(dm, x="Mes", y="Total", color="Mes", text_auto=True)

app.layout = html.Div(children=[
    html.H1(children='Boletim IGESDF - ATENDIMENTOS '),
    html.H2(children='Data Inicial: 07/06/2022'),
    html.H2(children='Data Final: 07/06/2022'),
    html.Div(children='''
       Mês de Março'''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        ),
    html.Div(children='''
             Mês de Março'''),
    dcc.Graph(
        id='example-graph2',
        figure=fig2
    ),
    html.H2(children='''
Distribuição de Despesas por Mês no Ano de  2022'''),
    dcc.Graph(
        id='example-graph3',
        figure=fig3
    ),


    html.Div(children='''
Mapa de Unidades de Pronto Atendimento'''),
    html.Iframe(id='mapa', srcDoc=mapa._repr_html_(), width='100%', height='500')


])

server = app.server

@server.route('/exportar')
def exportar():
    arquivo = "Painel_IGESDF.html"
    app.index_string = open(arquivo, 'r').read()
    return app.index()


if __name__ == '__main__':
    app.run_server(debug=True)



