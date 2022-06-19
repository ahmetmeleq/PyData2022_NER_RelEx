# from : https://plotly.com/python/network-graphs/

from dash import Dash, html
import dash_cytoscape as cyto
import json

with open('elon_musk_results_to_visualize.json','r') as f:
    cytoscape_elements = json.loads(f.read())
    
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Elon Musk Visited:"),
    
    cyto.Cytoscape(
        id='cytoscape',
        elements=cytoscape_elements,
        layout={'name': 'breadthfirst'},
        style={'width': '4000px', 'height': '2000px'}
    )
])


app.run_server(debug=True)