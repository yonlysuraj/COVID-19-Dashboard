import numpy as np
import pandas as pd
import plotly.express  as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

external_stylesheets = [{
  'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
  'rel': 'stylesheet',
  'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
  'crossorigin': 'anonymous'
}]

patients=pd.read_csv(r'dataset/IndividualDetails.csv')

total=patients.shape[0]
active=patients[patients['current_status']=='Hospitalized'].shape[0]
recovered=patients[patients['current_status']=='Recovered'].shape[0]
deceased=patients[patients['current_status']=='Deceased'].shape[0]

options=[
    {'label':'All', 'value':'All'},
    {'label':'Hospitalized', 'value':'Hospitalized'},
    {'label':'Recovered', 'value':'Recovered'},
    {'label':'Deceased', 'value':'Deceased'},

]
# Initialize the Dash app
app=dash.Dash(__name__, external_stylesheets=external_stylesheets)  

app.layout = html.Div([
    html.H1('COVID-19 Pandemic Dashboard', className='text-center mb-4'),
    html.Div([
        # Total Cases Card
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Cases", className='text-primary'),
                    html.H4(f"{total:,}"),
                    html.P("Total reported cases", className="text-muted small")
                ], className='card-body'),
            ], className='card shadow-sm'),
        ], className='col-md-3 mb-4'),

        # Deaths Card
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Deaths", className='text-danger'),
                    html.H4(f"{deceased:,}"),
                    html.P("Total deceased cases", className="text-muted small")
                ], className='card-body'),
            ], className='card shadow-sm'),
        ], className='col-md-3 mb-4'),

        # Recovered Card
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered", className='text-success'),
                    html.H4(f"{recovered:,}"),
                    html.P("Total recovered cases", className="text-muted small")
                ], className='card-body'),
            ], className='card shadow-sm'),
        ], className='col-md-3 mb-4'),

        # Active Cases Card
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active Cases", className='text-warning'),
                    html.H4(f"{active:,}"),
                    html.P("Currently hospitalized", className="text-muted small")
                ], className='card-body'),
            ], className='card shadow-sm'),
        ], className='col-md-3 mb-4'),
    ], className='row'),

    # Add dropdown and graph section
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='status-dropdown',
                options=options,
                value='All',
                className='mb-3'
            ),
            dcc.Graph(id='pie-chart'),  # Renamed from status-graph to pie-chart
            dcc.Graph(id='bar-chart')    # Added new bar chart component
        ], className='col-12')
    ], className='row mt-4')
], className='container')

# Update callback to return both figures
@app.callback(
    [Output('pie-chart', 'figure'),
     Output('bar-chart', 'figure')],
    [Input('status-dropdown', 'value')]
)
def update_graphs(selected_status):
    if selected_status == 'All':
        state_counts = patients['detected_state'].value_counts()
        
        # Pie Chart
        pie_fig = px.pie(
            values=state_counts.values,
            names=state_counts.index,
            title='Distribution of COVID-19 Cases by State',
            hole=0.4,
            hover_data=[state_counts.values.round(2)]
        )
        
        # Bar Chart
        bar_fig = px.bar(
            x=state_counts.index,
            y=state_counts.values,
            title='COVID-19 Cases by State',
            labels={'x': 'State', 'y': 'Number of Cases'},
            color=state_counts.values,
            color_continuous_scale='Viridis'
        )
    else:
        filtered_df = patients[patients['current_status'] == selected_status]
        state_status = filtered_df['detected_state'].value_counts()
        
        # Pie Chart
        pie_fig = px.pie(
            values=state_status.values,
            names=state_status.index,
            title=f'Distribution of {selected_status} Cases by State',
            hole=0.4,
            hover_data=[state_status.values.round(2)]
        )
        
        # Bar Chart
        bar_fig = px.bar(
            x=state_status.index,
            y=state_status.values,
            title=f'{selected_status} Cases by State',
            labels={'x': 'State', 'y': 'Number of Cases'},
            color=state_status.values,
            color_continuous_scale='Viridis'
        )
    
    # Update pie chart layout
    pie_fig.update_layout(
        template='plotly_white',
        height=500,
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.1,
            font=dict(size=11)
        ),
        margin=dict(t=50, l=20, r=200, b=20)
    )
    
    # Update bar chart layout
    bar_fig.update_layout(
        template='plotly_white',
        height=500,
        xaxis_tickangle=-45,
        margin=dict(t=50, l=50, r=20, b=120),
        showlegend=False,
    )
    
    # Update pie chart traces
    pie_fig.update_traces(
        textposition='none',
        hovertemplate="<b>%{label}</b><br>Cases: %{customdata[0]}<br>Percentage: %{percent}<extra></extra>",
        pull=[0.03] * len(pie_fig.data[0].labels)
    )
    
    return pie_fig, bar_fig

if __name__ == '__main__':
    app.run(debug=True)