import dash 
from dash.dependencies import Input, Output, State, MATCH, ALL
from dash.exceptions import PreventUpdate
import dash_core_components as dcc 
import dash_html_components as html
import dash_bootstrap_components as dbc 
import feffery_antd_components as fac
import json

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
        id=str(index),
        # key=str(index),
        className="antd-tabpane",
        tab=f"New Tab {index}", # tab title
        children=[
            dbc.Container(
                children=[
                    dbc.Form(
                        children=[
                            dbc.FormGroup(
                                children=[
                                    dbc.InputGroup([
                                        html.H2(f"Tab {index}"),
                                        dbc.Select(
                                            id={"type":"tab-select", "index":index},
                                            options=[
                                                {"value":"yes","label":"yes"}, 
                                                {"value":"no","label":"no"}
                                            ]
                                        ),
                                        dbc.Container(id={"type":"output", "index":index})
                                    ])
                                ]
                            )
                        ]
                    )
                ]
            )
        ],
    )


layout = dbc.Container(
    fluid=True,
    children=[
        # dbc.Button("delete active tab", id="button-delete"),
        dbc.Row([
            dbc.Col([
                fac.AntdTabs(
                    id='antd-tabs-main',
                    children=[
                        create_new_tabpane(0),
                        create_new_tabpane(1)
                        ],
                    className='antd-tabs',
                    style={'height': '200px'},
                    # type='editable-card',
                    defaultActiveKey='0',
                    tabPosition='top',
                    size='small'
                )
            ])
        ])
        
    ]
)

@app.callback(
    [
        Output("antd-tabs-main","children"),
        Output("antd-tabs-main","activeKey")
    ],
    [
        Input("antd-tabs-main","nClicksAdd"),
        Input("antd-tabs-main","nClicksRemove")
    ],
    [
        State("antd-tabs-main","trigger"),
        State("antd-tabs-main","children"),
        State("antd-tabs-main","targetKey")
    ],
)
def add_remove_tab(n_clicks_add, n_clicks_remove, on_edit_trigger, children, targetKey):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    else:
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]


    if n_clicks_add == None:
        n_clicks_add = 0
    if n_clicks_remove == None:
        n_clicks_remove = 0
    if not n_clicks_add and not n_clicks_remove:
        raise PreventUpdate
    
    print("")
    print("add_remove_tab")
    print(f"trigger_id: {trigger_id}")
    print("")
    print("children[0]")
    print(json.dumps(children[0],indent=2))
    
    add = True if on_edit_trigger == "add" else False

    if add:
        newKey = str(max([int(child["props"]["id"]) for child in children])+1)
        children.append(create_new_tabpane(newKey))
        activeKey = str(len(children)-1)
    else:
        for i, child in enumerate(children):
            if str(child["props"]["id"]) == str(targetKey):
                activeKey = str(i - 1);

        children=list(filter(lambda child:not child["props"]["id"]==targetKey, children))

    return [children,activeKey]



# @app.callback(
#     Output("antd-tabs-main","deleteActiveTab"),
#     [Input("button-delete","n_clicks")]
# )
# def delete_tab(n_clicks):
#     if not n_clicks:
#         raise PreventUpdate
#     return True

app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)