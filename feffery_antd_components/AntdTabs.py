# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdTabs(Component):
    """An AntdTabs component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): children
- activeKey (string; optional)
- className (string; optional)
- defaultActiveKey (string; default "0")
- id (string; optional)
- nClicksAdd (number; default 0): number of times add button has been clicked
- nClicksRemove (number; default 0): number of times add button has been clicked
- style (dict; optional): new tab to add on click
- tabPosition (string; optional)
- size (string; optional)
- targetKey (string; optional)
- loading_state (dict; optional): loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading
- trigger (string; optional): Used to make it easy in Dash application to detect whether nClicksAadd or nClicksRemove caused component to update"""
    @_explicitize_args
    def __init__(self, children=None, activeKey=Component.UNDEFINED, className=Component.UNDEFINED, defaultActiveKey=Component.UNDEFINED, id=Component.UNDEFINED, nClicksAdd=Component.UNDEFINED, nClicksRemove=Component.UNDEFINED, style=Component.UNDEFINED, tabPosition=Component.UNDEFINED, size=Component.UNDEFINED, targetKey=Component.UNDEFINED, loading_state=Component.UNDEFINED, trigger=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'activeKey', 'className', 'defaultActiveKey', 'id', 'nClicksAdd', 'nClicksRemove', 'style', 'tabPosition', 'size', 'targetKey', 'loading_state', 'trigger']
        self._type = 'AntdTabs'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'activeKey', 'className', 'defaultActiveKey', 'id', 'nClicksAdd', 'nClicksRemove', 'style', 'tabPosition', 'size', 'targetKey', 'loading_state', 'trigger']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdTabs, self).__init__(children=children, **args)
