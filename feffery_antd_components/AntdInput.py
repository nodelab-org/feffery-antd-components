# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdInput(Component):
    """An AntdInput component.


Keyword arguments:
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- loading_state (dict; optional): loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading
- mode (string; default 'default')
- placeholder (string; optional)
- size (string; optional)
- addonBefore (string; optional)
- addonAfter (string; optional)
- allowClear (boolean; optional)
- bordered (boolean; optional)
- defaultValue (string; optional)
- disabled (boolean; optional)
- maxLength (number; optional)
- value (string; optional)
- showCount (boolean; optional)
- nSubmit (number; default 0)
- nClicksSearch (number; default 0)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, loading_state=Component.UNDEFINED, mode=Component.UNDEFINED, placeholder=Component.UNDEFINED, size=Component.UNDEFINED, addonBefore=Component.UNDEFINED, addonAfter=Component.UNDEFINED, allowClear=Component.UNDEFINED, bordered=Component.UNDEFINED, defaultValue=Component.UNDEFINED, disabled=Component.UNDEFINED, maxLength=Component.UNDEFINED, value=Component.UNDEFINED, showCount=Component.UNDEFINED, nSubmit=Component.UNDEFINED, nClicksSearch=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'style', 'loading_state', 'mode', 'placeholder', 'size', 'addonBefore', 'addonAfter', 'allowClear', 'bordered', 'defaultValue', 'disabled', 'maxLength', 'value', 'showCount', 'nSubmit', 'nClicksSearch']
        self._type = 'AntdInput'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'style', 'loading_state', 'mode', 'placeholder', 'size', 'addonBefore', 'addonAfter', 'allowClear', 'bordered', 'defaultValue', 'disabled', 'maxLength', 'value', 'showCount', 'nSubmit', 'nClicksSearch']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdInput, self).__init__(**args)
