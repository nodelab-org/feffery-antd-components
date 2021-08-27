import dash 
from dash.dependencies import Input, Output, State, MATCH, ALL
from dash.exceptions import PreventUpdate
import dash_core_components as dcc 
import dash_html_components as html
import dash_bootstrap_components as dbc 
import feffery_antd_components as fac

app = dash.Dash(__name__, 
    title="Antd tabs demo",
    update_title='Loading...',
    assets_ignore='.*ignore*', 
    prevent_initial_callbacks=True) 


# register callbacks
# this callback takes a tab's select value as input and outputs it to a container
@app.callback(
    Output({"type":"output", "index":MATCH}, "children"), 
    Input({"type":"tab-select", "index":MATCH}, "value"),
    State({'type': 'tab-select', 'index': MATCH}, "id")
)
def show_selected_value(value, tab_id):
    print(f'Dropdown {tab_id["index"]} = {value}')
    return value

# returns a tab pane
def create_new_tabpane(index):
    return fac.AntdTabPane(
        id=f"{index}",
        className="antd-tabpane",
        tab=f"New Tab {index}", # tab title
        children=[
            dbc.Container(
                children=[
                    dbc.Form(dbc.FormGroup(dbc.InputGroup([
                        html.H2(f"Tab {index}"),
                        dbc.Select(
                            id={"type":"tab-select", "index":index},
                            options=[
                                {"value":"yes","label":"yes"}, 
                                {"value":"no","label":"no"}
                            ]
                        ),
                        dbc.Container(id={"type":"output", "index":index})
                    ])))
                ]
            )
        ],
        key=str(index),
    )


layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Button("+",id="button-add"),
        fac.AntdTabs(
            id='antd-tabs-main',
            children=create_new_tabpane(0),
            className='antd-tabs',
            style={'height': '200px'},
            # type='editable-card',
            defaultActiveKey='0',
            tabPosition='left',
            size='small'
        )
    ]
)

@app.callback(
    Output("antd-tabs-main","children"),
    [Input("button-add","n_clicks")]
)
def add_tab(n_clicks):
    if n_clicks == None:
        raise PreventUpdate
    return create_new_tabpane(n_clicks)
    
app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)