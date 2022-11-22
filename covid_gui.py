import pandas as pd
import numpy as np
import dash
from dash import dcc
from dash import html
import dash_daq as daq
from dash.dependencies import Input, Output
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets )


df = pd.read_excel("C:/Users/DELL/Downloads/saka.xlsx")

app.layout = html.Div(
    [
        html.H1("Africa COVID-19 Data", style={'textAlign': 'center'}),
            html.Br(),

            html.Div(
                dcc.Dropdown(
                    id='select_country',
                    options=[
                        {'label': 'Algeria', 'value': 'Algeria'},
                        {'label': 'Angola', 'value': 'AAngola'},
                        {'label': 'Benin', 'value': 'Benin'},
                        {'label': 'Botswana', 'value': 'Botswana'},
                        {'label': 'Burkinafoso', 'value': 'Burkinafoso'},
                        {'label': 'Burundi', 'value': 'Burundi'},
                        {'label': 'Cameroon', 'value': 'Cameroon'},
                        {'label': 'Capverde', 'value': 'Capverde'},
                        {'label': 'Chad', 'value': 'Chad'},
                        {'label': 'Comoros', 'value': 'Comoros'},
                        {'label': 'Congo', 'value': 'Congo'},
                        {'label': 'Democratic of congo', 'value': 'Democratic of congo'},
                        {'label': 'Djibouti', 'value': 'Djibouti'},
                        {'label': 'Egypt', 'value': 'Egypt'},
                        {'label': 'Eriteria', 'value': 'Eriteria'},
                        {'label': 'Eswatini', 'value': 'Eswatini'},
                        {'label': 'Ethopia', 'value': 'Ethopia'},
                        {'label': 'Gabon', 'value': 'Gabon'},
                        {'label': 'Guinea ', 'value': 'Guinea '},
                        {'label': 'Guinea bissau', 'value': 'Guinea bissau'},
                        {'label': 'Kenya', 'value': 'Kenya'},
                        {'label': 'Lesotho', 'value': 'Lesotho'},
                        {'label': 'Liberia', 'value': 'Liberia'},
                        {'label': 'Madagascar', 'value': 'Madagascar'},
                        {'label': 'Malawi', 'value': 'malawi'},
                        {'label': 'Mali', 'value': 'Mali'},
                        {'label': 'Mauritania', 'value': 'Mauritania'},
                        {'label': 'Mauritus', 'value': 'Mauritus'},
                        {'label': 'Morrocco', 'value': 'Morrocco'},
                        {'label': 'Mozambique', 'value': 'Mozambique'},
                        {'label': 'Namimbia', 'value': 'Namimbia'},
                        {'label': 'Niger', 'value': 'Niger'},
                        {'label': 'Nigeria', 'value': 'Nigeria'},
                        {'label': 'Rwanda', 'value': 'Rwanda'},
                        {'label': 'Sao tome ', 'value': 'Sao tome '},
                        {'label': 'Singapore', 'value': 'Singapore'},
                        {'label': 'Somalia', 'value': 'Somalia'},
                        {'label': 'South africa', 'value': 'South africa'},
                        {'label': 'Sudan', 'value': 'Sudan'},
                        {'label': 'Togo', 'value': 'Togo'},
                        {'label': 'Tunisia', 'value': 'Tunisia'},
                        {'label': 'Zambia', 'value': 'Zambia'},
                        {'label': 'Zimbabwe', 'value': 'Zimbabwe'}
                    ],

                    value='Algeria',
                    multi=False,
                    style={'width': "40%", 'divAlign': 'center'},
                )
            ),

            html.Div(id='output_container1', children=[]),
            html.Br(),

            html.Div(
                [
                    daq.LEDDisplay(
                        id='led_display1',
                        label='Total Cases',
                        value=0,
                        size=50,
                        color="#FF5E5E"
                    ),

                    daq.LEDDisplay(
                        id='led_display2',
                        label='Number of Deaths',
                        value=0,
                        size=50,
                        color="#FF5E5E"
                    ),

                    daq.LEDDisplay(
                        id='led_display3',
                        label='Population',
                        value=0,
                        size=50,
                    ),

                    daq.LEDDisplay(
                        id='led_display4',
                        label='Life Expectancy',
                        value=0,
                        size=50,
                    ),
                    daq.LEDDisplay(
                        id='led_display5',
                        label='Infection Rate (%)',
                        value=0,
                        size=50,
                        color="#FF5E5E"
                    ),
                    daq.LEDDisplay(
                        id='led_display6',
                        label='Death Rate (%)',
                        value=0,
                        size=50,
                        color="#FF5E5E"
                    ),

                ],

                style={'columnCount':3}
            ),

            html.Br(),

            html.H2(' Visualizations', style={'text-align': 'center'}),
            html.Br(),

            dcc.Graph(id='graph1', figure={}),
            html.Br(),
            dcc.Graph(id='graph2', figure={}),
            html.Br(),
            dcc.Graph(id='graph3', figure={}),
            html.Br(),
            dcc.Graph(id='graph4', figure={}),
            html.Br(),
            dcc.Graph(id='graph5', figure={}),
            html.Br(),
            dcc.Graph(id='graph6', figure={}),
            html.Br(),
            dcc.Graph(id='graph7', figure={})
    ]


)


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components


@app.callback(
    [Output(component_id='output_container1', component_property='children'),
        Output(component_id='led_display1', component_property='value'),
        Output(component_id='led_display2', component_property='value'),
        Output(component_id='led_display3', component_property='value'),
        Output(component_id='led_display4', component_property='value'),
        Output(component_id='led_display5', component_property='value'),
        Output(component_id='led_display6', component_property='value'),
        Output(component_id='graph1', component_property='figure'),
        Output(component_id='graph2', component_property='figure'),
        Output(component_id='graph3', component_property='figure'),
        Output(component_id='graph4', component_property='figure'),
        Output(component_id='graph5', component_property='figure'),
        Output(component_id='graph6', component_property='figure'),
        Output(component_id='graph7', component_property='figure'), ],
    Input(component_id='select_country', component_property='value')
)
def page_layout(selected_country):

    dff = df.copy()
    dff2 = df.copy()
    dff = dff[dff['country'] == selected_country]

    message = " The data you are seeing is for: {}".format(selected_country)

    fig1 = px.bar(data_frame=dff2,
                  x='country',
                  y='total_cases',
                  hover_data=['country', 'total_cases'],
                  template='plotly_dark',
                  color='country',
                  title='Reported Cases by Country',
                  labels={'country': 'Countries', 'total_cases': 'Cases'}
                  )

    fig2 = px.bar(data_frame=dff2,
                  x='country',
                  y='number_of_death',
                  hover_data=['country', 'number_of_death'],
                  template='plotly_dark',
                  color='country',
                  title='Reported Deaths by Country',
                  labels={'country': 'Countries', 'number_of_death': 'Deaths'}

                  )

    fig3 = px.scatter(data_frame=dff2,
                      x='total_cases',
                      y='number_of_death',
                      color='country',
                      hover_data=['total_cases', 'number_of_death'],
                      title='Relationship Between Cases and Deaths',
                      template='plotly_dark',
                      labels={'total_cases': 'Cases', 'number_of_death': "Deaths"}
                      )

    fig4 = px.scatter(data_frame=dff2,
                      x='total_cases',
                      y='population',
                      color='country',
                      hover_data=['total_cases', 'population'],
                      title='Relationship Between Cases and Population',
                      template='plotly_dark',
                      labels={'total_cases': 'Cases', 'population': 'Population'})

    fig5 = px.scatter(data_frame=dff2,
                      x='total_cases',
                      y='life_expectancy',
                      color='country',
                      hover_data=['total_cases', 'life_expectancy'],
                      title='Relationship Between Cases and Life Expectancy',
                      template='plotly_dark',
                      labels={'total_cases': 'Cases', 'life_expectancy': 'Life Expectancy'})

    fig6 = px.scatter(data_frame=dff2,
                      x='number_of_death',
                      y='population',
                      color='country',
                      hover_data=['number_of_death', 'population'],
                      title='Relationship Between Deaths and Population',
                      template='plotly_dark',
                      labels={'number_of_death': "Deaths", 'population': 'Population'})

    fig7 = px.scatter(data_frame=dff2,
                      x='number_of_death',
                      y='life_expectancy',
                      color='country',
                      hover_data=['number_of_death', 'life_expectancy'],
                      title='Relationship Between Deaths and Life Expectancy',
                      template='plotly_dark',
                      labels={'number_of_death': 'Deaths', 'life_expectancy': 'Life Expectancy'})


    return [message, dff['total_cases'], dff['number_of_death'],
            dff['population'], dff['life_expectancy'],
            np.round(dff['total_cases']/dff['population'], 3), np.round(dff['number_of_death']/dff['total_cases'], 3),
            fig1, fig2, fig3, fig4, fig5, fig6, fig7
            ]











if __name__ == '__main__':
    app.run_server(debug=True)

