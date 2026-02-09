import dash
from dash import dcc, html  # Updated imports

# create a dash application 
app = dash.Dash(name)

# Define the layout of the dashboard 
app.layout = html.Div(
    children=[
        html.H1('My Dashboard'),
        dcc.Graph(
            id='My-Graph',
            figure={
                'data': [   # 'Data' changed to 'data'
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Bar chart'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': 'line chart'},
                ],
                'layout': {
                    'title': 'Graph title',
                    'xaxis': {'title': 'x-axis'},
                    'yaxis': {'title': 'y-axis'}
                }
            }
        )
    ]
)

# Run the application from the server 
if name == 'main':
    app.run_server(debug=True)
