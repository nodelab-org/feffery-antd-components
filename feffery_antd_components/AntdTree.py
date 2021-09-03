# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdTree(Component):
    """An AntdTree component.


Keyword arguments:
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- treeData (optional)
- showIcon (boolean; default True)
- checkable (boolean; default False)
- defaultExpandAll (boolean; default False)
- defaultExpandedKeys (list of strings; optional)
- defaultExpandParent (boolean; default False)
- multiple (boolean; default False)
- selectable (boolean; default True)
- showLine (dict; default { 'showLeafIcon': false}): showLine has the following type: boolean | dict containing keys 'showLeafIcon'.
Those keys have the following types:
  - showLeafIcon (boolean; optional)
- selectedKeys (list; optional)
- checkedKeys (list; optional)
- height (number; optional)
- loading_state (dict; optional): loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, treeData=Component.UNDEFINED, showIcon=Component.UNDEFINED, checkable=Component.UNDEFINED, defaultExpandAll=Component.UNDEFINED, defaultExpandedKeys=Component.UNDEFINED, defaultExpandParent=Component.UNDEFINED, multiple=Component.UNDEFINED, selectable=Component.UNDEFINED, showLine=Component.UNDEFINED, selectedKeys=Component.UNDEFINED, checkedKeys=Component.UNDEFINED, height=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'style', 'treeData', 'showIcon', 'checkable', 'defaultExpandAll', 'defaultExpandedKeys', 'defaultExpandParent', 'multiple', 'selectable', 'showLine', 'selectedKeys', 'checkedKeys', 'height', 'loading_state']
        self._type = 'AntdTree'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'style', 'treeData', 'showIcon', 'checkable', 'defaultExpandAll', 'defaultExpandedKeys', 'defaultExpandParent', 'multiple', 'selectable', 'showLine', 'selectedKeys', 'checkedKeys', 'height', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdTree, self).__init__(**args)
