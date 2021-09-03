# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdModal(Component):
    """An AntdModal component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- loading_state (dict; optional): loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading
- title (string; optional)
- visible (boolean; default False)
- okText (string; optional)
- cancelText (string; optional)
- renderFooter (boolean; optional)
- width (number; optional)
- centered (boolean; optional)
- keyboard (boolean; optional)
- closable (boolean; optional)
- mask (boolean; optional)
- maskClosable (boolean; optional)
- okCounts (number; default 0)
- cancelCounts (number; default 0)
- closeCounts (number; default 0)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, loading_state=Component.UNDEFINED, title=Component.UNDEFINED, visible=Component.UNDEFINED, okText=Component.UNDEFINED, cancelText=Component.UNDEFINED, renderFooter=Component.UNDEFINED, width=Component.UNDEFINED, centered=Component.UNDEFINED, keyboard=Component.UNDEFINED, closable=Component.UNDEFINED, mask=Component.UNDEFINED, maskClosable=Component.UNDEFINED, okCounts=Component.UNDEFINED, cancelCounts=Component.UNDEFINED, closeCounts=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'style', 'loading_state', 'title', 'visible', 'okText', 'cancelText', 'renderFooter', 'width', 'centered', 'keyboard', 'closable', 'mask', 'maskClosable', 'okCounts', 'cancelCounts', 'closeCounts']
        self._type = 'AntdModal'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'style', 'loading_state', 'title', 'visible', 'okText', 'cancelText', 'renderFooter', 'width', 'centered', 'keyboard', 'closable', 'mask', 'maskClosable', 'okCounts', 'cancelCounts', 'closeCounts']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdModal, self).__init__(children=children, **args)
