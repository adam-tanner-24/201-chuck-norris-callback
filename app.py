######### Import your libraries #######
import dash
from dash import dcc
from dash import html
from dash import Input, Output, State
from dash.exceptions import PreventUpdate
import os

###### Set up variables
list_of_choices=['Chocolate', 'Vanilla','Butter Pecan','Cookies n Cream','Mint Chocolate Chip',' ']
list_of_pics=['chocolate-ice-cream.png','vanilla-ice-cream.png','butter-pecan-ice-cream.png','cookies-n-cream-ice-cream.png','mint-ice-cream.png','top 5 ice cream.png']
githublink = 'https://github.com/adam-tanner-24/201-chuck-norris-callback'

heading1="America's Top 5 Favorite Ice-Cream Flavors"

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Ice-Cream'

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    html.Br(),
    dcc.Dropdown(id='your-input-here',
                options=[
                    {'label':list_of_choices[0], 'value':list_of_pics[0]},
                    {'label':list_of_choices[1], 'value':list_of_pics[1]},
                    {'label':list_of_choices[2], 'value':list_of_pics[2]},
                    {'label':list_of_choices[3], 'value':list_of_pics[3]},
                    {'label':list_of_choices[4], 'value':list_of_pics[4]},
                    {'label':list_of_choices[5], 'value':list_of_pics[5]},
                ],
                value=list_of_pics[5],
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
    html.Div(id='output-message', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('your-output-here', 'children'),
              dash.dependencies.Output('output-message', 'children'),
              [dash.dependencies.Input('your-input-here', 'value')])
def image(whatever_you_chose):
    if whatever_you_chose is None:
        raise PreventUpdate
        
    image = html.Img(src=app.get_asset_url(whatever_you_chose), style={'width': 'auto', 'height': '50%'})
    split_list = whatever_you_chose.split('-',1)
    message = 'You chose '+split_list[0]+' ice cream flavor'
    return image, message

# @app.callback(dash.dependencies.Output('output-message', 'children'),
#               [dash.dependencies.Input('your-input-here', 'label')])
# def text(whatever_you_chose):
#     disp_val = f'You chose {whatever_you_chose} ice cream.'
#     return disp_val    



######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
