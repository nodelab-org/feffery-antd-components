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
def create_layout_tab(index):
    return fac.AntdTabPane(
        id=str(index),
        # key=str(index), # key == id
        className="antd-tabpane",
        tab=f"New Tab", # tab title
        children=[
            dbc.Container(
                children=[
                    html.Div(
                        id = {"type1":"div-graph-component", "index":index},
                        children=[
                            Graph2D(
                                id={"type1":"graph2D", "index":index},
                                key=index,
                                graphData={"nodes":[], "links":[]},#graphdata_init,
                                heightRatio=0.7,
                                nodeId="__nodeId",
                                nodeLabel="__nodeLabel",
                                nodeColor="__nodeColor",
                                nodeIcon="__nodeIcon",
                                nodeImg="__nodeImg",
                                nodeIcon_fontsheets={"FontAwesome":"https://kit.fontawesome.com/a6e0eeba63.js"}
                            ),
                        ]
                    ),
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
                                        dcc.Store(id={"type1":"store-database-useicons", "index":index}, data={})
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
                    id='antd-tabs-main',
                    children=[
                        create_layout_tab(index=0),
                        # create_layout_tab(1)
                        ],
                    className='antd-tabs',
                    style={'height': '800px'},
                    # type='editable-card',
                    defaultActiveKey='0',
                    tabPosition='top',
                    size='small'
                ),
            ])
        ]),
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
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
        Output("antd-tabs-main","children"),
        Output("antd-tabs-main","activeKey"),
        Output("store-index-counter", "data")
    ],
    [
        Input("antd-tabs-main","nClicksAdd"),
        Input("antd-tabs-main","nClicksRemove"),
        Input("keyboard-new-tab", "data"),
        Input("keyboard-close-tab","data"),
        Input("keyboard-move-to-right-tab","data"),
        Input("keyboard-move-to-left-tab","data"),
    ],
    [
        State("antd-tabs-main","trigger"),
        State("antd-tabs-main","children"),
        State("antd-tabs-main","activeKey"),
        State("antd-tabs-main","targetKey"),
        State("store-index-counter", "data")
    ],
)
def add_remove_change_tab(
    n_clicks_add, 
    n_clicks_remove, 
    keyboard_new_tab,
    keyboard_close_tab,
    keyboard_move_right,
    keyboard_move_left,
    on_edit_trigger, 
    children, 
    activeKey,
    targetKey,
    last_index
    ):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    else:
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if n_clicks_add == None:
        n_clicks_add = 0
    if n_clicks_remove == None:
        n_clicks_remove = 0
    if not n_clicks_add and not n_clicks_remove and not keyboard_new_tab and not keyboard_close_tab and not keyboard_move_right and not keyboard_move_left:
        raise PreventUpdate
    
    print("")
    print(children[0])

    if "keyboard-move-to" in trigger_id:
        # note that mouse tab change is handled by Tabs component itself
        
        last_index = dash.no_update
        if trigger_id == "keyboard-move-to-right-tab":
            for i, child in enumerate(children):
                if child["props"]["id"] == activeKey:
                    if i < len(children) - 1:
                        activeKey = children[i+1]["props"]["id"]
                    else:
                        activeKey = children[0]["props"]["id"]
                    break
        elif trigger_id == "keyboard-move-to-left-tab":
            for i, child in enumerate(children):
                if child["props"]["id"] == activeKey:
                    if i > 0:
                        activeKey = children[i-1]["props"]["id"]
                    else:
                        activeKey = children[-1]["props"]["id"]
                    break
        children = dash.no_update
    else:
        add = True if (trigger_id == "antd-tabs-main" and on_edit_trigger == "add") or trigger_id == "keyboard-new-tab" else False
        if add:
            # add tab
            last_index += 1
            activeKey = str(last_index)
            children.append(create_layout_tab(last_index))
        else: 
            # delete targetKey tab
            if len(children)>1:
                if trigger_id == "keyboard-close-tab":
                    targetKey = activeKey
                for i, child in enumerate(children):
                    if child["props"]["id"] == targetKey:
                        activeKey = children[i+1]["props"]["id"] if i<len(children)-1 else children[-2]["props"]["id"]
                        children.pop(i)
                        break
                    # for i, child in enumerate(children):
                    #     if str(child["props"]["id"]) == str(targetKey):
                    #         activeKey = i - 1 
                    #         break
                # else:
                #     activeKey = "0"
                # print("")
                # for i in range(int(activeKey)+1, len(children)):
                #     children[i]["props"]['id'] = str(i-1)
    print("")
    print(f"add_remove_change_tab, trigger_id: {trigger_id}")  
    return [children, activeKey, last_index]


# @app.callback(
#     Output({"type1":"indicator-active-tab","index":ALL}, "data"),
#     [
#         Input("antd-tabs-main","activeKey")
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
#         Input("antd-tabs-main","activeKey"),
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
#         Input("antd-tabs-main","activeKey"),
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
#     dict_graph_props_stored,
#     ):
#     ctx = dash.callback_context
#     if not ctx.triggered:
#         raise PreventUpdate
#     # initialise new ALL nodeIdsVisibleFilter props    
#     list_nodeIdsVisibleFilter_new = [[None] for i in range(len(list_nodeIdsVisibleFilter))]
#     list_linkIdsVisibleFilter_new = [[None] for i in range(len(list_linkIdsVisibleFilter))]
#     # retrieve newActiveKey nodeIdsVisibleFilter and linkIdsVisibleFilter
#     if not newActiveKey in dict_graph_props_stored:
#         # initialize if new
#         dict_graph_props_stored[newActiveKey] = {}
#         dict_graph_props_stored[newActiveKey]["nodeIdsVisibleFilter"] = []
#         dict_graph_props_stored[newActiveKey]["linkIdsVisibleFilter"] = []
#     list_nodeIdsVisibleFilter_new[int(newActiveKey)] = dict_graph_props_stored[newActiveKey]["nodeIdsVisibleFilter"] 
#     list_linkIdsVisibleFilter_new[int(newActiveKey)] = dict_graph_props_stored[newActiveKey]["linkIdsVisibleFilter"] 
#     # stash currentActiveKey nodeIdsVisibleFilter and linkIdsVisibleFilter
#     if not currentActiveKey in dict_graph_props_stored:
#         dict_graph_props_stored[currentActiveKey] = {}
#     dict_graph_props_stored[currentActiveKey]["nodeIdsVisibleFilter"]  = list_nodeIdsVisibleFilter[int(currentActiveKey)] 
#     dict_graph_props_stored[currentActiveKey]["linkIdsVisibleFilter"]  = list_linkIdsVisibleFilter[int(currentActiveKey)] 
    
#     return [
#         list_nodeIdsVisibleFilter_new,
#         list_linkIdsVisibleFilter_new,
#         dict_graph_props_stored,
#         newActiveKey
#     ]


# @app.callback(
#     [
#         Output("graph2D", "graphData"),
#         Output("graph2D", "zoom"),
#         Output("graph2D", "centerAt"),
#         Output("store-graph-props","data"),
#         # Output("store-saved-active-key","data")
#     ],
#     [
#         # Input("antd-tabs-main","activeKey"),
#         Input("button-add-graphdata", "n_clicks"),
#         Input("graph2D", "centreCoordinates")
#     ],
#     [
#         State("graph2D", "graphData"),
#         State("graph2D", "currentZoomPan"),
#         State("store-saved-active-key","data"),
#         State("store-graph-props","data"),
#     ]
# )
# def update_active_tab_graphdata(
#     newActiveKey, 
#     n_clicks_add_graphdata,
#     centreCoordinates,
#     graphdata,
#     currentZoomPan, 
#     currentActiveKey,
#     dict_graph_props_stored,
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
#     #    -> initialise dict_graph_props_stored
#     #    -> save centreCoordinates to dict_graph_props_stored 
#     #    -> save newActiveKey to store-saved-active-key
#     # 2. user added a new tab and switched to it (newActiveKey in in dict_graph_props_stored)
#     #    -> save current props to dict_graph_props_stored under currentActiveKey
#     #    -> pan and zoom to default
#     # 3. User clicked button to add graphData
#     #    -> add graphdata
#     # 4. centreCoordinates changed
#     #    -> add new centreCoordinates to dict_graph_props_stored
#     # 3. user switched to a previously seen tab 
#     #    -> save current props to dict_graph_props_stored 
#     #    -> retrieve props from dict_graph_props_stored
#     #


#     #   TODO:
#     # 1. when we initiate a new tab, need to use zoomToFit or simikar
#     #       how get initial zoom, like we get centreCoordinates?
#     # 2. need to call centerAt using difference between current and previous coordinates. But currently 
#     #   currentZoomPan only gets updated on a zoom or pan event. How can we get them? Using centerAt without arguments? See issue
    
#     # optimizing
#     # - use memoizing to avoid overwriting existing saved graphdata if it's the same
#     # - consider updating dict_graph_props_stored when graphData or other props change, rather than when activeKey changes
#     # - consider client-side callback
#     # - use destructuring to save and get props en masse

#     # save graphData under current key
#     if not dict_graph_props_stored:
#         dict_graph_props_stored = {}
#     if trigger_id == "button-add-graphdata":
#         graphdata = graphdata_init
#         zoom = [currentZoomPan["k"],10] if currentZoomPan["k"] else 1.5
#         centerAt = [0,0,0]
#         dict_graph_props_stored["centreCoordinates"] = centreCoordinates
#     elif trigger_id == "graph2D":
#         # activated by centreCoordinates
#         zoom = [currentZoomPan["k"],10] if currentZoomPan["k"] else 1.5
#         centerAt = [0,0,0]
#         dict_graph_props_stored["centreCoordinates"] = centreCoordinates
#     elif trigger_id == "antd-tabs-main":
#         print("")
#         print(f"currentZoomPan: {currentZoomPan}")
#         if not currentActiveKey: 
#             currentActiveKey = "0"
#         # save current tab graphdata to store
#         if not currentActiveKey in dict_graph_props_stored:
#             dict_graph_props_stored[currentActiveKey] = {}
#         dict_graph_props_stored[currentActiveKey]["graphdata"] = rm_graphdata_render_data(graphdata, graph_lib="2D", coordinates_rm=[])
#         dict_graph_props_stored[currentActiveKey]["currentZoomPan"] = currentZoomPan if currentZoomPan else {"k":1.5,"x":0,"y":0}

#         # fix node coordinates for re-creating layout later
#         for i in range(len(dict_graph_props_stored[currentActiveKey]["graphdata"]["nodes"])):
#             dict_graph_props_stored[currentActiveKey]["graphdata"]["nodes"][i]["fx"] = dict_graph_props_stored[currentActiveKey]["graphdata"]["nodes"][i]["x"]
#             dict_graph_props_stored[currentActiveKey]["graphdata"]["nodes"][i]["fy"] = dict_graph_props_stored[currentActiveKey]["graphdata"]["nodes"][i]["y"]

#         # new tab contents
#         if newActiveKey in dict_graph_props_stored:
#             # retrieve graph props from store for new active key
#             graphdata = dict_graph_props_stored[newActiveKey]["graphdata"]
#             zoom = [dict_graph_props_stored[newActiveKey]["currentZoomPan"]["k"],10]
#             centerAt = [
#                 dict_graph_props_stored["centreCoordinates"]["x"]+dict_graph_props_stored[newActiveKey]["currentZoomPan"]["x"]-dict_graph_props_stored[currentActiveKey]["currentZoomPan"]["x"], 
#                 dict_graph_props_stored["centreCoordinates"]["y"]+dict_graph_props_stored[newActiveKey]["currentZoomPan"]["y"]-dict_graph_props_stored[currentActiveKey]["currentZoomPan"]["y"], 
#                 50
#                 ]# if dict_graph_props_stored[currentActiveKey]["currentZoomPan"]["x"] and dict_graph_props_stored[currentActiveKey]["currentZoomPan"]["y"] else [0,0,0]
#         else:
#             # initialize empty new tab
#             graphdata = {"nodes":[], "links":[]}
#             zoom = [currentZoomPan["k"],10] if currentZoomPan["k"] else 1.5
#             centerAt = [dict_graph_props_stored["centreCoordinates"]["x"], dict_graph_props_stored["centreCoordinates"]["y"], 50]

#     # changed tabs. retrieve graphData from store, 
#     print("")
#     print("update_active_tab_graphdata")

#     print(f"zoom:{zoom}")
#     print(f"centerAt:{centerAt}")
#     return [
#         graphdata, 
#         zoom, 
#         centerAt, 
#         dict_graph_props_stored, 
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


@app.callback(
    [
        Output({"type1":"graph2D", "index":MATCH}, "graphData"),
        Output({"type1":"graph2D", "index":MATCH}, "pauseAnimation")
    ],
    [
        Input({"type1":"button-add-graphdata", "index":MATCH}, "n_clicks"),
        Input("antd-tabs-main","activeKey"),
        # Input({"type1":"indicator-active-tab","index":MATCH}, "data"),
    ],
    [
        State({"type1":"graph2D", "index":MATCH}, "graphData"),
        State({"type1":"button-add-graphdata", "index":ALL}, "n_clicks"),
        State("store-saved-active-key","data"),
        State("antd-tabs-main","children")
    ], prevent_initial_call=True
)
def update_tab_graphdata(
    n_clicks_add_graphdata,
    newActiveKey,
    graphdata,
    all_n_clicks_add_graphdata,
    currentActiveKey,
    children
    ):
    '''@usage 
    if user presses button to initialize graphdata (mocking a query), simply update graphdata.
    '''
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    else:
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if newActiveKey  == None:
        newActiveKey = children[0]["props"]["id"]

    if "button-add-graphdata" in trigger_id:
        # case 1: graphdata was added
        graphdata = copy.deepcopy(graphdata_init)
        # nodeIdsInvisibleUser = linkIdsInvisibleUser = []
        pauseAnimation = dash.no_update
    else:
        print("")
        print(f"newActiveKey: {newActiveKey}")
        for i, child in enumerate(children):
            if children[i]["props"]["id"] == newActiveKey:
                break
        # user added or deleted a tab, or switched active tab, 
        if dash.callback_context.states_list[0]["id"]["index"] == ctx.states_list[1][i]["id"]["index"]:
            # if the current MATCH is the new active tab
            if graphdata and graphdata["links"]:
                graphdata["links"] = reset_link_source_target(graphdata["links"])
            pauseAnimation = False
        else:
            pauseAnimation = True
            graphdata = dash.no_update
    print("")
    print(f"update_tab_graphdata, trigger_id:{trigger_id}")
    print(f'matching key: {dash.callback_context.states_list[0]["id"]["index"]}')
    return [
        graphdata, 
        pauseAnimation
        ]



@app.callback(
    Output("store-saved-active-key","data"),
    [
        Input({"type1":"graph2D", "index":ALL}, "pauseAnimation"),
    ],
    [
        State("antd-tabs-main","activeKey"),
        State("antd-tabs-main","children")
    ]
)
def update_store_saved_active_key(
    list_pauseAnimation, 
    newActiveKey,
    children
    ):
    '''@usage pauseAnimation is always activated by update_tab_graphdata
    '''    
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    # print("ctx.triggered")
    # print(ctx.triggered)
    print("")
    print("update_store_saved_active_key")
    # print(f"newActiveKey: {newActiveKey}")
    if newActiveKey is None:
        newActiveKey = children[0]["props"]["id"]
    return newActiveKey


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
    State("antd-tabs-main","activeKey"),
    State("antd-tabs-main","children")
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