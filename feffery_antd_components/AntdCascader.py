# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdCascader(Component):
    """An AntdCascader component.


Keyword arguments:
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- options (optional)
- disabled (boolean; optional)
- changeOnSelect (boolean; default False)
- size (string; optional)
- bordered (boolean; optional)
- placeholder (string; optional)
- defaultValue (list of strings; optional)
- value (list of strings; optional)
- expandTrigger (string; optional)
- popupPlacement (string; optional)
- loading_state (dict; optional): loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, options=Component.UNDEFINED, disabled=Component.UNDEFINED, changeOnSelect=Component.UNDEFINED, size=Component.UNDEFINED, bordered=Component.UNDEFINED, placeholder=Component.UNDEFINED, defaultValue=Component.UNDEFINED, value=Component.UNDEFINED, expandTrigger=Component.UNDEFINED, popupPlacement=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'style', 'options', 'disabled', 'changeOnSelect', 'size', 'bordered', 'placeholder', 'defaultValue', 'value', 'expandTrigger', 'popupPlacement', 'loading_state']
        self._type = 'AntdCascader'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'style', 'options', 'disabled', 'changeOnSelect', 'size', 'bordered', 'placeholder', 'defaultValue', 'value', 'expandTrigger', 'popupPlacement', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdCascader, self).__init__(**args)
