import dash 
from dash.dependencies import Input, Output, State, MATCH, ALL
from dash.exceptions import PreventUpdate
import dash_core_components as dcc 
import dash_html_components as html
import dash_bootstrap_components as dbc 
import dash_daq as daq
import feffery_antd_components as fac
from dash_extensions import Keyboard
from dash_react_force_graph import Graph2D
import json
import copy
import time

def reset_link_source_target(links):
    if links and type(links[0]["source"]) is dict:
        for link in links:
            link["source"] = link["source"]["__nodeId"]
            link["target"] = link["target"]["__nodeId"]
    return links

# def rm_graphdata_render_data(graphdata, graph_lib, coordinates_rm=None):
#     '''
#     @usage remove the data inserted into graphdata by react-force-graph components.
#     @param graphdata: graphdata used by react-force-graph
#     @param graph_lib: one of "2D", "3D" (not yet "AR", "VR")
#     @param coordinates_rm: which coordinates to remove, e.g. ["x","y","z"]
#     @return graphdata, with data removed
#     '''
#     if graphdata and graphdata["links"]:
#         # if coordinates_rm == None:
#         #     coordinates_rm = []
#         # # do not remove indexColor?
#         # # nodes_keys_rm = ["index", "vx","vy"]
#         # nodes_keys_rm = []
#         # if graph_lib == "3D":
#         #     nodes_keys_rm.append("vz")

#         # # links_keys_rm = ["index","__controlPoints"]
#         # links_keys_rm=[]
#         # if graph_lib == "3D":
#         #     nodes_keys_rm.append("__threeObj")
#         #     links_keys_rm += ["__arrowObj",   "__curve", "__lineObj"]
#         # nodes_keys_rm += coordinates_rm
#         # if nodes_keys_rm:
#         #     for i in range(len(graphdata["nodes"])):
#         #         for each_key in nodes_keys_rm:
#         #             if each_key in graphdata["nodes"][i].keys():
#         #                 graphdata["nodes"][i].pop(each_key)
#         # # links
#         # if links_keys_rm:
#         #     for i in range(len(graphdata["links"])):
#         #         for each_key in links_keys_rm:
#         #             if each_key in graphdata["links"][i].keys():
#         #                 graphdata["links"][i].pop(each_key)
#         # reactforcegraph substitutes the whole node object for the id upon render; reverse this for consistency
#         for i in range(len(graphdata["links"])):
#             if not (type(graphdata["links"][i]["source"])) is str:
#                 graphdata["links"][i]["source"] = graphdata["links"][i]["source"]["__nodeId"]
#             if not (type(graphdata["links"][i]["target"])) is str:
#                 graphdata["links"][i]["target"] = graphdata["links"][i]["target"]["__nodeId"]
#     return graphdata


graphdata_init = {
    "nodes":[
        {"__nodeId":"1",  "__is_inferred":False, "name": "Joe Benson", "__nodeLabel":"Joe Benson", "__nodeColor":"cornflowerblue", "__nodeIcon":"\uF007", "__thingType":"person", "__rootType":"entity"},
        {"__nodeId":"2", "__is_inferred":False,  "name": "Daniella M", "__nodeLabel":"Daniella M", "__nodeColor":"cornflowerblue", "__nodeIcon":"\uF007", "__thingType":"person", "__rootType":"entity"},
        {"__nodeId":"3", "__is_inferred":False, "name": "Susan T", "__nodeLabel":"Susan T", "__nodeColor":"cornflowerblue", "__nodeIcon":"\uF007", "__thingType":"person", "__rootType":"entity"},
        {"__nodeId":"4", "__is_inferred":False, "name": "Ed Smith",  "__nodeLabel":"Ed Smith", "__nodeColor":"cornflowerblue", "__nodeIcon":"\uF007", "__thingType":"person", "__rootType":"entity"},
        {"__nodeId":"5",  "__is_inferred":False, "name": "Chevron", "__nodeLabel":"Chevron", "__nodeColor":"cornflowerblue", "__nodeImg":"https://picsum.photos/id/1024/200/200", "__thingType":"corporation", "__rootType":"entity"},
        {"__nodeId":"6",  "__is_inferred":False, "name": "Friends of the Earth", "__nodeLabel":"Friends of the Earth", "__nodeColor":"cornflowerblue", "__nodeImg":"https://picsum.photos/id/10/200/300", "__thingType":"NGO", "__rootType":"entity"},
        {"__nodeId":"7",  "__is_inferred":False, "name": "Strawberry Fields Ltd", "__nodeLabel":"Strawberry Fields Ltd", "__nodeColor":"cornflowerblue", "__nodeImg":"https://picsum.photos/id/11/200/300", "__thingType":"corporation", "__rootType":"entity"},
        {"__nodeId":"8",  "__is_inferred":False, "name": "The Fundamentally Supine Authority", "__nodeLabel":"The Fundamentally Supine Authority", "__nodeColor":"cornflowerblue", "__nodeImg":"https://picsum.photos/id/16/200/300", "__thingType":"government", "__rootType":"entity"},
        {"__nodeId":"9",  "__is_inferred":False, "__nodeLabel":"neighbours", "__nodeColor":"tomato", "__thingType":"neighbours", "__rootType":"relation"},
        {"__nodeId":"10", "__is_inferred":False,  "__nodeLabel":"employment", "__nodeColor":"tomato", "__thingType":"employment", "__rootType":"relation"},
        {"__nodeId":"11", "__is_inferred":False,  "__nodeLabel":"employment", "__nodeColor":"tomato", "__thingType":"employment", "__rootType":"relation"},
        {"__nodeId":"12", "__is_inferred":True, "__nodeLabel":"employment", "__nodeColor":"tomato", "__thingType":"employment", "__rootType":"relation"},
        {"__nodeId":"13", "__is_inferred":False,  "__nodeLabel":"neighbours", "__nodeColor":"tomato", "__thingType":"employment", "__rootType":"relation"},
        {"__nodeId":"14", "__is_inferred":False,  "__nodeLabel":"employment", "__nodeColor":"tomato", "__thingType":"employment", "__rootType":"relation"},
        {"__nodeId":"15", "__is_inferred":False,  "name": "Jenny Howard", "__nodeLabel":"Jenny Howard", "__nodeColor":"cornflowerblue", "__nodeIcon": "\uF007", "__thingType":"person", "__rootType":"entity"}

        ],
    "links":[
        {"id":"1", "label":"employee", "source":"1", "target":"10"},
        {"id":"2", "label":"employee", "source":"2", "target":"10"},
        {"id":"3", "label":"employer", "source":"5", "target":"10"},
        {"id":"4", "label":"employee", "source":"3", "target":"11"},
        {"id":"5", "label":"neighbour", "source":"4", "target":"13"},
        {"id":"6", "label":"employer", "source":"6", "target":"11"},
        {"id":"7", "label":"employer", "source":"8", "target":"12"},
        {"id":"8", "label":"neighbour", "source":"2", "target":"9"},
        {"id":"9", "label":"neighbour", "source":"4", "target":"9"},
        {"id":"10", "label":"neighbour", "source":"1", "target":"13"},
        {"id":"11", "label":"neighbour", "source":"3", "target":"13"},
        {"id":"12", "label":"employee", "source":"4", "target":"12"},
        {"id":"13", "label":"employer", "source":"7", "target":"14"},
        {"id":"14", "label":"employee", "source":"15", "target":"14"},
        {"id":"15", "label":"neighbour", "source":"15", "target":"9"},
        {"id":"16", "label":"neighbour", "source":"15", "target":"15"},
        ]#
    }


app = dash.Dash(__name__, 
    title="Antd tabs demo",
    update_title='Loading...',
    assets_ignore='.*ignore*', 
    prevent_initial_callbacks=True) 


def get_components_matching_trigger_id_variable(
        ctx, 
        id_variable = "index", 
        type_variable = "type1",
        which = "input"
        ):
        '''@usage: in pattern-matching callbacks where the ALL wildcard used, 
            get a list of the input or state components whose id variable matches the callback trigger
        '''
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
        trigger_id_index = json.loads(trigger_id)["index"]

        list_out = []
        list_list_comp = ctx.inputs_list if which == "input" else ctx.states_list 
        for list_comp in list_list_comp:
            if not type(list_comp) is list:
                list_comp = [list_comp]
            for comp in list_comp:
                if not "value" in comp:
                    comp["value"] = None                
                if not type(comp["id"]) is dict:
                    comp["id"] = {type_variable:comp["id"]}
                    list_out.append(comp)
                elif trigger_id_index == comp["id"][id_variable]:
                    list_out.append(comp)
                    break
        return list_out


# returns a tab pane
def create_layout_tab(index, tab_title="New Tab", icon=None):
    return fac.AntdTabPane(
        id=str(index),
        icon=icon,
        # key=str(index), # key == id
        className="antd-tab-pane",
        tabTitle=tab_title, # tab title
        children=[
            dbc.Container(
                children=[
                    dcc.Store(id={"type1":"store-graphdata", "index":index}, storage_type = "session"),
                    dbc.Form(
                        children=[
                            dbc.FormGroup(
                                children=[
                                    dbc.Button(
                                    "add graphData", 
                                    id={"type1":"button-add-graphdata", "index":index}
                                    ),
                                    dbc.Container(id={"type1":"output-nodesSelected-2D", "index":index}),
                                    dbc.Container(id={"type1":"output-linksSelected-2D", "index":index}),
                                    dbc.InputGroup([
                                        html.H2(f"Tab {index}"),
                                        dbc.Select(
                                            id={"type1":"select", "type2":"database", "index":index},
                                            options=[
                                                {"value":"tenancy","label":"tenancy"}, 
                                                {"value":"socialnetwork","label":"socialnetwork"},
                                                {"value":"offshoreleaks","label":"offshoreleaks"}
                                            ]
                                        ),
                                        dbc.Input(
                                            type="color",
                                            value="#4463dd",
                                            id={"type1":"input", "type2":"backgroundcolor", "index":index},
                                        ),
                                        daq.BooleanSwitch(
                                            id={"type1":"booleanswitch", "type2":"useicons", "index":index},
                                            label="use icons"
                                        ),
                                        dbc.Button(children="save",id={"type1":"button", "type2":"tab", "index":index}),
                                        dbc.Container(id={"type1":"output", "type2":"tab", "index":index}),
                                        dcc.Store(id={"type1":"store-database-useicons", "index":index}, data={}, storage_type="session")
                                    ])
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    )


layout = dbc.Container(
    fluid=True,
    children=[
        dcc.Store(id="store-database-backgroundcolor", data={}),
        dcc.Store(id="store-index-counter", data=0),
        dcc.Store(id="store-database-useicons", data={})
    ] +[        
        dcc.Store(id=f"keyboard-{action}", data=0, storage_type="memory") for action in [
            "new-tab",
            "close-tab",
            "move-to-right-tab",
            "move-to-left-tab"
        ]
    ] + [
        Keyboard(id="keyboard"),
        dbc.Row([
            dbc.Col([
                fac.AntdTabs(
                    id="body-tabs",
                    children=[
                        create_layout_tab(index=0, icon="schema"),
                        # create_layout_tab(1)
                        ],
                    className='antd-tabs',
                    forceRender=False,
                    style={'height': '200px'},
                    # type='editable-card',
                    defaultActiveKey='0',
                    tabPosition='top',
                    size='small'
                ),
            ])
        ]),
        dbc.Row(
            dbc.Col(
                dbc.Container(
                    id = "container-graph-component",
                    children=[
                        Graph2D(
                            id="graph2D", 
                            # key="graph2D",
                            # graphData={"nodes":[], "links":[]},#graphdata_init,
                            graphData=graphdata_init,
                            heightRatio=0.6,
                            nodeId="__nodeId",
                            nodeLabel="__nodeLabel",
                            nodeColor="__nodeColor",
                            nodeIcon="__nodeIcon",
                            nodeImg="__nodeImg"
                            #nodeIcon_fontsheets={"FontAwesome":"https://kit.fontawesome.com/a6e0eeba63.js"}
                        ),
                    ]
                ),
            )
        ),
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        html.Div(id="output-nodesSelected"),
                        dcc.Store(
                            id="store-graph-props",
                            data={"0":{}},
                            storage_type="memory"
                        ),
                        dcc.Store(
                            id="store-saved-active-key",
                            data="0", # doesn't work, is initialized as None!
                            storage_type="memory"
                        ),
                    ]
                )
            ]
        )
    ]
)

# register callbacks


@app.callback(
    [
        Output("keyboard-new-tab", "data"),
        Output("keyboard-close-tab","data"),
        Output("keyboard-move-to-right-tab","data"),
        Output("keyboard-move-to-left-tab","data"),
    ],
    [
        Input("keyboard", "n_keydowns")
    ],
    [
        State("keyboard", "keydown"),
    ]
)
def common_store_route_keyboard_event(
    n_keydowns, 
    dict_keydown
    ):
    '''@usage update only the one keyboard store that was triggered
    '''
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    else:
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    keys = ["ctrlKey + t", "ctrlKey + w", "ctrlKey + altKey + ArrowRight", "ctrlKey + altKey + ArrowLeft"]
    list_out = [dash.no_update]*len(keys)  

    list_list_keys = [key_combo.split(" + ") for key_combo in keys]
    for i in range(len(list_list_keys)):
        if dict_keydown["key"] == list_list_keys[i][-1] and all([dict_keydown[modifier] for modifier in list_list_keys[i][0:-1]]):
            list_out[i] = n_keydowns # arbitrary
            break 
    print("")
    print(f"common_store_route_keyboard_event, trigger_id: {trigger_id}")
    return list_out    



@app.callback(
    [
        Output("body-tabs","children"),
        Output("body-tabs","activeKey"),
        Output("store-saved-active-key","data"),
        Output("store-index-counter", "data"),
        Output("graph2D", "graphData"),
        Output("graph2D", "nodesSelected"),
        Output("graph2D", "linksSelected"),
        Output("graph2D", "nodeIdsInvisibleUser"),
        Output("graph2D", "linkIdsInvisibleUser"),
        Output("graph2D", "nodeIdsInvisibleAuto"),
        Output("graph2D", "linkIdsInvisibleAuto"),
        Output("graph2D", "centerAtZoom"),
        Output("store-graph-props","data"),
    ],
    [
        Input("body-tabs","nClicksAdd"),
        Input("body-tabs","nClicksRemove"),

        Input("keyboard-new-tab", "data"),
        Input("keyboard-close-tab","data"),
        Input("keyboard-move-to-right-tab","data"),
        Input("keyboard-move-to-left-tab","data"),

        Input("body-tabs","activeKey"),

        Input({"type1":"button-add-graphdata", "index":ALL}, "n_clicks")
    ],
    [
        State("store-saved-active-key","data"),
        State("body-tabs","children"),
        State("body-tabs","targetKey"),
        State("store-index-counter", "data"),
        State("graph2D", "graphData"),
        State("graph2D", "nodesSelected"),
        State("graph2D", "linksSelected"),
        State("graph2D", "nodeIdsInvisibleUser"),
        State("graph2D", "linkIdsInvisibleUser"),
        State("graph2D", "nodeIdsInvisibleAuto"),
        State("graph2D", "linkIdsInvisibleAuto"),
        State("graph2D", "currentZoomPan"),
        State("store-graph-props","data"),
    ],
)
def add_remove_change_tab(
    n_clicks_add, 
    n_clicks_remove, 

    keyboard_new_tab,
    keyboard_close_tab,
    keyboard_move_right,
    keyboard_move_left,

    activeKey,

    all_n_clicks_add_graphdata,

    previousActiveKey,
    children, 
    targetKey,
    last_index,
    graphdata,
    nodesSelected,
    linksSelected,
    nodeIdsInvisibleUser,
    linkIdsInvisibleUser,
    nodeIdsInvisibleAuto,
    linkIdsInvisibleAuto,
    currentZoomPan, 
    tab_graph2Dprops_store
    ):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    else:
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if not any([
        n_clicks_add, 
        n_clicks_remove,
        keyboard_new_tab, 
        keyboard_close_tab,
        keyboard_move_right,
        keyboard_move_left,
        any(all_n_clicks_add_graphdata)
        ]):
        raise PreventUpdate
    centerAtZoom = dash.no_update
    if activeKey == None:
        activeKey = 0

    # Dash initiates components with null props - even when they have a default value.
    if nodesSelected == None:
        nodesSelected = []
    if linksSelected == None:
        linksSelected = []
    if nodeIdsInvisibleUser == None:
        nodeIdsInvisibleUser = []
    if linkIdsInvisibleUser == None:
        linkIdsInvisibleUser = []
    if nodeIdsInvisibleAuto == None:
        nodeIdsInvisibleAuto = []
    if linkIdsInvisibleAuto == None:
        linkIdsInvisibleAuto = []

    if "keyboard-move-to" in trigger_id or ("body-tabs" in trigger_id and ctx.triggered[0]["prop_id"].split(".")[1] == "activeKey"):
        # note that while tab change by keyboard requires changing children manually,
        # tab change by mouse click is handled by Tabs component itself, so we have to react to change of key
        print("change tab")
        last_index = dash.no_update
        if trigger_id == "keyboard-move-to-right-tab":
            for i, child in enumerate(children):
                if child["props"]["id"] == activeKey:
                    if i < len(children) - 1:
                        newActiveKey = str(children[i+1]["props"]["id"])
                    else:
                        newActiveKey = str(children[0]["props"]["id"])
                    break
        elif trigger_id == "keyboard-move-to-left-tab":
            for i, child in enumerate(children):
                if child["props"]["id"] == activeKey:
                    if i > 0:
                        newActiveKey = str(children[i-1]["props"]["id"])
                    else:
                        newActiveKey = str(children[-1]["props"]["id"])
                    break
        else: 
            newActiveKey = str(activeKey)

        children = dash.no_update

        # stash current Graph2D props for current tab to store
        tab_graph2Dprops_store[previousActiveKey]["graphData"] = graphdata
        for link in tab_graph2Dprops_store[previousActiveKey]["graphData"]["links"]:
            if type(link["source"]) is dict:
                link["source"] = link["source"]["__nodeId"]
                link["target"] = link["target"]["__nodeId"]
            del link["index"]
        tab_graph2Dprops_store[previousActiveKey]["nodesSelected"] = nodesSelected
        for link in linksSelected:
            if type(link["source"]) is dict:
                link["source"] = link["source"]["__nodeId"]
                link["target"] = link["target"]["__nodeId"]
        print("")
        print(f"stashing linksSelected: {linksSelected}")
        tab_graph2Dprops_store[previousActiveKey]["linksSelected"] = linksSelected
        tab_graph2Dprops_store[previousActiveKey]["nodeIdsInvisibleUser"] = nodeIdsInvisibleUser
        tab_graph2Dprops_store[previousActiveKey]["linkIdsInvisibleUser"] = linkIdsInvisibleUser
        tab_graph2Dprops_store[previousActiveKey]["nodeIdsInvisibleAuto"] = nodeIdsInvisibleAuto
        tab_graph2Dprops_store[previousActiveKey]["linkIdsInvisibleAuto"] = linkIdsInvisibleAuto
        tab_graph2Dprops_store[previousActiveKey]["centerAtZoom"] = currentZoomPan
        
        # retrieve stored Graph2D props for new tab
        graphdata = tab_graph2Dprops_store[newActiveKey]["graphData"]
        nodesSelected = tab_graph2Dprops_store[newActiveKey]["nodesSelected"]
        linksSelected = tab_graph2Dprops_store[newActiveKey]["linksSelected"]
        print("")
        print(f"retrieved linksSelected: {linksSelected}")
        nodeIdsInvisibleUser = tab_graph2Dprops_store[newActiveKey]["nodeIdsInvisibleUser"]
        linkIdsInvisibleUser = tab_graph2Dprops_store[newActiveKey]["linkIdsInvisibleUser"]
        nodeIdsInvisibleAuto = tab_graph2Dprops_store[newActiveKey]["nodeIdsInvisibleAuto"]
        linkIdsInvisibleAuto = tab_graph2Dprops_store[newActiveKey]["linkIdsInvisibleAuto"]
        centerAtZoom = tab_graph2Dprops_store[newActiveKey]["centerAtZoom"]

    elif "button-add-graphdata" in trigger_id:
        print("add graphdaa")
        children = newActiveKey = last_index = dash.no_update
        graphdata = copy.deepcopy(graphdata_init)
        nodesSelected = []
        linksSelected = [] 
        nodeIdsInvisibleUser = [] 
        linkIdsInvisibleUser = [] 
        nodeIdsInvisibleAuto = []
        linkIdsInvisibleAuto = []
        centerAtZoom = dash.no_update
        tab_graph2Dprops_store = dash.no_update

    elif (trigger_id == "body-tabs" and ctx.triggered[0]["prop_id"].split(".")[1] == "nClicksAdd") or trigger_id == "keyboard-new-tab":
        print("add tab")
        # add tab
        last_index += 1
        newActiveKey = str(last_index)
        children.append(create_layout_tab(last_index, icon="data"))
        # stash current Graph2D props for current tab to store
        tab_graph2Dprops_store[previousActiveKey]["graphData"] = graphdata
        for link in tab_graph2Dprops_store[previousActiveKey]["graphData"]["links"]:
            if type(link["source"]) is dict:
                link["source"] = link["source"]["__nodeId"]
                link["target"] = link["target"]["__nodeId"]
            # del link["index"]
        tab_graph2Dprops_store[previousActiveKey]["nodesSelected"] = nodesSelected
        for link in linksSelected:
            if type(link["source"]) is dict:
                link["source"] = link["source"]["__nodeId"]
                link["target"] = link["target"]["__nodeId"]
        print("")
        print(f"stashing linksSelected: {linksSelected}")
        tab_graph2Dprops_store[previousActiveKey]["linksSelected"] = linksSelected
        tab_graph2Dprops_store[previousActiveKey]["nodeIdsInvisibleUser"] = nodeIdsInvisibleUser
        tab_graph2Dprops_store[previousActiveKey]["linkIdsInvisibleUser"] = linkIdsInvisibleUser
        tab_graph2Dprops_store[previousActiveKey]["nodeIdsInvisibleAuto"] = nodeIdsInvisibleAuto
        tab_graph2Dprops_store[previousActiveKey]["linkIdsInvisibleAuto"] = linkIdsInvisibleAuto
        tab_graph2Dprops_store[previousActiveKey]["centerAtZoom"] = currentZoomPan
        
        # initialise new
        graphdata = copy.deepcopy(graphdata_init)#{"nodes":[], "links":[]}
        nodesSelected = [] 
        linksSelected = [] 
        nodeIdsInvisibleUser = []
        linkIdsInvisibleUser = [] 
        nodeIdsInvisibleAuto = []
        linkIdsInvisibleAuto = [] 
        centerAtZoom = dash.no_update
        # graph2D store key
        tab_graph2Dprops_store[newActiveKey] = {}
        
    elif ((trigger_id == "body-tabs" and ctx.triggered[0]["prop_id"].split(".")[1] == "nClicksRemove") or trigger_id == "keyboard-close-tab") and len(children)>1:
        print("close tab")
        # delete targetKey tab or current tab if keyboard)
        if trigger_id == "keyboard-close-tab":
            targetKey = activeKey
        for i, child in enumerate(children):
            if child["props"]["id"] == targetKey:
                newActiveKey = children[i+1]["props"]["id"] if i<len(children)-1 else children[-2]["props"]["id"]
                children.pop(i)
                break
        # clean up store from deleted tab
        del tab_graph2Dprops_store[str(targetKey)]
        # retrieve data for next tab
        graphdata = tab_graph2Dprops_store[newActiveKey]["graphData"]
        nodesSelected = tab_graph2Dprops_store[newActiveKey]["nodesSelected"]
        linksSelected = tab_graph2Dprops_store[newActiveKey]["linksSelected"]
        print("")
        print(f"retrieved linksSelected: {linksSelected}")
        nodeIdsInvisibleUser = tab_graph2Dprops_store[newActiveKey]["nodeIdsInvisibleUser"]
        linkIdsInvisibleUser = tab_graph2Dprops_store[newActiveKey]["linkIdsInvisibleUser"]
        nodeIdsInvisibleAuto = tab_graph2Dprops_store[newActiveKey]["nodeIdsInvisibleAuto"]
        linkIdsInvisibleAuto = tab_graph2Dprops_store[newActiveKey]["linkIdsInvisibleAuto"]
        centerAtZoom = tab_graph2Dprops_store[newActiveKey]["centerAtZoom"]
    print("")
    print(f"add_remove_change_tab, trigger_id:   {trigger_id}")  
    # print(f"centerAtZoom: {centerAtZoom}")
    # print(f"tab_graph2Dprops_store: {tab_graph2Dprops_store}")
    return [
        children, 
        newActiveKey,
        newActiveKey, 
        last_index, 
        graphdata,
        nodesSelected,
        linksSelected,
        nodeIdsInvisibleUser,
        linkIdsInvisibleUser,
        nodeIdsInvisibleAuto,
        linkIdsInvisibleAuto,
        centerAtZoom, 
        tab_graph2Dprops_store
        ]


# @app.callback(
#     Output({"type1":"indicator-active-tab","index":ALL}, "data"),
#     [
#         Input("body-tabs","activeKey")
#     ],
#     [
#         State({"type1":"indicator-active-tab","index":ALL}, "data"),
#     ]
# )
# def update_active_tab_indicator(
#     activeKey,
#     list_activetab
#     ):  
#     ctx = dash.callback_context
#     if not ctx.triggered:
#         raise PreventUpdate
#     else:
#         trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    
#     start_time = time.time()
#     list_out = [False if boolean == True else dash.no_update for boolean in list_activetab]
#     list_out[int(activeKey)] = True
#     stop_time = time.time()
#     elapsed = stop_time - start_time
#     print("")
#     print("update_active_tab_indicator")
#     print(f"start_time {start_time}")
#     print(f"time elapsed {elapsed:.1f} seconds")
#     return list_out


# @app.callback(
#     Output({"type1":"graph2D", "index":MATCH}, "graphData"),
#     [
#         Input({"type1":"button-add-graphdata", "index":MATCH}, "n_clicks"),
#         Input("body-tabs","activeKey"),
#     ],
#     [
#         # State({"type1":"graph2D", "index":MATCH}, "graphData"),
#         State({"type1":"graph2D", "index":ALL}, "graphData"),
#     ]
# )
# def new_graphdata(
#     n_clicks_add,
#     activeKey,
#     list_graphdata
#     ):
#     ctx = dash.callback_context
#     if not ctx.triggered:
#         raise PreventUpdate
#     else:
#         trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    
#     print("")
#     print("new_graphdata")
#     print(f"trigger_id: {trigger_id}")

#     if "button-add-graphdata" in trigger_id:
#         return graphdata_init 
#     else:
#         graphdata_out = list_graphdata[int(activeKey)]
#         if graphdata_out:
#             print("")
#             print("rm_graphdata_render_data")
#             return rm_graphdata_render_data(graphdata_out, graph_lib="2D", coordinates_rm=None)
#         else:
#             print("")
#             print("raising P    reventUpdate")
#             raise PreventUpdate


# @app.callback(
#     [
#         Output({"type1":"graph2D", "index":ALL}, "nodeIdsVisibleFilter"),
#         Output({"type1":"graph2D", "index":ALL}, "linkIdsVisibleFilter"),
#         Output("store-graph-props","data"),
#         Output("store-saved-active-key","data")
#     ],
#     [
#         Input("body-tabs","activeKey"),
#     ],
#     [
#         State("store-saved-active-key","data"),
#         State({"type1":"graph2D", "index":ALL}, "nodeIdsVisibleFilter"),
#         State({"type1":"graph2D", "index":ALL}, "linkIdsVisibleFilter"),
#         State("store-graph-props","data")
#     ]
# )
# def toggle_node_visibility_when_switching_tab(
#     newActiveKey,
#     currentActiveKey,
#     list_nodeIdsVisibleFilter,
#     list_linkIdsVisibleFilter,
#     tab_graph2Dprops_store,
#     ):
#     ctx = dash.callback_context
#     if not ctx.triggered:
#         raise PreventUpdate
#     # initialise new ALL nodeIdsVisibleFilter props    
#     list_nodeIdsVisibleFilter_new = [[None] for i in range(len(list_nodeIdsVisibleFilter))]
#     list_linkIdsVisibleFilter_new = [[None] for i in range(len(list_linkIdsVisibleFilter))]
#     # retrieve newActiveKey nodeIdsVisibleFilter and linkIdsVisibleFilter
#     if not newActiveKey in tab_graph2Dprops_store:
#         # initialize if new
#         tab_graph2Dprops_store[newActiveKey] = {}
#         tab_graph2Dprops_store[newActiveKey]["nodeIdsVisibleFilter"] = []
#         tab_graph2Dprops_store[newActiveKey]["linkIdsVisibleFilter"] = []
#     list_nodeIdsVisibleFilter_new[int(newActiveKey)] = tab_graph2Dprops_store[newActiveKey]["nodeIdsVisibleFilter"] 
#     list_linkIdsVisibleFilter_new[int(newActiveKey)] = tab_graph2Dprops_store[newActiveKey]["linkIdsVisibleFilter"] 
#     # stash currentActiveKey nodeIdsVisibleFilter and linkIdsVisibleFilter
#     if not currentActiveKey in tab_graph2Dprops_store:
#         tab_graph2Dprops_store[currentActiveKey] = {}
#     tab_graph2Dprops_store[currentActiveKey]["nodeIdsVisibleFilter"]  = list_nodeIdsVisibleFilter[int(currentActiveKey)] 
#     tab_graph2Dprops_store[currentActiveKey]["linkIdsVisibleFilter"]  = list_linkIdsVisibleFilter[int(currentActiveKey)] 
    
#     return [
#         list_nodeIdsVisibleFilter_new,
#         list_linkIdsVisibleFilter_new,
#         tab_graph2Dprops_store,
#         newActiveKey
#     ]


# @app.callback(
#     [
#         Output("graph2D", "graphData"),
#         Output("graph2D", "centerAtZoom"),
#         Output("store-graph-props","data"),
#     ],
#     [
#         Input("body-tabs","activeKey"),
#         Input({"type1":"button-add-graphdata", "index":ALL}, "n_clicks")
#     ],
#     [
#         State("graph2D", "graphData"),
#         State("graph2D", "currentZoomPan"),
#         State("store-saved-active-key","data"),
#         State("store-graph-props","data"),
#     ], prevent_initial_call=True
# )
# def update_active_tab_graphdata(
#     newActiveKey, 
#     all_n_clicks_add_graphdata,
#     graphdata,
#     currentZoomPan, 
#     currentActiveKey,
#     tab_graph2Dprops_store,
#     ):
#     '''@usage when the active tab changes, 
#     1. save current props to store under the last known active key.
#     2. If new active tab was seen before, retrieve saved props. Else, use init props
#     '''
#     ctx = dash.callback_context
#     if not ctx.triggered:
#         raise PreventUpdate
#     else:
#         trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]


#     # scenarios:

#     # 1. component was initiated with a single new tab (currentActiveKey is empty)
#     #    -> initialise tab_graph2Dprops_store
#     #    -> save centreCoordinates to tab_graph2Dprops_store 
#     #    -> save newActiveKey to store-saved-active-key
#     # 2. user added a new tab and switched to it (newActiveKey in in tab_graph2Dprops_store)
#     #    -> save current props to tab_graph2Dprops_store under currentActiveKey
#     #    -> pan and zoom to default
#     # 3. User clicked button to add graphData
#     #    -> add graphdata
#     # 4. centreCoordinates changed
#     #    -> add new centreCoordinates to tab_graph2Dprops_store
#     # 3. user switched to a previously seen tab 
#     #    -> save current props to tab_graph2Dprops_store 
#     #    -> retrieve props from tab_graph2Dprops_store
#     #


#     #   TODO:
#     # 1. when we initiate a new tab, need to use zoomToFit or simikar
#     #       how get initial zoom, like we get centreCoordinates?
#     # 2. need to call centerAt using difference between current and previous coordinates. But currently 
#     #   currentZoomPan only gets updated on a zoom or pan event. How can we get them? Using centerAt without arguments? See issue
    
#     # optimizing
#     # - use memoizing to avoid overwriting existing saved graphdata if it's the same
#     # - consider updating tab_graph2Dprops_store when graphData or other props change, rather than when activeKey changes
#     # - consider client-side callback
#     # - use destructuring to save and get props en masse

#     # save graphData under current key
#     if not tab_graph2Dprops_store:
#         tab_graph2Dprops_store = {}
#     if trigger_id == "button-add-graphdata":
#         graphdata = graphdata_init
#         centerAtZoom = dash.no_update
#         tab_graph2Dprops_store = dash.no_update
#     elif trigger_id == "body-tabs":
#         if not currentActiveKey: 
#             currentActiveKey = "0"
#         if not newActiveKey: 
#             newActiveKey = "0"
#         if newActiveKey == currentActiveKey:
#             raise PreventUpdate
#         # save current tab graphdata to store
#         if not currentActiveKey in tab_graph2Dprops_store:
#             tab_graph2Dprops_store[currentActiveKey] = {}
#         tab_graph2Dprops_store[currentActiveKey]["graphdata"] = rm_graphdata_render_data(graphdata, graph_lib="2D", coordinates_rm=[])
#         tab_graph2Dprops_store[currentActiveKey]["currentZoomPan"] = currentZoomPan if currentZoomPan else {"k":1.5,"x":0,"y":0}

#         # fix node coordinates for re-creating layout later
#         for i in range(len(tab_graph2Dprops_store[currentActiveKey]["graphdata"]["nodes"])):
#             tab_graph2Dprops_store[currentActiveKey]["graphdata"]["nodes"][i]["fx"] = tab_graph2Dprops_store[currentActiveKey]["graphdata"]["nodes"][i]["x"]
#             tab_graph2Dprops_store[currentActiveKey]["graphdata"]["nodes"][i]["fy"] = tab_graph2Dprops_store[currentActiveKey]["graphdata"]["nodes"][i]["y"]

#         # new tab contents
#         if newActiveKey in tab_graph2Dprops_store:
#             # retrieve graph props from store for new active key
#             graphdata = tab_graph2Dprops_store[newActiveKey]["graphdata"]
#             zoom = [tab_graph2Dprops_store[newActiveKey]["currentZoomPan"]["k"],10]
#             centerAt = [
#                 tab_graph2Dprops_store["centreCoordinates"]["x"]+tab_graph2Dprops_store[newActiveKey]["currentZoomPan"]["x"]-tab_graph2Dprops_store[currentActiveKey]["currentZoomPan"]["x"], 
#                 tab_graph2Dprops_store["centreCoordinates"]["y"]+tab_graph2Dprops_store[newActiveKey]["currentZoomPan"]["y"]-tab_graph2Dprops_store[currentActiveKey]["currentZoomPan"]["y"], 
#                 50
#                 ]# if tab_graph2Dprops_store[currentActiveKey]["currentZoomPan"]["x"] and tab_graph2Dprops_store[currentActiveKey]["currentZoomPan"]["y"] else [0,0,0]
#         else:
#             # initialize empty new tab
#             graphdata = {"nodes":[], "links":[]}
#             zoom = [currentZoomPan["k"],10] if currentZoomPan["k"] else 1.5
#             centerAt = [tab_graph2Dprops_store["centreCoordinates"]["x"], tab_graph2Dprops_store["centreCoordinates"]["y"], 50]

#     # changed tabs. retrieve graphData from store, 
#     print("")
#     print("update_active_tab_graphdata")

#     print(f"zoom:{zoom}")
#     print(f"centerAt:{centerAt}")
#     return [
#         graphdata, 
#         zoom, 
#         centerAt, 
#         tab_graph2Dprops_store, 
#         newActiveKey
#         ]

# @app.callback(
#     [
#         Output({"type1":"graph2D", "index":MATCH}, "nodeIdsInvisibleUser"),
#         Output({"type1":"graph2D", "index":MATCH}, "linkIdsInvisibleUser"),
#     ],
#     [
#         Input({"type1":"graph2D", "index":MATCH}, "pauseAnimation")
#     ],
#     [
#         State({"type1":"graph2D", "index":MATCH}, "graphData"),
#     ], prevent_initial_call = True
# )
# def toggle_nodeIdsInvisibleUser_linkIdsInvisibleUser(
#     pauseAnimation,
#     graphdata
#     ):
#     ctx = dash.callback_context
#     if not ctx.triggered:
#         raise PreventUpdate
#     else:
#         trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

#     if pauseAnimation:
#         nodeIdsInvisibleUser = [node["__nodeId"] for node in graphdata["nodes"]]
#         linkIdsInvisibleUser = [link["id"] for link in graphdata["links"]]
#     else:
#         nodeIdsInvisibleUser = []
#         linkIdsInvisibleUser = []

#     print("")
#     print(f"toggle_nodeIdsInvisibleUser_linkIdsInvisibleUser, trigger_id: {trigger_id}")

#     return [
#         nodeIdsInvisibleUser,
#         linkIdsInvisibleUser
#         ]


# @app.callback(
#     [
#         Output({"type1":"graph2D", "index":MATCH}, "graphData"),
#         Output({"type1":"store-graphdata", "index":MATCH}, "data"),
#         Output({"type1":"graph2D", "index":MATCH}, "pauseAnimation"),
#     ],
#     [
#         Input({"type1":"button-add-graphdata", "index":MATCH}, "n_clicks"),
#         Input("body-tabs","activeKey"),
#         # Input({"type1":"indicator-active-tab","index":MATCH}, "data"),
#     ],
#     [
#         State({"type1":"graph2D", "index":MATCH}, "graphData"),
#         State({"type1":"button-add-graphdata", "index":ALL}, "n_clicks"),
#         State({"type1":"store-graphdata", "index":MATCH}, "data"),
#         State("store-saved-active-key","data"),
#         State("body-tabs","children")
#     ], prevent_initial_call=True
# )
# def update_tab_graphdata(
#     n_clicks_add_graphdata,
#     newActiveKey,
#     graphdata,
#     all_n_clicks_add_graphdata,
#     graphdata_store,
#     currentActiveKey,
#     children
#     ):
#     '''@usage 
#     if user presses button to initialize graphdata (mocking a query), simply update graphdata.
#     '''
#     ctx = dash.callback_context
#     if not ctx.triggered:
#         raise PreventUpdate
#     else:
#         trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
#     if newActiveKey  == None:
#         newActiveKey = children[0]["props"]["id"]

#     if "button-add-graphdata" in trigger_id:
#         # case 1: graphdata was added
#         graphdata = copy.deepcopy(graphdata_init)
#         for node in graphdata["nodes"]:
#             node["__fixed"] = False
#         # nodeIdsInvisibleUser = linkIdsInvisibleUser = []
#         pauseAnimation = dash.no_update
#     else:
#         # user added or deleted a tab, or switched active tab, 
#         for i, child in enumerate(children):
#             if children[i]["props"]["id"] == newActiveKey:
#                 break
#         if str(dash.callback_context.states_list[0]["id"]["index"]) == newActiveKey:# ctx.states_list[1][i]["id"]["index"]:
#             # if the current MATCH is the new active tab
#             print("")
#             print("moved to tab!")
#             graphdata = copy.deepcopy(graphdata_store)
#             graphdata_store = dash.no_update
#             pauseAnimation = False
#         elif str(dash.callback_context.states_list[0]["id"]["index"]) == currentActiveKey:
#             # leaving tab
#             print("")
#             print("left the tab!")
#             if graphdata and graphdata["links"]:
#                 graphdata["links"] = reset_link_source_target(graphdata["links"])
#             # for node in graphdata["nodes"]:
#             #     del node["vx"]
#             #     del node["vy"]
#             #     del node["index"]
#             # for link in graphdata["links"]:
#             #     del link["index"]
#             #     del link["__controlPoints"]
#             graphdata_store = copy.deepcopy(graphdata)
#             graphdata = {"nodes":[], "links":[]}
#             pauseAnimation = True
#         else:
#             raise PreventUpdate
#     print(f"update_tab_graphdata, trigger_id:{trigger_id}")
#     print(f'matching key: {dash.callback_context.states_list[0]["id"]["index"]}')
#     return [
#         graphdata, 
#         graphdata_store,
#         pauseAnimation
#         ]



# @app.callback(
#     Output("store-saved-active-key","data"),
#     [
#         Input({"type1":"graph2D", "index":ALL}, "pauseAnimation"),
#     ],
#     [
#         State("body-tabs","activeKey"),
#         State("body-tabs","children")
#     ]
# )
# def update_store_saved_active_key(
#     list_pauseAnimation, 
#     newActiveKey,
#     children
#     ):
#     '''@usage pauseAnimation is always activated by update_tab_graphdata
#     '''    
#     ctx = dash.callback_context
#     if not ctx.triggered:
#         raise PreventUpdate
#     # print("ctx.triggered")
#     # print(ctx.triggered)
#     print("")
#     print("update_store_saved_active_key")
#     # print(f"newActiveKey: {newActiveKey}")
#     if newActiveKey is None:
#         newActiveKey = children[0]["props"]["id"]
#     return newActiveKey


# @app.callback(
# [
#     Output({"type1":"output-nodesSelected-2D", "index":MATCH}, "children"),
#     Output({"type1":"output-linksSelected-2D", "index":MATCH},  "children"),

# ],
# [
#     Input({"type1":"graph2D", "index":MATCH}, "nodesSelected"),
#     Input({"type1":"graph2D", "index":MATCH}, "linksSelected"),

# ])
# def display_selected_nodes_(
#     nodesSelected,
#     linksSelected
#     ):
#         return [
#         json.dumps(nodesSelected, indent=3),
#         json.dumps(linksSelected, indent=3)
#         ]

# an experiment with ALL outputs. Better to use MATCH here. 


@app.callback(
[
    Output({"type1":"output-nodesSelected-2D", "index":ALL}, "children"),
    Output({"type1":"output-linksSelected-2D", "index":ALL},  "children"),

],
[
    Input({"type1":"graph2D", "index":ALL}, "nodesSelected"),
    Input({"type1":"graph2D", "index":ALL}, "linksSelected"),

],
[
    State("body-tabs","activeKey"),
    State("body-tabs","children")
])
def display_selected_nodes_(
    all_nodesSelected,
    all_linksSelected,
    activeKey,
    children
    ):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    # else:
    #     trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if not activeKey:
        raise PreventUpdate
    for i, child in enumerate(children):
        if child["props"]["id"] == i:
            break
    list_nodesSelected_out = [dash.no_update] * len(ctx.outputs_list[0])
    list_nodesSelected_out[i] = json.dumps(all_nodesSelected[i], indent=3)
    list_linksSelected_out = [dash.no_update] * len(ctx.outputs_list[1])
    list_linksSelected_out[i] = json.dumps(all_linksSelected[i], indent=3)
    return [
    list_nodesSelected_out,
    list_linksSelected_out
    ]


# this callback takes a tab's select value as input and outputs it to a container
@app.callback(
    [
        Output({"type1":"output", "type2":"tab","index":MATCH}, "children"), 
        Output({"type1":"store-database-useicons", "index":MATCH}, "data")
    ],
    [
        Input({"type1":"button", "type2":"tab", "index":MATCH}, "n_clicks")
    ],
    [
        State({"type1":"booleanswitch", "type2":"useicons", "index":MATCH},"on"),
        State({"type1":"select", "type2":"database", "index":MATCH}, "value"),
        State("store-database-useicons","data")
    ]
)
def display_useicon_in_tab_and_save_to_intermediate_store(
    n_clicks, 
    on, 
    database, 
    data_store
    ):
    '''@usage an example of using an intermediate store to output from MATCH inputs to a single output. 
        this callback saves to intermediate store, while useicons_intermediate_to_central_store saves from
        intermediate to central store
    '''
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    else:
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

    print("")
    print(f"display_useicon_in_tab_and_save_to_intermediate_store, trigger_id = {trigger_id}")
    # print("")
    # print(f'Dropdown {tab_id["index"]} = {backgroundcolor}')
    # print(f'json.loads(trigger_id) is type {type(json.loads(trigger_id))}')
    if not data_store:
        data_store = {}
    if database:
        data_store[database] = on
    return [f"use icons: {on}", data_store]



@app.callback(
    [
        Output("store-database-useicons", "data")
    ],
    [
        Input({"type1":"store-database-useicons", "index":ALL}, "data")
    ]
)
def useicons_intermediate_to_central_store(data_store_intermediate):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    else:
        central_store_data = ctx.triggered[0]["value"]
        return [central_store_data]



@app.callback(
        Output("store-database-backgroundcolor", "data"),
    [
        Input({"type1":"button", "type2":"tab", "index":ALL}, "n_clicks")
    ],
    [
        State({"type1":"input", "type2":"backgroundcolor", "index":ALL}, "value"),
        State({"type1":"select", "type2":"database", "index":ALL}, "value"),
        # State({"type1": "input", "type2":"backgroundcolor", "index":ALL}, "id"),
        State("store-database-backgroundcolor", "data")
    ]
)
def save_database_backgroundcolor(n_clicks, backgroundcolor, database, store_data):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    else:
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    print("")
    print(f"save_database_backgroundcolor, trigger_id = {trigger_id}")
    list_comp_state = get_components_matching_trigger_id_variable(
        ctx=ctx, 
        id_variable = "index", 
        type_variable = "type1", 
        which = "state"
        )

    backgroundcolor = list_comp_state[0]["value"]
    database = list_comp_state[1]["value"]
    if not database or not backgroundcolor:
        raise PreventUpdate
    store_data = list_comp_state[2]["value"]

    if not store_data:
        store_data = {}
    store_data[database] = backgroundcolor
    return store_data


app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)