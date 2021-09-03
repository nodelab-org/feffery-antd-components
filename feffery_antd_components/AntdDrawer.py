# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdDrawer(Component):
    """An AntdDrawer component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- visible (boolean; optional)
- title (string; optional)
- placement (string; optional)
- closable (boolean; optional)
- forceRender (boolean; default False)
- destroyOnClose (boolean; default True)
- containerId (string; optional)
- height (number; optional)
- mask (boolean; optional)
- maskClosable (boolean; optional)
- width (number; optional)
- zIndex (number; optional)
- loading_state (dict; optional): loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, visible=Component.UNDEFINED, title=Component.UNDEFINED, placement=Component.UNDEFINED, closable=Component.UNDEFINED, forceRender=Component.UNDEFINED, destroyOnClose=Component.UNDEFINED, containerId=Component.UNDEFINED, height=Component.UNDEFINED, mask=Component.UNDEFINED, maskClosable=Component.UNDEFINED, width=Component.UNDEFINED, zIndex=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'style', 'visible', 'title', 'placement', 'closable', 'forceRender', 'destroyOnClose', 'containerId', 'height', 'mask', 'maskClosable', 'width', 'zIndex', 'loading_state']
        self._type = 'AntdDrawer'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'style', 'visible', 'title', 'placement', 'closable', 'forceRender', 'destroyOnClose', 'containerId', 'height', 'mask', 'maskClosable', 'width', 'zIndex', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdDrawer, self).__init__(children=children, **args)
