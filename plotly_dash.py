import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash
from dash import html
from dash import dcc

data = px.data.gapminder()

app = dash.Dash()

app.layout = html.Div([
    html.Div(children=[html.H1("My First Dashboard", style={'color':'red', 'text-align':'center'})],
             style={'border':'1px black solid', 'float':'left', 'width':'100%', 'height':'50px'}),
    html.Div(children=[
        dcc.Graph(id="Scatter plot",
                  figure={'data':[go.Scatter(x=data['gdpPercap'],
                                             y=data['lifeExp'],
                                             mode='markers')],
                            'layout':go.Layout(title="Scatter plot")})
    ],style={'border':'1px black solid', 'float':'left', 'width':'49%', 'heigth':'350px'}),
    html.Div(children=[
        dcc.Graph(id="Box plot",figure={
            'data':[go.Box(x=data['lifeExp'])],
            'layout':go.Layout(title="Boxplot")
        })
    ],style={'border':'1px black solid', 'float':'left', 'width':"49%", 'height':'350px'})
])


if __name__ == '__main__':
    app.run_server()




"""
external_stylesheets = [
    {
        'href' : 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel' : 'stylesheet',
        'integrity' : 'sha384-MCw98/SFnGE8fJT3GXwEOngsv7Zt27NXFoaoApmYm81iuXoPKFOJwJ8ERdKnLPMO',
        'crossorigin' : 'anonymous'
    }
]

patients = pd.read_csv("IndividualDetails.csv")
total = patients.shape[0]
Active = patients[patients['current_status'] == 'Hospitalized'].shape[0]
recovered = patients[patients['current_status'] == 'Recovered'].shape[0]
deaths = patients[patients['current_status']=='Deceased'].shape[0]
total_cases = patients['detected_state'].value_counts().head(10).reset_index()
options = [
    {'label': 'All', 'value': 'All'},
    {'label': 'Hospitalized', 'value': 'Hospitalized'},
    {'label': 'Recovered', 'value' :' Recovered'},
    {'label': 'Deceased', 'value': 'Deceased'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("Corona virus pandemic", style={'color':'green', 'text-align':'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Cases", className='text-light'),
                    html.H4(total, className='text-light')
                ], className='card-body')
            ], className='card bg-danger')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active Cases", className='text-light'),
                    html.H4(Active, className='text-light')
                ], className='card-body')
            ], className='card bg-danger')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered", className='text-light'),
                    html.H4(recovered, className='text-light')
                ], className='card-body')
            ], className='card bg-danger')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Deaths", className='text-light'),
                    html.H4(deaths, className='text-light')
                ], className='card-body')
            ], className='card bg-danger')
        ], className='col-md-3')
    ], className='row'),
    html.Div([], className='row '),
    html.Div([
        html.Div([
            html.Div([
                html.Div([

                    dcc.Graph(id='bar', figure={'data': [go.Histogram(patients['age'])],
                                                'layout':go.Layout(title="Bar graph")})
                ], className='card-body')
            ], className='card')
        ], className='col-md-12')
    ], className='row')
], className='container')



if __name__ == '__main__':
    app.run_server(debug=True)
"""