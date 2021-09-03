# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdButton(Component):
    """An AntdButton component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- type (string; default 'default')
- href (string; optional)
- target (string; optional)
- block (boolean; default False)
- danger (boolean; default False)
- disabled (boolean; default False)
- shape (string; optional)
- size (string; optional)
- nClicks (number; default 0)
- loading_state (dict; optional): loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, type=Component.UNDEFINED, href=Component.UNDEFINED, target=Component.UNDEFINED, block=Component.UNDEFINED, danger=Component.UNDEFINED, disabled=Component.UNDEFINED, shape=Component.UNDEFINED, size=Component.UNDEFINED, nClicks=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'style', 'type', 'href', 'target', 'block', 'danger', 'disabled', 'shape', 'size', 'nClicks', 'loading_state']
        self._type = 'AntdButton'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'style', 'type', 'href', 'target', 'block', 'danger', 'disabled', 'shape', 'size', 'nClicks', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdButton, self).__init__(children=children, **args)
