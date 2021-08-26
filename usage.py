import dash 
from dash.dependencies import Input, Output, State, MATCH, ALL
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
@app.callback(
    Output({"type":"output", "index":MATCH}, "children"), 
    Input({"type":"tab-select", "index":MATCH}, "value"),
    State({'type': 'tab-select', 'index': MATCH}, "id")
)
def show_selected_value(value, tab_id):
    print(f'Dropdown {tab_id["index"]} = {value}')
    return value

def create_new_tabpane(index):
    return fac.AntdTabPane(
        id=f"tabpane-{index}",
        className = "antd-tabpane",
        tab=f"New Tab {index}", # tab title
        children=[
            dbc.Container(dbc.Form(dbc.FormGroup(dbc.InputGroup([
                html.H2(f"Tab {index}"),
                dbc.Select(
                    id={"type":"tab-select", "index":index},
                    options=[
                        {"value":"yes","label":"yes"}, 
                        {"value":"no","label":"no"}
                    ]
                ),
                dbc.Container(id={"type":"output", "index":index})
                ]))))
        ],
        key=str(index),
        # closable=True
    )


layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Button("+",id="button-add"),
        fac.AntdTabs(
            id='antd-tabs-main',
            children=[
                create_new_tabpane(0)
            ],
            className='antd-tabs',
            style={'height': '200px'},
            defaultActiveKey='0',
            tabPosition='left',
            size='small',
            type='editable-card'
        )
    ]
)

@app.callback(
    Output("antd-tabs-main","children"),
    [Input("button-add","n_clicks")],
    [State("antd-tabs-main","children")]
)
def add_tab(n_clicks,tabs):
    if n_clicks == None:
        raise PreventUpdate
    tabs.append(create_new_tabpane(n_clicks))
    return tabs
    
app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)